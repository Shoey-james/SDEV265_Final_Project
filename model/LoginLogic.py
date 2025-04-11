# login_logic.py
import sqlite3
from PyQt6.QtWidgets import QMessageBox

class LoginLogic:
    @staticmethod
    def validate_login(controller, username, password):
    
        user_info = LoginLogic.check_credentials(username, password)

        if user_info:
            username, password = user_info
            print(f"Login successful! Welcome {username}")
            controller.login_successful(username)
        else:
            QMessageBox.critical("Login Failed", "Invalid username or password.")

    def check_credentials(username, password):
        try:
            conn = sqlite3.connect('db_tables/user.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT username, password FROM user_table WHERE username=? AND password=?",
                (username, password)
            )
            result = cursor.fetchone()
            conn.close()
            return result if result else None

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None

class CreateAccount:

    def validate_new_user(controller, username, password, fname, lname, email, phone):
        username_taken = CreateAccount.check_username(username)
        if username_taken:
            print(f"Username already exists.")
    #TODO:
    # tHIS NEEDS FINISHING.

    def check_username(username):
        try:
            conn = sqlite3.connect('db_tables/user.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT username FROM user_table WHERE username=?",
                (username,)
            )
            result = cursor.fetchone()
            conn.close()
            return result if result else None

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None