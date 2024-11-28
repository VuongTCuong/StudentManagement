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
                    makhoa TEXT,
                    FOREIGN KEY(makhoa) REFERENCES Khoa(makhoa)
                );
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")

    def add_class(self, malop, tenlop, makhoa):
        try:
             self.cursor.execute('''
                                 INSERT INTO Lop (malop,tenlop,makhoa)
                                 VALUES (?, ?, ?)
                                 ''', (malop, tenlop, makhoa))
             self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: Mã Lớp already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error: Can not Add Lớp {e}")
            return False
        return True
    def get_class_by_depart(self,makhoa):
        try:
            query = "select * from Lop where makhoa ='{0}'".format(makhoa)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        result = self.cursor.fetchall()
        return result
    
    def get_one_class(self,malop):
        try:
            query = "select * from Lop where malop ={0}".format(malop)
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        result = self.cursor.fetchone()
        return result
    
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
    
    def update_class(self, malop, tenlop, makhoa):
        try:
            self.cursor.execute('''
                UPDATE Lop 
                SET tenlop = ?, makhoa = ?
                WHERE malop = ?
            ''', (tenlop, makhoa, malop))
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: Class name already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error: Cannot update class - {e}")
            return False
        return True
    
    def delete_class(self, malop):
        if self.is_exist_class(malop):
            try:
                self.cursor.execute('''
                    DELETE FROM Lop
                    WHERE malop = ?
                ''', (malop,))
                self.conn.commit()
                return True
            except sqlite3.Error as e:
                print(f"Error: Cannot delete class - {e}")
                return False
        return False
    
    def is_exist_class(self, malop):
        try:
            self.cursor.execute('SELECT * FROM Lop WHERE malop = ?', (malop,))
            self.conn.commit()
            if self.cursor.fetchone() is not None:
                return True
        except sqlite3.Error as e:
            print(f"Error: {e}")
        return False
    
    def get_class_by_id(self, malop):
        try:
            self.cursor.execute('SELECT * FROM Lop WHERE malop = ?', (malop,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        return self.cursor.fetchone()

