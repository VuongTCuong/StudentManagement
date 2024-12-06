from DAL import OpenClassDAL
class OpenClassBUS:
    def __init__(self):
        self.OpenClassDAL = OpenClassDAL.OpenClassDAL()

    def get_all(self):
        return self.OpenClassDAL.get_all()
    
    def get_all_mo(self):
        return self.OpenClassDAL.get_all_mo()
    
    def add_OpenClass(self,maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
        return self.OpenClassDAL.add_OpenClass(maml,mamon,hocki,namhoc,giangvien,siso,trangthai)

    def update_OpenClass(self,maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
        return self.OpenClassDAL.update_OpenClass(maml,mamon,hocki,namhoc,giangvien,siso,trangthai)
    
    def delete_OpenClass(self,maml):
        return self.OpenClassDAL.delete_OpenClass(maml)
    
    def filter(self,khoa,hocki):
        if khoa=='Khoa':
            khoa=''
        if hocki=='Học kì':
            hocki=''
        return self.OpenClassDAL.filter(khoa,hocki)
    
    def get_sv_by_malop(self,maml):
        return self.OpenClassDAL.get_sv_by_malop(maml)