

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,  QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout, QPushButton
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


class CreateAccountDisplay(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("RecipeSave || Create an Account")
        self.resize(800, 800)
        self.center_window(800, 800)
        self.setObjectName("createAccount")

        # Title Label
        title = QLabel("Sign up for Recipe Save!", self)
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(200, 70, 450, 50)

        # Subtitle Label
        subtitle = QLabel("Fill in the fields to create an account", self)
        subtitle.setObjectName("subtitle")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setGeometry(200, 140, 400, 30)

        # Form for Login
        self.form_background = QWidget(self)
        self.form_background.setGeometry(200, 180, 400, 450)
        self.form_background.setObjectName("formBackground")
        self.form_background.lower()

        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setGeometry(220, 200, 360, 40)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setGeometry(220, 260, 360, 40)
        
        self.fname_input = QLineEdit(self)
        self.fname_input.setPlaceholderText("First Name")
        self.fname_input.setGeometry(220, 320, 360, 40)

        self.lname_input = QLineEdit(self)
        self.lname_input.setPlaceholderText("Last Name")
        self.lname_input.setGeometry(220, 380, 360, 40)
        
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Email Address")
        self.email_input.setGeometry(220, 440, 360, 40)
        
        # Create Account Button
        create_btn = QPushButton("Create an Account", self)
        create_btn.setObjectName("accountButtons")
        create_btn.clicked.connect(lambda: self.controller.reg_submit_clicked(self.username_input, self.password_input, self.fname_input, self.lname_input, self.email_input))
        create_btn.setGeometry(220, 500, 360, 40)

    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)



