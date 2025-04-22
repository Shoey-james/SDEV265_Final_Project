from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import sqlite3



class HomePage(QMainWindow):
    def __init__(self, controller, fname, username):
        super().__init__()
        self.controller = controller
        self.current_user = fname
        self.username = username
        self.setWindowTitle("RecipeSave")
        self.resize(800, 800)
        self.center_window(800, 800)


    
        # Home Page
        self.home_page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(5)
        self.setCentralWidget(self.home_page)
        self.home_page.setLayout(layout)


        # Title Label
        self.title = QLabel("Welcome", self)
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        
        # Subtitle Label
        self.subtitle = QLabel(f"   {self.current_user[0]}!", self)
        self.subtitle.setObjectName("name")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Containers, ERICK REFERENCE HERE FOR CONTAINER LOGIC
        """ Logo """
        self.logo_container = QWidget()
        logo_layout = QVBoxLayout()
        self.logo_container.setLayout(logo_layout)
        """ Search """
        self.search_container = QWidget()
        self.search_container.setObjectName("searchContainer")
        self.search_container.setFixedSize(350, 500)
        search_layout = QHBoxLayout()
        self.search_container.setLayout(search_layout)
        
        
        """ Favorites """
        self.favorites_container = QWidget()
        self.favorites_container.setObjectName("favoritesContainer")
        self.favorites_container.setFixedSize(350, 500)
        favorites_layout = QHBoxLayout()
        self.favorites_container.setLayout(favorites_layout)
        # widget for favorite container to display favorites_table db info TODO: finish favorites_table, test functionality of favorites display after
        self.favorites_list = QListWidget() # list widget for displaying favorites
        self.favorites_list.setObjectName("favoritesList")
        favorites_layout.addWidget(self.favorites_list)
        self.load_favorites_table() # populates the favorites list from the database """

        # Horizontal layout to hold search and favorites
        search_fav_layout = QHBoxLayout()
        search_fav_layout.addWidget(self.search_container)
        search_fav_layout.addWidget(self.favorites_container)

        # Logo
        """ Placeholder for photo """
        self.logo_label = QLabel()
        """ Pixmap to add photo  """
        pixmap = QPixmap("images/logo.png")
        pixmap = pixmap.scaledToWidth(650)
        self.logo_label.setPixmap(pixmap)
        logo_layout.addWidget(self.logo_label, alignment=Qt.AlignmentFlag.AlignCenter)
        # Search Recipes
        """ Input Field """
        self.search_bar = QLineEdit()
        """ Button """
        self.search_btn = QPushButton("Search", self)
        self.search_btn.clicked.connect(self.controller.search)
        # Add to Search Layout
        search_layout.addWidget(self.search_bar, alignment=Qt.AlignmentFlag.AlignTop)
        search_layout.addWidget(self.search_btn, alignment=Qt.AlignmentFlag.AlignTop)

        # Add containers to layout
        layout.addWidget(self.logo_container)
        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)
        layout.addLayout(search_fav_layout)
        # table
        # TODO: add table next to search button
        # Note- Look up QListWidget, you might like it better than a table to contain the favorites list
        
        # Sign out button
        exit_btn = QPushButton("Sign Out", self)
        exit_btn.setObjectName("accountButtons")
        exit_btn.clicked.connect(self.controller.exit_pressed)
        exit_btn.setGeometry(608, 250, 120, 30)
        
        # My favorites page pop-up button
        favorite_btn = QPushButton("My Favorites", self)
        favorite_btn.setObjectName("accountButtons")
        favorite_btn.clicked.connect(self.controller.favorite_pressed)
        favorite_btn.setGeometry(170, 250, 140, 30)
        
    
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
            
            
            
    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)
        
        

