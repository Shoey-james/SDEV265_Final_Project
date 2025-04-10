
import view.LoginWindow as LoginWindow
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout, QPushButton
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


class CreateAccountDisplay():
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecipeSave || Create an Account")
        self.resize(800, 800)
        self.center_window(800, 800)

        # Title Label
        title = QLabel("RecipeSave", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(200, 70, 400, 50)

        # Subtitle Label
        subtitle = QLabel("Fill in the fields to create an account", self)
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setGeometry(200, 140, 400, 30)

        # Form for Login
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setGeometry(220, 200, 360, 40)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(220, 260, 360, 40)
        
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("First Name")
        self.username_input.setGeometry(220, 320, 360, 40)

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Last Name")
        self.username_input.setGeometry(220, 380, 360, 40)
        
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Email Address")
        self.username_input.setGeometry(220, 440, 360, 40)
        
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Phone Number")
        self.username_input.setGeometry(220, 500, 360, 40)

        # Create Account Button
        create_btn = QPushButton("Create an Account", self)
        create_btn.clicked.connect()
        create_btn.setGeometry(220, 560, 360, 40)

    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)



