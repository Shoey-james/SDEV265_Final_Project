import sys
from PyQt6.QtWidgets import QApplication
import view.LoginWindow as ld
import controller.controller as ctr  

def load_stylesheet(app):
    """ Loads and applies the global stylesheet. """  
    with open("styles.css", "r") as f:  # Open CSS file and read
        app.setStyleSheet(f.read())  # Apply styles to the app

if __name__ == "__main__":
    """ Program Initialization """
    app = QApplication(sys.argv)  # Initialize QApplication
    load_stylesheet(app)  # Apply styles

    controller = ctr.Controller()  # Initialize the controller
    window = ld.LoginWindow(controller)  # Create the login window
    controller.window = window
    window.show()  # Show the main window
    
    sys.exit(app.exec())  # Start the event loop user1