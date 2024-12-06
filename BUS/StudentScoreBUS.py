from DAL import StudentScoreDAL
class StudentScoreBUS:
    def __init__(self):
        self.studentscoreDAL = StudentScoreDAL.StudentScoreDAL()

    def get_score_info(self,masv,hocki,namhoc):
        return self.studentscoreDAL.get_score_info(masv,hocki,namhoc)