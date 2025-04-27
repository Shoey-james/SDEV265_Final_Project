from PyQt6.QtWidgets import (
    QApplication, QMainWindow,  QWidget, QLabel, QScrollArea, QVBoxLayout, QTextEdit, QPushButton
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import sqlite3
from collections import defaultdict

# if conversion functions get settled, this will be next
# TODO: change everything over to add recipe display page. will be able to manage recipe db from this page 
# (add/remove recipes,favorite/unfavorite them, access portion calculator possibly from here)
class RecipesWindow(QMainWindow):  
    def __init__(self, controller, rec_id):
        super().__init__()
        self.controller = controller
        self.rec_id = rec_id
        self.setWindowTitle("RecipeSave || Full Recipe View")
        self.resize(1000, 900)
        self.center_window(1000, 900)
        
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
        self.name_label = QLabel(name)
        self.name_label.setObjectName("recFullViewName")
        if image:
            self.img_label = QLabel()
            self.img_label.setObjectName("recipeImage")
            img = QPixmap(image).scaledToWidth(300)
            self.img_label.setPixmap(img)

        # Add widgets to layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.img_label)
        
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