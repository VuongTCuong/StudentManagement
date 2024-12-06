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