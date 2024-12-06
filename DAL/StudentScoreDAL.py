import sqlite3
class StudentScoreDAL:
    def __init__(self, path = 'student_management.db'):
        #connect to database SQLite
        try:
            self.conn = sqlite3.connect(path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: Can not connect to database {e}")

    def get_score_info(self,masv,hocki,namhoc):
        try:
            query = '''select mamon,tenmonhoc,sotc,diemgk,diemthi from(
                       select ml.mamon,masv,diemgk,diemthi,hocki,namhoc from diem d ,molop ml
                       where d.mamonhoc = ml.mamon
                       and d.masv=? and hocki=? and namhoc=?) R, Monhoc mh
                       where R.mamon = mh.mamonhoc'''
                  
            self.cursor.execute(query,(masv,hocki,namhoc))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()
    
    def get_whole_score(self,masv):
        try:
            query = ''' select diem.mamonhoc,sotc,(diemgk+diemthi)/2 as diemtk10,
                            case 
                                when (diemgk+diemthi)/2>=8.5 then 4
                                when (diemgk+diemthi)/2>=7.0 then 3
                                when (diemgk+diemthi)/2>=5.5 then 2
                                when (diemgk+diemthi)/2>=4.0 then 1
                                else 0
                            end as diemtk4
                        from Diem,Monhoc 
                        where diem.mamonhoc = monhoc.mamonhoc
                        and masv = ?'''
                  
            self.cursor.execute(query,(masv,))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error: Can not get {e}")
        return self.cursor.fetchall()