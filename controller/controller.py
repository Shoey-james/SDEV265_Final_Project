from model.LoginLogic import LoginLogic, CreateAccount
from view.HomePage import HomePage, SearchPopupWindow
from view.RecipesWIndow import RecipesWindow
from view.LoginWindow import LoginWindow
from view.CreateAccountDisplay import CreateAccountDisplay
import sqlite3
from PyQt6.QtWidgets import QMessageBox


class Controller:

    def search(self, search_bar, page):
        print("searching")
        try:
        # Connect to your SQLite database
            user_query = search_bar.text()
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()

            # Search for recipes where rec_name partially matches the search query
            cursor.execute(
                "SELECT rec_id FROM recipe_table WHERE rec_name LIKE ?", ('%' + user_query + '%',)
            )
            #cursor.execute("SELECT rec_id FROM favorites_table WHERE username = 'user1'")
            search_tuple = cursor.fetchall()
            
            conn.close()
            return self.load_searched_rec(search_tuple, page)

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None
        
    def load_searched_rec (self, search_tuple, page): # rec name and info get pulled from this function
        print("load_rec_name")
        search_list = [row[0] for row in search_tuple] # make the tuple a list
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            if search_list:  # runs if list is not empty
                placeholders = ','.join(['?'] * len(search_list)) # creates a list of , and ? for each item in rec_list
                cursor.execute(f"SELECT rec_id, rec_name, rec_img, rec_desc FROM recipe_table WHERE rec_id IN ({placeholders})", search_list)
                search_info = cursor.fetchall()
            else: # runs if there are not recipes in the favorites list
                search_info = []
            
            conn.close()
            return page.search_display(search_info)

            
        except sqlite3.Error as e:
            print("Error loading rec_name:", e)

    def all_recipes(self, page):
        print("retrieveing all recipes")
        try:
        # Connect to database
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()

            # Search for all recipes
            cursor.execute("SELECT rec_id FROM recipe_table")
            recipe_tuple = cursor.fetchall()
            
            conn.close()
            return self.load_all_rec(recipe_tuple, page)

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None
        
    def load_all_rec (self, recipe_tuple, page): # rec name and info get pulled from this function
        print("load_rec_name")
        recipe_list = [row[0] for row in recipe_tuple] # make the tuple a list
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            if recipe_list:  # runs if list is not empty
                placeholders = ','.join(['?'] * len(recipe_list)) # creates a list of , and ? for each item in rec_list
                cursor.execute(f"SELECT rec_id, rec_name, rec_img, rec_desc FROM recipe_table WHERE rec_id IN ({placeholders})", recipe_list)
                all_info = cursor.fetchall()
            else: # runs if there are not recipes in the favorites list
                all_info = []
            
            conn.close()
            return page.search_display(all_info)

            
        except sqlite3.Error as e:
            print("Error loading rec_name:", e)

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
        self.home = HomePage(self, fname, self.username) # pass the controller as "self" and the first name
        self.home.show() # .show opens "HomePage"
        self.window.close() # this will close login page. "window" is LoginWindow class defined in controller.py
        
    # My Favorites button on HomePage.py press logic       
    def recipes_pressed(self, rec_id):
        print("Recipe Full view button pressed.")
        self.full_recipe_view = RecipesWindow(self, rec_id)
        self.full_recipe_view.show()
    
        
    # sign out button on HomePage.py press logic   
    def exit_pressed(self):     
        print("Sign out button pressed.")
        self.window = LoginWindow(self)
        self.window.show()
        self.home.close()
        
        
    def get_fname(self, username):
        try:
            conn = sqlite3.connect('db_tables/tables.db')
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

    def scaling_pressed(self, clicked_button, scaling_buttons):
        print(clicked_button, "pressed.")
        # First, reset all scaling buttons
        for button in scaling_buttons:
            button.setStyleSheet("""
                QPushButton#scalingButtons {
                    color: white;
                    min-width: 40px;
                    min-height: 40px;
                    max-width: 40px;
                    max-height: 40px;
                    padding: 4px 8px;
                    border-radius: 12px;
                    font-size: 14px;
                    background-image: url("images/orange_button.jpg");
                    background-repeat: no-repeat;
                    background-position: center;
                    border: none;
                }
                QPushButton#scalingButtons:hover {
                    background-color: darkorange;
                    border: 2px solid white;
                    padding: 3px 7px;
                }
            """)

        clicked_button.setStyleSheet(button.styleSheet() + """
        QPushButton#scalingButtons {
            background-color: #a84300;
            border: 3px double white;
            padding: 2px 6px;
        }
    """)

