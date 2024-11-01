import sqlite3
class studentDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")
    def create_student_table(self): 
        try:      
            self.cursor.execute('''
                create table if not exists SinhVien(
                    masv INTEGER PRIMARY KEY,
                    tensv TEXT NOT NULL,
                    namsinh INTEGER NOT NULL,
                    gioitinh TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    malop INTEGER,
                    FOREIGN KEY(malop) REFERENCES Lop(malop)
                )                                 
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")
    
    def add_student(self,masv,tensv,namsinh,gioitinh,email,malop):
        try:
            self.cursor.execute('''
                INSERT INTO SinhVien (masv, tensv, namsinh, gioitinh, email, malop)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (masv, tensv, namsinh, gioitinh, email, malop))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
            
        return False
    def close(self):
        try: 
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error disconnecting database {e}")