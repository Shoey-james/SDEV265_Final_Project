import sys
import CreateAccount
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout, QPushButton
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


def LoginWindow():
    print("Login window opened")

def CreateAccountWindow(self):
    # TODO: attach button to open CreateAccount.py page
    print("Create account window opened")


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RecipeSave")
        self.resize(800, 800)
        self.center_window(800, 800)

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("white"))
        self.setPalette(palette)

        # Fonts
        top_font = QFont("Helvetica", 35, QFont.Weight.Bold)
        sub_label_font = QFont("Helvetica", 16)
        button_font = QFont("Helvetica", 12, QFont.Weight.Bold)

        # Colors
        color_font = "Black"
        button_bg = "Beige"
        button_fg = "Black"

        # Title Label
        title = QLabel("RecipeSave", self)
        title.setFont(top_font)
        title.setStyleSheet(f"color: {color_font}; background-color: beige;")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setGeometry(200, 70, 400, 50)

        # Subtitle Label
        subtitle = QLabel("Please log in or create a new account", self)
        subtitle.setFont(sub_label_font)
        subtitle.setStyleSheet(f"color: {color_font}; background-color: white;")
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

        # Login Button
        login_btn = QPushButton("Login to Account", self)
        login_btn.setFont(button_font)
        login_btn.setStyleSheet(f"background-color: {button_bg}; color: {button_fg};")
        login_btn.clicked.connect(self.login_user)
        login_btn.setGeometry(220, 320, 360, 40)  # Button size and position

        # Create Account Button
        create_btn = QPushButton("Create an Account", self)
        create_btn.setFont(button_font)
        create_btn.setStyleSheet(f"background-color: {button_bg}; color: {button_fg};")
        create_btn.clicked.connect(CreateAccountWindow)
        create_btn.setGeometry(220, 380, 360, 40)

    def login_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print(f"[LOGIN] Username: {username}, Password: {password}")

    def center_window(self, width, height):
        screen = QApplication.primaryScreen().availableGeometry()
        x = (screen.width() - width) // 2
        y = (screen.height() - height) // 2
        self.move(x, y)


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
