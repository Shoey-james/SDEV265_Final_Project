from PyQt6.QtWidgets import (
    QApplication, QMainWindow,  QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout, QPushButton
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt

# if conversion functions get settled, this will be next
# TODO: change everything over to add recipe display page. will be able to manage recipe db from this page 
# (add/remove recipes,favorite/unfavorite them, access portion calculator possibly from here)
class RecipesWindow(QMainWindow):  
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("RecipeSave || My Recipes")
        self.resize(800, 800)
        self.center_window(800, 800)
        self.setObjectName("myRecipes")
        
        
        # TODO: repurpose for container 
        """ 
        self.favorites_container = QWidget()
        self.favorites_container.setObjectName("favoritesContainer")
        self.favorites_container.setFixedSize(350, 500)
        favorites_layout = QHBoxLayout()
        self.favorites_container.setLayout(favorites_layout)
        
        # widget for favorite container to display favorites_table db info TODO: finish favorites_table, test functionality of favorites display after
        
        self.favorites_list = QListWidget() # list widget for displaying favorites
        self.favorites_list.setObjectName("favoritesList")
        favorites_layout.addWidget(self.favorites_list)
        self.load_favorites_table() # populates the favorites list from the database 

        # Horizontal layout to hold search and favorites
        
        search_fav_layout = QHBoxLayout()
        
        """
        
    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)

        # Title Label
        title = QLabel("RecipeSave", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(200, 70, 400, 50)

        # Subtitle Label
        subtitle = QLabel("Welcome!", self)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setGeometry(200, 140, 400, 30)
        
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
