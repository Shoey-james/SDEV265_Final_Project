# login_logic.py
import sqlite3
import re
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
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Warning)
            error_box.setWindowTitle("Login Failed")
            error_box.setText("Invalid username or password.")
            error_box.exec()
            
    def check_credentials(username, password):
        try:
            conn = sqlite3.connect('db_tables/tables.db')
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
        username_regex = r'^(?=.*[a-z])(?=.*\d)[A-Za-z\d]{4,12}$'
        if not re.match(username_regex, username):
            print("Username must be 4-12 characters long, all lowercase, have one digit and one letter, and have no special characters!")
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
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()

            # Check for existing username and/or email
            cursor.execute("SELECT * FROM user_table WHERE username = ? OR email = ?", (username, email))
            if cursor.fetchone():
                print("Username, or email already exists!")
                conn.close()
                return False

            conn.close()

        except sqlite3.IntegrityError as e:  # Handle UNIQUE constraint failures, since username is key and must be unique.
            print(f"Integrity error occurred: {e}")
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Warning)
            error_box.setWindowTitle("Account Creation Failed") # It is a database error but user doesn't need to see that.
            error_box.setText("An account with this username may already exist.")
            error_box.exec()
            return False
            
        except sqlite3.Error as e:  # Handle any SQLite database errors
            print(f"A DATABASE error occurred: {e}")
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Icon.Warning)
            error_box.setWindowTitle("Unexpected Error") # It is a database error but user doesn't need to see that.
            error_box.setText("An unexpected error occured while creating your account.")
            error_box.exec()
            return False
        return True

    def create_acc(controller, username, password, fname, lname, email):
        this_controller = controller
        """
        Collects user input, validates the data, and inserts a new patient record into the database.
        Ensures proper error handling to prevent database integrity issues.
        """
        print("create_acc")
        
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            # Insert the new patient record into the patient_users table
            cursor.execute('''INSERT INTO user_table (username, password, fname, lname, email)
                            VALUES (?, ?, ?, ?, ?)''', (username, password, fname, lname, email))
            conn.commit()
            conn.close()
            print("Account created successfully!")
            return True
            
        except (sqlite3.IntegrityError, sqlite3.Error) as e:
            print(f"An error occurred: {e}")
