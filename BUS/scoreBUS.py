from DAL.scoreDAL import scoreDAL
from DTO import scoreDTO
class scoreBUS:
    def __init__(self):
        self.score_dal = scoreDAL()
    
    def add_score(self,score):
        query = 'INSERT INTO Diem (mamonhoc,masinhvien,diem) VALUES (?,?,?)'
        params = (score.mamonhoc,score.masinhvien,score.diem)
        return self.score_dal.add_score(query,params)

    def update_score(self, score):
        query = 'UPDATE Diem SET diem=? WHERE mamonhoc=? AND masinhvien=?'
        params = (score.diem, score.mamonhoc, score.masinhvien)
        return self.score_dal.update_score(query, params)
    
    def delete_score(self,mamonhoc,masinhvien):
        query = 'DELETE FROM Diem WHERE mamonhoc=? AND masinhvien=?'
        params = (mamonhoc,masinhvien)
        return self.score_dal.delete_score(query,params)    

    def get_all_scores(self):
        return self.score_dal.get_all_scores()
    def get_score_by_student_id(self,masinhvien):
        return self.score_dal.get_score_by_student_id(masinhvien)
    
    def get_score_by_subject_id(self,mamonhoc):
        return self.score_dal.get_score_by_subject_id(mamonhoc) 
    
    def get_score_by_student_and_subject_id(self,masinhvien,mamonhoc):
        return self.score_dal.get_score_by_student_and_subject_id(masinhvien,mamonhoc)
    
    def close_connection(self):
        self.score_dal.close_connection()
    
    def check_subject_exists(self,mamonhoc):
        return self.score_dal.check_subject_exists(mamonhoc)
    
    def check_student_exists(self,masinhvien):
        return self.score_dal.check_student_exists(masinhvien)

