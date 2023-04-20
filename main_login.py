# Cap Stone COMPETENCY TRACKING TOOL
import bcrypt
import manager_functions
import user_functions
from competency_tracker_database import cursor



def login(self):
    email = input("Enter email: ")
    password = input("Enter password: ")
    hashed_password = login.hashed(self, self.password)
    select_sql = "SELECT password, user_type, user_id FROM Users WHERE email = ? "
    values = (self.email)
    cursor.execute(select_sql, values)
    row = cursor.fetchone()
    if hashed_password != row[0]:
        return print("Login Failed")
    if row[1] == "manager":
        manager_functions.show_manager_menu()
    else:
        user_functions.show_user_menu(row[2])

login()

def hashed(password):
    salt = bcrypt.gensalt()
    bytes = password.encode('utf-8')
    hashed_pass = bcrypt.hashpw(bytes, salt)
    return hashed_pass
