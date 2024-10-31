import sqlite3
import os

class userDAL: 
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")

    # Create users table
    def create_user_table(self): 
        try:      
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            ''')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")
    

    #add user to table return True if added successfully, return False if added unsucessfully
    def add_user(self, username, pwd, email):
        try:
             self.cursor.execute('''
                                 INSERT INTO users (username, password, email)
                                 VALUES (?, ?, ?)
                                 ''', (username, pwd, email))
             self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: Username already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error: Can not Add User {e}")
            return False
        return True

    #check username exist?
    def check_username(self, username):
        try:
            self.cursor.execute('''
                    SELECT * FROM users WHERE username = ?
                                ''', (username))
            user = self.cursor.fetchone()
            if len(user) == 0:
                return False
            else:
                return True
        except sqlite3.Error as e:
            print(e)

    #check user info in database
    #LOGIN VIA USERNAME
    def check_user(self, username, pwd):
        try:
            self.cursor.execute('''
                    SELECT * FROM users WHERE username = ? AND password = ?
                                ''', (username, pwd))
            user = self.cursor.fetchone()
            return user is not None #return True if exist user, False if not exist
        except sqlite3.Error as e:
            print(f"Error can not check user information: {e}")


    def existed_email(self, email):
        try:
            self.cursor.execute('''SELECT * FROM users WHERE email = ?''', (email,))
            user = self.cursor.fetchone()
            return user is not None #return True if exist, False if not exist
        except sqlite3.Error as e:
            print(f"Error can not check email information: {e}")


    #close connection
    def close(self):
        try: 
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error disconnecting database {e}")


    

        