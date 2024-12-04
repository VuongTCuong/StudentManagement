import sqlite3

class studentjoinclassDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")
        
    def get_all(self):
        try:
            query = '''select * from Sinhvienthamgialop'''
                  
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()
    
    def get_class_joined(self,masv):
        try:
            query = '''select * from Sinhvienthamgialop where masv=?'''
                  
            self.cursor.execute(query,(masv,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()
    

    def add_student(self,mamolop,masv):
        try:
            query = '''insert into Sinhvienthamgialop(mamolop,masv) values(?,?)'''
            
            self.cursor.execute(query,(mamolop,masv))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()

    def delete_student(self,mamolop,masv):
        try:
            query = '''delete from Sinhvienthamgialop where mamolop=? and masv=?'''
            
            self.cursor.execute(query,(mamolop,masv))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return False
    