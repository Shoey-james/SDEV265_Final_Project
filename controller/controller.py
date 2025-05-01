from model.LoginLogic import LoginLogic, CreateAccount
from view.HomePage import HomePage, SearchPopupWindow
from view.RecipesWIndow import RecipesWindow
from view.LoginWindow import LoginWindow
from view.CreateAccountDisplay import CreateAccountDisplay
from model.PortionScaler import PortionScaler
from model.Units import Units
import sqlite3
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt

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

    def scaling_pressed(self, button, scaling_buttons, curr_rec):
        button_id = scaling_buttons.id(button)
        print(f"Button Pressed:{button.text()}, ID: {button_id}")
        # First, reset all scaling buttons
        for btn in scaling_buttons.buttons():
            btn.setStyleSheet("""
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

        button.setStyleSheet(button.styleSheet() + """
        QPushButton#scalingButtons {
            background-color: #a84300;
            border: 3px double white;
            padding: 2px 6px;
        }
    """)
        self.scale_rec_ingredients(curr_rec, button_id)
    
    def scale_rec_ingredients(self, curr_rec, button_id):
        print("Scaling ingredients initiated")
        conn = sqlite3.connect('db_tables/tables.db')
        cursor = conn.cursor()
        cursor.execute("SELECT ing_id, ing_name, ing_quant, ing_unit FROM ingredients_table WHERE rec_id = ?", (curr_rec,))
        rows = cursor.fetchall()
        conn.close()

        for ing_id, ing_name, ing_quant, ing_unit in rows:
            try:
                dec_original_value = Units.to_decimal(ing_quant)
            except:
                print(f"Could not parse: {ing_quant}")
                continue
            scaler = PortionScaler(
                original_unit = ing_unit,
                original_value = dec_original_value,
                scale_factor = button_id
            )
            scaled_value = scaler.scale_ingredient()
            print(f"Scaled value (after scale_ingredient): {scaled_value}")
            scaled_value, original_unit, equiv_value, equiv_unit = scaler.get_equivalents()
            
            fraction_scaled_value = Units.to_fraction(scaled_value)
            if equiv_value:
                fraction_equiv_value = Units.to_fraction(equiv_value)
                scaled_text = f"{fraction_scaled_value} {original_unit} (or {fraction_equiv_value} {equiv_unit})"
            else:
                scaled_text = f"{fraction_scaled_value} {original_unit}"

            scaled_text += f" {ing_name}"
            print("Suggested equivalent:", scaled_text)
            if scaled_value is None:
                continue
            if hasattr(self, "full_recipe_view"):
                label = self.full_recipe_view.ingredient_labels.get(ing_id)
                if label:
                    label.setText(scaled_text)
    
    def favbtn_pressed(self, rec_id):
        print("fav button pressed")
        is_favorited = self.quick_select_favorite(rec_id)

        if is_favorited:       # Unfavorite --> delete from favorites_table
            self.delete_favorite(rec_id)

        elif is_favorited == None:       # Favorite --> insert into favorites_table
            self.insert_favorite(rec_id)
            
    
    def insert_favorite(self, rec_id):
        print("insert favorite function accessed")
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO favorites_table (username, rec_id) VALUES (?, ?);",
                (self.username, rec_id,)
            )
            conn.commit()
            cursor.close()
        except sqlite3.IntegrityError as e:
            print(f"Insert failed: {e}")  # For example, if the favorite already exists
        
        
        self.home.update_home()
        self.full_recipe_view.update_rec_window()

    def delete_favorite(self, rec_id):
        print(" delete favorite function accessed")
        try:
            conn = sqlite3.connect('db_tables/tables.db')
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM favorites_table WHERE username = ? AND rec_id = ?;",
                (self.username, rec_id,)
            )
            conn.commit()
            cursor.close()
        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")
            return None

        
        self.home.update_home()
        self.full_recipe_view.update_rec_window()



    def quick_select_favorite(self, rec_id):
        print("Quick_select_favorites: Current User: ", self.username)
        print("Quick_select_favorites: rec_id: ", rec_id)
        conn = sqlite3.connect('db_tables/tables.db')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT 1 FROM favorites_table WHERE username = ? AND rec_id = ?",
            (self.username, rec_id)
        )
        result = cursor.fetchone()
        conn.close()
        return True if result else None

