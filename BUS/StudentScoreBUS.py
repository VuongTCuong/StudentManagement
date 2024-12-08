from DAL import StudentScoreDAL
class StudentScoreBUS:
    def __init__(self):
        self.studentscoreDAL = StudentScoreDAL.StudentScoreDAL()

    def get_score_info(self,masv,hocki,namhoc):
        return self.studentscoreDAL.get_score_info(masv,hocki,namhoc)
    
 
    def get_whole_score(self,masv):
        return self.studentscoreDAL.get_whole_score(masv)