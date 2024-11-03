from DAL import classDAL

class classBUS:
    def __init__(self):
        self.classDAL = classDAL.classDAL()
    
    def add_class(self, malop, tenlop, makhoa):
        # strip() removes leading and trailing whitespace from strings
        malop = malop.strip()
        tenlop = tenlop.strip()
        makhoa = makhoa.strip()
        return self.classDAL.add_class(malop, tenlop, makhoa)

    def get_all_class(self):
        return self.classDAL.get_all_class()
    
    def update_class(self, malop, tenlop, makhoa):
        malop = malop.strip()
        tenlop = tenlop.strip() 
        makhoa = makhoa.strip()
        return self.classDAL.update_class(malop, tenlop, makhoa)

    def delete_class(self, malop):
        malop = malop.strip()
        return self.classDAL.delete_class(malop)

    def get_class_by_id(self, malop):   
        malop = malop.strip()
        return self.classDAL.get_class_by_id(malop) 
    
