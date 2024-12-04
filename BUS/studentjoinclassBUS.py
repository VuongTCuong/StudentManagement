from DAL import studentjoinclassDAL

class studentjoinclassBUS:
    def __init__(self):
        self.studentjoinclassDAL = studentjoinclassDAL.studentjoinclassDAL()
    
    def get_all_class_joined(self,masv):
        result = self.studentjoinclassDAL.get_class_joined(masv)   
        return [class_joined[0] for class_joined in result] 
    
    def add_student(self,mamolop,masv):
        return self.studentjoinclassDAL.add_student(mamolop,masv)
    
    def delete_student(self,mamolop,masv):
        return self.studentjoinclassDAL.delete_student(mamolop,masv)