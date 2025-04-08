from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap



class MainWindow(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("RecipeSave")
        self.resize(800, 800)
        self.center_window(800, 800)

        #self.setAutoFillBackground(True)

        # Home Page
        self.home_page = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(5)
        self.setCentralWidget(self.home_page)
        self.home_page.setLayout(layout)


        # Title Label
        self.title = QLabel("RecipeSave", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.title.setGeometry(200, 70, 400, 50)

        # Subtitle Label
        self.subtitle = QLabel("Welcome!", self)
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        #self.subtitle.setGeometry(200, 140, 400, 30)

        # Containers
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

    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)

