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
        self.resize(800, 600)
        self.center_window(800, 600)
        
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
        # TODO: change button to 
"""
        # Search Button
        login_btn = QPushButton("Search", self)
        login_btn.setFont(button_font)
        login_btn.setStyleSheet(f"background-color: {button_bg}; color: {button_fg};")
        login_btn.clicked.connect(self.search)
        login_btn.setGeometry(300, 200, 100, 30)  # position, button size        
        # table
        # TODO: add table next to search button
        
    def search(self):
        print("searching ")
        # TODO: search button logic

"""

# TODO: repurpose favorite table code to populate a container on recipes window
# that will eventually have functionality of adding/removing recipes and maybe favorites?


"""
    def load_favorites_table(self):
        try:
            print(self.username)
            # Connect to your SQLite database
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()

            # Fetch favorite recipes for the current user
            cursor.execute("SELECT rec_id FROM favorites_table WHERE username = ? ", (self.username,))
            #cursor.execute("SELECT rec_id FROM favorites_table WHERE username = 'user1'")
            rec_tuple = cursor.fetchall()
            
            conn.close()
            return self.load_rec_name(rec_tuple)
            
        except sqlite3.Error as e:
            print("Error loading favorites:", e)
            
    def load_rec_name(self, rec_tuple): # rec name and info get pulled from this function
        print("load_rec_name")
        rec_list = [row[0] for row in rec_tuple] # make the tuple a list
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            if rec_list:  # runs if list is not empty
                placeholders = ','.join(['?'] * len(rec_list)) # creates a list of , and ? for each item in rec_list
                cursor.execute(f"SELECT rec_name, rec_img FROM recipe_table WHERE rec_id IN ({placeholders})", rec_list)
                rec_info = cursor.fetchall()
            else: # runs if there are not recipes in the favorites list
                rec_info = []
            
            conn.close()
            return self.create_favorites_display(rec_info)

            
        except sqlite3.Error as e:
            print("Error loading rec_name:", e)
            
    def create_favorites_display(self, rec_info):
        print("create_favorites_display")
        # Populate the list (from load favorites)
        
        for row in rec_info:
            name = row[0]
            img = row[1]

            # Create widget to hold name and image
            fave_rec_widget = QWidget()
            fave_rec_widget.setObjectName("faveRecWidget")
            layout = QHBoxLayout()
            layout.setContentsMargins(5,5,5,5)

            # Label for the image
            img_label= QLabel()
            img_label.setObjectName("faveImg")
            pixmap = QPixmap(img).scaled(64,64)
            img_label.setPixmap(pixmap)

            # Label for the name
            name_label = QLabel(name)
            name_label.setObjectName("faveRecipeName")


            layout.addWidget(img_label)
            layout.addWidget(name_label)
            fave_rec_widget.setLayout(layout)

            item = QListWidgetItem()
            item.setSizeHint(fave_rec_widget.sizeHint())
            self.favorites_list.addItem(item)
            self.favorites_list.setItemWidget(item, fave_rec_widget)
"""
