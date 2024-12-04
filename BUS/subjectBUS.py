from DAL import subjectDAL

class subjectBUS:
    def __init__(self):
        self.subjectDAL = subjectDAL.subjectDAL()
    
    def add_subject(self, mamonhoc, tenmonhoc, makhoa, sotinchi):
        try:
            query = """
                INSERT INTO MonHoc (mamonhoc, tenmonhoc, makhoa, sotc)
                VALUES (?, ?, ?, ?)
            """
            params = (mamonhoc, tenmonhoc, makhoa, sotinchi)
            return self.subjectDAL.add_subject(query, params)
        except Exception as e:
            print(f"Error in add_subject: {str(e)}")
            return False
    
    def get_one_subject(self,mamon):
        return self.subjectDAL.get_one_subject(mamon)

    def get_all_subjects(self):
        return self.subjectDAL.get_all_subjects()
    
    def get_subject_by_id(self, mamonhoc):
        return self.subjectDAL.get_subject_by_id(mamonhoc)
    
    def get_subject_by_department_id(self, makhoa):
        return self.subjectDAL.get_subject_by_department_id(makhoa)
    
    def update_subject(self, mamonhoc, tenmonhoc, makhoa, sotinchi):
        try:
            query = """
                UPDATE MonHoc 
                SET tenmonhoc = ?, makhoa = ?, sotc = ?
                WHERE mamonhoc = ?
            """
            params = (tenmonhoc, makhoa, sotinchi, mamonhoc)
            return self.subjectDAL.update_subject(query, params)
        except Exception as e:
            print(f"Error in update_subject: {str(e)}")
            return False
    
    def delete_subject(self, mamonhoc):
        try:
            query = "DELETE FROM MonHoc WHERE mamonhoc = ?"
            params = (mamonhoc,)
            return self.subjectDAL.delete_subject(query, params)
        except Exception as e:
            print(f"Error in delete_subject: {str(e)}")
            return False
    
    def close_connection(self):
        self.subjectDAL.close_connection()


