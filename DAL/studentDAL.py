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
                    makhoa TEXT NOT NULL,
                    tenlop TEXT,
                    FOREIGN KEY(tenlop) REFERENCES Lop(tenlop)
                    FOREIGN KEY(makhoa) REFERENCES Khoa(makhoa)
                )                                 
            ''')
            print('Created Database.')
        except sqlite3.Error as e:
            print(f"Error: Can not create table {e}")
    
    def add_student(self,masv,tensv,namsinh,gioitinh,email,makhoa,tenlop):
        try:
            self.cursor.execute('''
                INSERT INTO SinhVien (masv, tensv, namsinh, gioitinh, email, makhoa, tenlop)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (masv, tensv, namsinh, gioitinh, email, makhoa, tenlop))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(e)
        return False

    def get_one_student(self,masv):
        try:   
            query = 'select * from Sinhvien where masv='+masv
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        return self.cursor.fetchone()
    def get_all_student(self):
        try:
            self.cursor.execute('select * from Sinhvien')
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        return self.cursor.fetchall()

    def is_exist_student(self,masv):
        try:
            self.cursor.execute('select * from SinhVien where masv='+masv)
            self.conn.commit()
            if self.cursor.fetchone()!=None:
                return True
        except sqlite3.Error as e:
            print(e)
        return False
    def update_student(self,masv,tensv,namsinh,gioitinh,email,makhoa,tenlop):
        if self.is_exist_student(masv):
                try:
                    self.cursor.execute('''
                        UPDATE SinhVien 
                        SET tensv = ?, namsinh = ?, gioitinh = ?, email = ?, makhoa = ?, tenlop = ?
                        WHERE masv = ?
                    ''', (tensv, namsinh, gioitinh, email, makhoa, tenlop, masv))
                    self.conn.commit()
                    return True
                except sqlite3.Error as e:
                    print(e)
        return False

    def delete_student(self,masv):
        if self.is_exist_student(masv):
            try:
                self.cursor.execute('''
                    DELETE FROM SinhVien
                    WHERE masv = ?
                ''', (masv,))
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


    def filterStudent(self,makhoa,tenlop):
        query = 'select * from SinhVien'
        if makhoa!='' and tenlop=='':
            query+= " where makhoa='{0}'".format(makhoa)

        if makhoa=='' and tenlop!='':
            query+= " where tenlop='{0}'".format(tenlop)

        if makhoa!='' and tenlop!='':
            query+= " where makhoa='{0}' and tenlop='{1}'".format(makhoa,tenlop)
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(e)
        return self.cursor.fetchall()
