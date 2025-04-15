# login_logic.py
import sqlite3
import re
import PyQt6
from PyQt6.QtWidgets import QMessageBox, QVBoxLayout

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

    def validate_input(username, password, fname, lname, email):
        """
        Validates the user input: username, password, first name, last name, email, phone number, and counselor's ID.
        Returns: True if all inputs are valid, False otherwise.
        """
        print("validate_input initiated")
        if not all([username, password, fname, lname, email]):
            print("All fields are required!")
            return False
        
        # Username validation: must be at least 4 characters long (up to 12), have at least 1 letter/1 digit, and no special characters
        username_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{4,12}$'
        if not re.match(username_regex, username):
            print("Username must be 4-12 characters long, have one digit and one letter, and have no special characters!")
            return False

        # Password validation: Must be at least 8 characters long and contain at least one letter and one digit
        password_regex = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
        if not re.match(password_regex, password):
            print("Password should be at least 8 characters long, and contain at least one letter and one number!")
            return False
        
        # Name validation: Only letters and spaces, between 2 and 30 characters
        fname_regex = r'^[A-Za-z\s]{2,30}$'
        if not re.match(fname_regex, fname):
            print("First and last names should only contain letters and spaces, and be between 2 and 30 characters.")
            return False
        
        # Name validation: Only letters and spaces, between 2 and 30 characters
        lname_regex = r'^[A-Za-z\s]{2,30}$'
        if not re.match(lname_regex, lname):
            print("First and last names should only contain letters and spaces, and be between 2 and 30 characters.")
            return False
        
        # Email validation: Basic email format check
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            print("Please enter a valid email address.")
            return False
        
        try:
            # connect to DB
            conn = sqlite3.connect('db_tables/user.db')
            cursor = conn.cursor()

            # Check for existing username and/or email
            cursor.execute("SELECT * FROM user_table WHERE username = ? OR email = ?", (username, email))
            if cursor.fetchone():
                print("Username, or email already exists!")
                conn.close()
                return False

            conn.close()
            
        except sqlite3.Error as e:  # Handle any SQLite database errors
            print(f"An error occurred: {e}")
            return False
        
        return True

    def create_acc(self, username, password, fname, lname, email):
        """
        Collects user input, validates the data, and inserts a new patient record into the database.
        Ensures proper error handling to prevent database integrity issues.
        """
        print("create_acc")
        """self.username = username
        self.password = password
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone"""

        # Validate the input fields and create the account if valid
        if not self.validate_input(self, username, password, fname, lname, email):
            return  # Stop execution if validation fails
        
        try:
            conn = sqlite3.connect('db_tables/user.db')
            cursor = conn.cursor()
            # Insert the new patient record into the patient_users table
            cursor.execute('''INSERT INTO user_table (username, password, fname, lname, email
                            VALUES (?, ?, ?, ?, ?, ?)''', (username, password, fname, lname, email))
            conn.commit()
            conn.close()
            print("Account created successfully!")
        except (sqlite3.IntegrityError, sqlite3.Error) as e:
            print(f"An error occurred: {e}")
# TODO: continue fixing if/try statement above to match current db and attributes. figure out how to handle user_id in user_table
"""
    def show_error(self, message):
        #Helper method to show error message box.
        QMessageBox.critical(self, "Error", message)

    def show_info(self, message):
        #Helper method to show info message box.
        QMessageBox.information(self, "Success", message)
        
"""