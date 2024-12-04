import sqlite3

class OpenClassDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")
    def get_all(self):
        try:
            query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                    from MoLop,Monhoc 
                    where molop.mamon=Monhoc.mamonhoc'''
                  
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()
    
    def get_all_mo(self):
        try:
            query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                    from MoLop,Monhoc 
                    where molop.mamon=Monhoc.mamonhoc and trangthai="Mở"'''
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()
    
    def add_OpenClass(self,maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
        try:
            query = 'insert into molop (mamolop,mamon,hocki,namhoc,giangvien,siso,trangthai) values (?,?,?,?,?,?,?)'
                  
            self.cursor.execute(query,(maml,mamon,hocki,namhoc,giangvien,siso,trangthai))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not insert {e}")
        return False
    
    def update_OpenClass(self,maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
        try:
            query = '''update molop 
                       set mamon=? ,hocki=? ,namhoc=?,giangvien=?,siso=?,trangthai=?
                       where mamolop=?'''
                  
            self.cursor.execute(query,(mamon,hocki,namhoc,giangvien,siso,trangthai,maml))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error: Can not update {e}")
        return False
    
    def search_by_maml(self,maml):
        try:
            query = 'select * from molop where mamolop=?'
            self.cursor.execute(query,(maml,))
            self.conn.commit()
            return self.cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Error: Can not find: {e}")
    def delete_OpenClass(self,maml):
        if self.search_by_maml(maml):
            query = '''delete from molop where mamolop=?'''
                  
            self.cursor.execute(query,(maml,))
            self.conn.commit()
            return True
        return False
    
    def filter(self,khoa,hocki):
        if khoa=='':
            if hocki=='':
                query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                        from MoLop,Monhoc 
                        where molop.mamon=Monhoc.mamonhoc'''
            else:
                query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                        from MoLop,Monhoc 
                        where molop.mamon=Monhoc.mamonhoc and hocki="{0}"'''.format(hocki)
        else:
            if hocki=='':
                query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                        from MoLop,Monhoc 
                        where molop.mamon=Monhoc.mamonhoc and makhoa="{0}"'''.format(khoa)
            else:
                query = '''select mamolop,mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai
                        from MoLop,Monhoc 
                        where molop.mamon=Monhoc.mamonhoc and makhoa="{0}" and hocki="{1}"'''.format(khoa,hocki)
   
        try:  
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return []
