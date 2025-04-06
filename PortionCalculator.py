import sys
import CreateAccount
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QFormLayout, QPushButton, QTableWidget, QVBoxLayout, QGridLayout
)
from PyQt6.QtGui import QFont, QColor, QPalette
from PyQt6.QtCore import Qt


def PortionCalcWindow():
    print("PortionCalc window opened")



class PortionCalcWindow(QWidget):
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
        subtitle = QLabel("Welcome!", self)
        subtitle.setFont(sub_label_font)
        subtitle.setStyleSheet(f"color: {color_font}; background-color: white;")
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


def main():
    app = QApplication(sys.argv)
    window = PortionCalcWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
