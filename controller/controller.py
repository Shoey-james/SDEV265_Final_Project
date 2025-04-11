from model.LoginLogic import LoginLogic, CreateAccount
from view.HomePage import HomePage
from view.CreateAccountDisplay import CreateAccountDisplay
import sqlite3


class Controller:

    def search(self):
        print("searching ")
        # TODO: search button logic

    def create_account(self):
        print("Opening Registration Form")
        self.reg_page = CreateAccountDisplay(self)
        self.reg_page.show()

    def reg_submit_clicked(self, username_input, password_input, fname_input, lname_input, email_input, phone_input):
        print("Registration form submit button pressed")
        username = username_input.text()
        password = password_input.text()
        fname = fname_input.text()
        lname = lname_input.text()
        email = email_input.text()
        phone = phone_input.text()
        CreateAccount.validate_new_user(username, password, fname, lname, email, phone)

    def login_pressed(self, username_input, password_input):
        print("Login button pressed.")
        username = username_input.text()
        password = password_input.text()
        LoginLogic.validate_login(self, username, password)

    def login_successful(self, username):
        self.username = username
        print(f"Controller has received {self.username} as active. Opening Home Page.")
        fname = self.get_fname(self.username)
        self. home = HomePage(self, fname)
        self.home.show()
        self.window.close()
        
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