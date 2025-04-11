
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel
)
from PyQt6.QtCore import Qt


class RecipesDisplay():
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("RecipeSave")
        self.resize(800, 800)
        self.center_window(800, 800)

        # Title Label
        title = QLabel("RecipeSave", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(200, 70, 400, 50)

        # Subtitle Label
        subtitle = QLabel("Welcome!", self)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setGeometry(200, 140, 400, 30)
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
    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)