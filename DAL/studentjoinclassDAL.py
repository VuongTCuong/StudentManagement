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
    
    def get_by_lop(self,mamolop):
        try:
            query = '''select * from Molop where mamolop=?'''
                  
            self.cursor.execute(query,(mamolop,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchone()
    def get_class_joined(self,masv):
        try:
            query = '''select ml.mamolop,masv,mamon,hocki,namhoc,giangvien,siso,trangthai 
                       from Sinhvienthamgialop sv,Molop ml 
                       where sv.mamolop = ml.mamolop
                         and sv.masv = ?'''
                  
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
    def get_all_soluongsv(self):
        try:
            query = ''' select R1.mamolop,R1.mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai,soluongsv
                        from (select molop.mamolop,mamon,hocki,namhoc,giangvien,siso,trangthai,count(masv) as soluongsv
                                from molop LEFT OUTER JOIN sinhvienthamgialop sv on molop.mamolop=sv.mamolop
                            group by molop.mamolop) R1, Monhoc
                        where R1.mamon = Monhoc.mamonhoc'''
            
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not count {e}")
        return self.cursor.fetchall()
    
    def get_all_soluongsv_mo(self):
        try:
            query = ''' select R1.mamolop,R1.mamon,tenmonhoc,makhoa,sotc,hocki,namhoc,giangvien,siso,trangthai,soluongsv
                        from (select molop.mamolop,mamon,hocki,namhoc,giangvien,siso,trangthai,count(masv) as soluongsv
                                from molop LEFT OUTER JOIN sinhvienthamgialop sv on molop.mamolop=sv.mamolop
                            group by molop.mamolop) R1, Monhoc
                        where R1.mamon = Monhoc.mamonhoc and trangthai="Mở"'''
            
            self.cursor.execute(query)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not count {e}")
        return self.cursor.fetchall()
    
