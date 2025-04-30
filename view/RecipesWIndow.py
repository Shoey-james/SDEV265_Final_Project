from PyQt6.QtWidgets import (
    QApplication, QMainWindow,  QWidget, QLabel, QScrollArea, QVBoxLayout, QTextEdit, QPushButton, QHBoxLayout, QButtonGroup
)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt, QSize
import sqlite3
from collections import defaultdict

class RecipesWindow(QMainWindow):  
    def __init__(self, controller, rec_id):
        super().__init__()
        self.controller = controller
        self.rec_id = rec_id
        self.ingredient_labels = {}
        self.setWindowTitle("RecipeSave || Full Recipe View")
        self.resize(800, 700)
        self.center_window(800, 700)
        
        # Scroll area for the whole window
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        # Set up the vertical flow of data
        container = QWidget()
        container.setObjectName("fullRecipe")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        container.setLayout(layout)
        scroll_area.setWidget(container)
        self.setCentralWidget(scroll_area)

        # Get the recipe info
        conn = sqlite3.connect('db_tables/tables.db')
        cursor = conn.cursor()

        # Recipe metadata
        cursor.execute("SELECT rec_name, rec_dir, rec_img FROM recipe_table WHERE rec_id = ?", (rec_id,))
        name, directions, image = cursor.fetchone()

        # Load ingredients for the recipe
        cursor.execute("""
                       SELECT ing_id, ing_name, ing_quant, ing_unit, component
                       FROM ingredients_table
                       WHERE rec_id = ?
                       ORDER BY
                            CASE WHEN component IS NULL THEN 1 ELSE 0 END,
                            component
                      """, (rec_id,))
        ingredients = cursor.fetchall()
        conn.close()

# Create widgets to display recipe
        self.title_container = QWidget()
        self.title_container.setObjectName("titleContainer")
        title_layout = QHBoxLayout()
        self.title_container.setLayout(title_layout)
        self.name_label = QLabel(name)
        self.name_label.setObjectName("recFullViewName")
        title_layout.addWidget(self.name_label)
# Favorite button
        self.favbtn = QPushButton("") # Keep this empty JAMES LOL 
        self.favbtn.setObjectName("favoriteButton")
        is_favorited = self.controller.quick_select_favorite(rec_id)

        if is_favorited:
            star = QPixmap("images/star_filled.png")
            
        else:
            star = QPixmap("images/star_outline.png")
            
        print(star.isNull())  # Will print True if image failed to load
        width = 20
        height = 20
        resized_star = star.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
        #icon = QIcon(resized_star)
        self.favbtn.setIcon(QIcon(resized_star))
        self.favbtn.setIconSize(QSize(20, 20)) 
        self.favbtn.setFixedSize(30, 30)
        self.favbtn.setFlat(True)
        self.favbtn.clicked.connect(lambda: self.controller.favbtn_pressed(self.favbtn, rec_id))
        title_layout.addWidget(self.favbtn)
        layout.addWidget(self.title_container)

        if image:
            self.img_label = QLabel()
            self.img_label.setObjectName("recipeImage")
            img = QPixmap(image).scaledToWidth(300)
            self.img_label.setPixmap(img)
        layout.addWidget(self.img_label)
        

        # Scaling buttons
        self.button_container = QWidget()
        self.button_container.setObjectName("scalingButtonContainer")
        button_layout = QHBoxLayout()
        self.button_container.setLayout(button_layout)
        self.scaling_buttons = QButtonGroup()
        self.onex = QPushButton("1x")
        self.twox = QPushButton("2x")
        self.threex = QPushButton("3x")
        self.fourx = QPushButton("4x")

        for i, sc_btn in enumerate([self.onex, self.twox, self.threex, self.fourx]):
            sc_btn.setObjectName("scalingButtons")
            self.scaling_buttons.addButton(sc_btn, i+1)
            button_layout.addWidget(sc_btn)

        self.scaling_buttons.buttonClicked.connect(lambda button: self.controller.scaling_pressed(button, self.scaling_buttons, self.rec_id))

        layout.addWidget(self.button_container)

        #Group Ingredients
        grouped = self.group_by_comp(ingredients)
        for component, ing_list in grouped.items():
            if component:
                self.comp_label = QLabel(component)
                self.comp_label.setObjectName("component")
                layout.addWidget(self.comp_label)
            for ingredient in ing_list:
                self.ing_label = QLabel(f"{ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")
                self.ing_label.setObjectName("ingredient")
                self.ingredient_labels[ingredient['ing_id']] = self.ing_label
                layout.addWidget(self.ing_label)

        # Create widget for directions
        self.directions_text = QTextEdit()
        self.directions_text.setObjectName("directions")
        self.directions_text.setReadOnly(True)
        self.directions_text.setPlainText(directions)
        self.directions_text.setMaximumWidth(800) 
        directions_height = self.directions_text.size().height()
        self.directions_text.setFixedHeight(int(directions_height) + 50)
        layout.addWidget(self.directions_text)

    def group_by_comp(self, ingredients):
        grouped = defaultdict(list)

        for ing_id, name, quantity, unit, component in ingredients:
            grouped[component].append({
                "ing_id": ing_id,
                "name": name,
                "quantity": quantity,
                "unit": unit,
            })

        return grouped
    


        
    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)