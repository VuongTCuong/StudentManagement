import sqlite3
class departmentDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")

    def create_department_table(self): 
        try:      
            self.cursor.execute('''
                create table if not exists Khoa(
                    makhoa INTEGER PRIMARY KEY,
                    tenkhoa TEXT UNIQUE
                )                                 
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")
    
    def add_department(self, makhoa, tenkhoa):
        try:
             self.cursor.execute('''
                                 INSERT INTO Khoa (makhoa, tenkhoa)
                                 VALUES (?, ?)
                                 ''', (makhoa, tenkhoa))
             self.conn.commit()
        except sqlite3.IntegrityError as e:
            print(f"Error: Mã Khoa already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error: Can not Add Khoa {e}")
            return False
        return True

    def get_all_department(self):
        try:
            self.cursor.execute('SELECT * FROM Khoa')
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        result = self.cursor.fetchall()
        return result
    
    def update_department(self, department):
        try:
            cursor = self.conn.cursor()
            
            sql = """
                UPDATE Department 
                SET TenKhoa = %s 
                WHERE MaKhoa = %s
            """
            cursor.execute(sql, (department.tenkhoa, department.makhoa))
            self.conn.commit()
            
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in DepartmentDAO - update_department: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def delete_department(self, makhoa):
        try:
            cursor = self.conn.cursor()
            
            sql = "DELETE FROM Department WHERE MaKhoa = %s"
            cursor.execute(sql, (makhoa,))
            self.conn.commit()
            
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error in DepartmentDAO - delete_department: {str(e)}")
            return False
        finally:
            cursor.close()
    
    def check_department_in_classes(self, makhoa):
        try:
            cursor = self.conn.cursor()
            
            sql = "SELECT COUNT(*) FROM Class WHERE MaKhoa = %s"
            cursor.execute(sql, (makhoa,))
            count = cursor.fetchone()[0]
            
            return count
        except Exception as e:
            print(f"Error checking classes: {str(e)}")
            return 0
        finally:
            cursor.close() 

    def check_department_in_students(self, makhoa):
        try:
            cursor = self.conn.cursor()
            
            sql = "SELECT COUNT(*) FROM Student WHERE MaKhoa = %s"
            cursor.execute(sql, (makhoa,))
            count = cursor.fetchone()[0]
            
            return count
        except Exception as e:
            print(f"Error checking students: {str(e)}")
            return 0
        finally:
            cursor.close()

    
    def is_exist_department(self, makhoa):
        try:
            self.cursor.execute('SELECT * FROM Khoa WHERE makhoa = ?', (makhoa,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")

    def close(self):
        try: 
            self.conn.close()
        except sqlite3.Error as e:
            print(f"Error disconnecting database {e}")
    
    def get_department_by_id(self, makhoa):
        try:
            self.cursor.execute('SELECT * FROM Khoa WHERE makhoa = ?', (makhoa,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        result = self.cursor.fetchone()
        return result
    

