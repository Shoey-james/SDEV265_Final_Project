# login_logic.py
import sqlite3
from PyQt6.QtWidgets import QMessageBox

class LoginLogic:
    def validate_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        user_info = self.check_credentials(username, password)

        if user_info:
            username, password = user_info
            print(f"Login successful! Welcome {username}")
            # Trigger controller method or move to next window if needed
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password.")

    def check_credentials(self, username, password):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()

            cursor.execute(
                "SELECT username, password FROM user_table WHERE username=? AND password=?",
                (username, password)
            )
            result = cursor.fetchone()
            conn.close()
            return result if result else None

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            return None

