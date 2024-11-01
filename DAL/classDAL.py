import sqlite3
class classDAL: 
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")

    def create_class_table(self): 
        try:      
            self.cursor.execute('''
                create table if not exists Lop(
                    malop INTEGER PRIMARY KEY,
                    tenlop TEXT UNIQUE,
                    makhoa INTEGER,
                    FOREIGN KEY(makhoa) REFERENCES Khoa(makhoa)
                );
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")

    def add_class(self, malop, tenlop, makhoa):
        try:
             self.cursor.execute('''
                                 INSERT INTO Lop (malop,telop,makhoa)
                                 VALUES (?, ?, ?, ?)
                                 ''', (malop, tenlop, makhoa))
             self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: Mã Lớp already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error: Can not Add Lớp {e}")
            return False
        return True
    
    def get_all_class(self):
        try:
            self.cursor.execute('SELECT * FROM Lop')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        result = self.cursor.fetchall()
        return result
    def close(self):
        try: 
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error disconnecting database {e}")

