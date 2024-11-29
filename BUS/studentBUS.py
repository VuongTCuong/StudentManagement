from DAL import studentDAL
import pandas as pd

class studentBUS:
    def __init__(self):
        self.studentDAL = studentDAL.studentDAL()

    def add_student(self,student):
        masv = student.masv
        tensv = student.tensv
        namsinh = student.namsinh
        gioitinh = student.gioitinh
        email = student.email
        makhoa = student.makhoa
        malop = student.malop
        return self.studentDAL.add_student(masv,tensv,namsinh,gioitinh,email,makhoa,malop)
    
    def get_one_student(self,masv):
        return self.studentDAL.get_one_student(masv)

    def get_all_student(self):
        return self.studentDAL.get_all_student()
    
    def update_student(self,student):
        masv = student.masv
        tensv = student.tensv
        namsinh = student.namsinh
        gioitinh = student.gioitinh
        email = student.email
        makhoa = student.makhoa
        malop = student.malop
        return self.studentDAL.update_student(masv,tensv,namsinh,gioitinh,email,makhoa,malop)
    
    def delete_student(self,masv):
        return self.studentDAL.delete_student(masv)
    
    def import_csv(self,file_direct):
        data = pd.read_csv(file_direct)
        data_np_ar = data.to_numpy()
        for data in data_np_ar:
            data_str = list(map(str,data))
            print(data_str)
            self.studentDAL.add_student(data_str[0],data_str[1],data_str[2],data_str[3],data_str[4],data_str[5],data_str[6])

    def filterStudent(self,makhoa,tenlop):
        if makhoa =='Khoa':
            makhoa = ''
        if tenlop =='Lớp':
            tenlop = ''
        return self.studentDAL.filterStudent(makhoa,tenlop)