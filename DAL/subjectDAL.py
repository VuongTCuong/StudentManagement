import sqlite3
class subjectDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")

    def create_subject_table(self):
        try:
            self.cursor.execute('''
                create table if not exists MonHoc(
                    mamon TEXT PRIMARY KEY,
                    tenmon TEXT NOT NULL,
                    makhoa TEXT NOT NULL,
                    sotc INTEGER,
                    FOREIGN KEY(makhoa) REFERENCES Khoa(makhoa)
                )                                 
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")   
    
    def add_subject(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Cannot add subject - {e}")
            return False
    
    def update_subject(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Cannot update subject - {e}")
            return False
    
    def delete_subject(self, query, params):
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not delete subject {e}") 
    
    def get_one_subject(self,mamon):
        try:
            query = "select * from monhoc where mamonhoc='{0}'".format(mamon)
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error: Can not get all subjects {e}")

    def get_all_subjects(self):
        try:
            self.cursor.execute('''
                SELECT * FROM MonHoc
            ''')
            return self.cursor.fetchall()   
        except sqlite3.Error as e:
            print(f"Error: Can not get all subjects {e}")
    
    def get_subject_by_id(self,mamonhoc):
        try:
            self.cursor.execute('''
                SELECT * FROM MonHoc WHERE mamonhoc = ?
            ''', (mamonhoc,))
            return self.cursor.fetchone()   
        except sqlite3.Error as e:
            print(f"Error: Can not get subject by id {e}")
    
    def get_subject_by_department_id(self,makhoa):
        try:
            self.cursor.execute('''
                SELECT * FROM MonHoc WHERE makhoa = ?
            ''', (makhoa,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error: Can not get subject by department id {e}")
    
    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")   
    