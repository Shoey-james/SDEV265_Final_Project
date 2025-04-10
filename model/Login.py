# login logic
# TODO: finish changing this to reflect the database tables in this project
""" import sqlite3
from PyQt6.QtWidgets import QMessageBox

def validate_login(self):
    """
    #Validate the login credentials and open the User account if valid. Otherwise, display an error message.
    """
    # Get username and password from the line edits
    username = self.username_input.text()
    password = self.password_input.text()

    # Check if username and password exist
    user_info = self.check_credentials(username, password)

    if user_info:
        # Extract the user type and result
        user_type, result = user_info
        user_id, firstname, lastname = result
        print(f"Login successful! Welcome {firstname}")
    else:
        # Show error message box
        QMessageBox.critical(self, "Login Failed", "Invalid username or password.")


def check_credentials(self, username, password):
    """
    #Validate the login values against the database.
    #Returns a tuple with user type and (ID, first name, last name) if valid, otherwise None.
    """
    try:
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()

        # Check user login
        cursor.execute(
            "SELECT  FROM patient_users WHERE p_username=? AND p_password=?",
            (username, password)
        )
        result = cursor.fetchone()
        if result:
            conn.close()
            return ("patient", result)

        # Check counselor login
        cursor.execute(
            "SELECT c_id, c_first_name, c_last_name FROM counselor_users WHERE c_username=? AND c_password=?",
            (username, password)
        )
        result = cursor.fetchone()
        if result:
            conn.close()
            return ("counselor", result)

        conn.close()
        return None

    except sqlite3.Error as e:
        QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        return None
"""