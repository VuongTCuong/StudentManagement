from DAL import studentjoinclassDAL
import regex as re
class studentjoinclassBUS:
    def __init__(self):
        self.studentjoinclassDAL = studentjoinclassDAL.studentjoinclassDAL()
    
    def get_all_class_joined(self,masv):
        result = self.studentjoinclassDAL.get_class_joined(masv)   
        return [class_joined[0] for class_joined in result] 
    
    def get_all_subject_joined(self,masv):
        result = self.studentjoinclassDAL.get_class_joined(masv)   
        return [class_joined[2] for class_joined in result] 
    
    def get_hocki_namhoc_joined(self,masv):
        result = self.studentjoinclassDAL.get_class_joined(masv) 
        hocki_namhoc = [(i[3],i[4]) for i in result]
        num_hocki_namhoc = []  
        if result:
            for i in hocki_namhoc:
                num_hocki = int(re.findall(r'\d+',i[0])[0])
                num_namhoc = list(map(int,re.findall(r'\d+',i[1])))
                temp_tuple = (num_hocki,num_namhoc[0],num_namhoc[1])
                if  temp_tuple not in num_hocki_namhoc:
                    num_hocki_namhoc+=[temp_tuple]

        num_hocki_namhoc.sort(key=lambda x: (x[1],x[0]),reverse=True)
        return num_hocki_namhoc
    def get_all_soluongsv(self):
        return self.studentjoinclassDAL.get_all_soluongsv()
    
    def get_all_soluongsv_mo(self):
        return self.studentjoinclassDAL.get_all_soluongsv_mo()
    def get_mamon_by_lop(self,mamolop):
        return self.studentjoinclassDAL.get_by_lop(mamolop)
    def add_student(self,mamolop,masv):
        return self.studentjoinclassDAL.add_student(mamolop,masv)
    
    def delete_student(self,mamolop,masv):
        return self.studentjoinclassDAL.delete_student(mamolop,masv)