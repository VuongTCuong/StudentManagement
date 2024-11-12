import sqlite3

class scoreDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")
        
    def add_score(self,query,params):
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not insert score {e}")
    
    def update_score(self,query,params):
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not update score {e}")  
    
    def delete_score(self,query,params):    
        try:
            self.cursor.execute(query,params)
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not delete score {e}")  
    
    def get_all_scores(self):
        try:
            self.cursor.execute('''SELECT * FROM Diem''')
            result = self.cursor.fetchall()
            return result if result else []
        except sqlite3.Error as e:
            print(f"Error: Can not get all scores {e}")
            return []
    
    
    def get_score_by_student_id(self,masv):
        try:
            self.cursor.execute('''SELECT * FROM Diem WHERE masinhvien = ?''', (masv,))
            result = self.cursor.fetchall()
            return result if result else []
        except sqlite3.Error as e:
            print(f"Error: Can not get score by student id {e}")
            return []
    
    def get_score_by_subject_id(self,mamonhoc):
        try:
            self.cursor.execute('''SELECT * FROM Diem WHERE mamonhoc = ?''', (mamonhoc,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error: Can not get score by subject id {e}") 
    
    def get_score_by_student_and_subject_id(self,masv,mamonhoc):
        try:
            self.cursor.execute('''SELECT * FROM Diem WHERE masinhvien = ? AND mamonhoc = ?''', (masv,mamonhoc))
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error: Can not get score by student and subject id {e}") 
    
    def close_connection(self):
        self.conn.close()
        
