from DAL.scoreDAL import scoreDAL
from DTO import scoreDTO
class ScoreBUS:
    def __init__(self):
        self.score_dal = scoreDAL()
        # Initialize the next ID based on the highest existing ID
        scores = self.get_all_scores()  # Assuming you have a getAll method
        if scores:
            max_id = max(score.id for score in scores)
            scoreDTO._next_id = max_id + 1
        else:
            scoreDTO._next_id = 1
    
    def add_score(self,score):
        query = 'INSERT INTO Diem (masv,mamonhoc,diem) VALUES (?,?,?)'
        params = (score.masv,score.mamonhoc,score.diem)
        return self.score_dal.add_score(query,params)
    
    def update_score(self,score):
        query = 'UPDATE Diem SET masv=?,mamonhoc=?,diem=? WHERE id=?'
        params = (score.masv,score.mamonhoc,score.diem,score.id)
        return self.score_dal.update_score(query,params)
    
    def delete_score(self,id):
        query = 'DELETE FROM Diem WHERE id=?'
        params = (id,)
        return self.score_dal.delete_score(query,params)
    
    def get_all_scores(self):
        return self.score_dal.get_all_scores()
    
    def get_score_by_id(self,id):
        return self.score_dal.get_score_by_id(id)
    
    def get_score_by_student_id(self,masv):
        return self.score_dal.get_score_by_student_id(masv)
    
    def get_score_by_subject_id(self,mamonhoc):
        return self.score_dal.get_score_by_subject_id(mamonhoc) 
    
    def get_score_by_student_and_subject_id(self,masv,mamonhoc):
        return self.score_dal.get_score_by_student_and_subject_id(masv,mamonhoc)
    
    def close_connection(self):
        self.score_dal.close_connection()

