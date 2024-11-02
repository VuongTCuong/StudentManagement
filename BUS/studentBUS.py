from DAL import studentDAL

class studentBUS:
    def __init__(self):
        self.studentDAL = studentDAL.studentDAL()

    def add_student(self,student):
        masv = student.masv
        tensv = student.tensv
        namsinh = student.namsinh
        gioitinh = student.gioitinh
        email = student.email
        malop = student.malop
        return self.studentDAL.add_student(masv,tensv,namsinh,gioitinh,email,malop)
    
    def get_all_student(self):
        return self.studentDAL.get_all_student()
    
    def update_student(self,student):
        masv = student.masv
        tensv = student.tensv
        namsinh = student.namsinh
        gioitinh = student.gioitinh
        email = student.email
        malop = student.malop
        return self.studentDAL.update_student(masv,tensv,namsinh,gioitinh,email,malop)
    
    def delete_student(self,masv):
        return self.studentDAL.delete_student(masv)
    