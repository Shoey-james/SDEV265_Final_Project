from model.LoginLogic import LoginLogic, CreateAccount
from view.HomePage import HomePage
from view.MyFavoritesWindow import MyFavoritesWindow
from view.LoginWindow import LoginWindow
from view.CreateAccountDisplay import CreateAccountDisplay
import sqlite3
from PyQt6.QtWidgets import (QMessageBox, QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QPushButton, QVBoxLayout, QListWidget, QListWidgetItem)


class Controller:

    def search(self):
        print("searching ")
        # TODO: search button logic

    def create_account(self):
        print("Opening Registration Form")
        self.reg_page = CreateAccountDisplay(self)
        self.reg_page.show()

    def reg_submit_clicked(self, username_input, password_input, fname_input, lname_input, email_input):
        print("Registration form submit button pressed")
        # Assuming this code goes into a method of your PyQt app:

        # These are the inputs you want to validate
        self.username = username_input.text()
        self.password = password_input.text()
        self.fname = fname_input.text()
        self.lname = lname_input.text()
        self.email = email_input.text()

        # Validate input
        if CreateAccount.validate_input(self.username, self.password, self.fname, self.lname, self.email):
            # If validation is successful, create the account
            print("validation passed in account creation. Going to creat_acc logic")
            if CreateAccount.create_acc(self, self.username, self.password, self.fname, self.lname, self.email):
                print("Account was created, closing Create Account page.")
                self.reg_page.close()
                success_box = QMessageBox()
                success_box.setIcon(QMessageBox.Icon.Information)
                success_box.setWindowTitle("Account Created")
                success_box.setText("Account successfully created. Please log in.")
                success_box.exec()


    def login_pressed(self, username_input, password_input):
        print("Login button pressed.")
        username = username_input.text()
        password = password_input.text()
        LoginLogic.validate_login(self, username, password) # pass controller as self 

    def login_successful(self, username):
        self.username = username
        print(f"Controller has received {self.username} as active. Opening Home Page.")
        fname = self.get_fname(self.username)
        self.home = HomePage(self, fname) # pass the controller as "self" and the first name
        self.home.show() # .show opens "HomePage"
        self.window.close() # this will close login page. "window" is LoginWindow class defined in controller.py
        
    # My Favorites button on HomePage.py press logic       
    def favorite_pressed(self):
        print("Favorite button pressed.")
        self.favorite_page = MyFavoritesWindow(self)
        self.favorite_page.show()
    
        
    # sign out button on HomePage.py press logic   
    def exit_pressed(self):     
        print("Sign out button pressed.")
        self.window = LoginWindow(self)
        self.window.show()
        self.home.close()
        
        
    def get_fname(self, username):
        try:
            conn = sqlite3.connect('db_tables/user.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT fname FROM user_table WHERE username=?",
                (username,)
            )
            result = cursor.fetchone()
            conn.close()
            return result if result else None

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None
    """   
    def load_favorites_table(self):
        try:
            # Connect to your SQLite database
            conn = sqlite3.connect("favorites_table.db")  # Replace this with your actual DB file
            cursor = conn.cursor()

            # Fetch favorite recipes for the current user
            cursor.execute("SELECT rec_name FROM favorites_table WHERE user_name = ?", (self.username[0],))
            rows = cursor.fetchall()

            # Populate the list
            for row in rows:
                item = QListWidgetItem(row[0])
                self.favorites_list.addItem(item)

            conn.close()

        except sqlite3.Error as e:
            print("Error loading favorites:", e)
    """ 
