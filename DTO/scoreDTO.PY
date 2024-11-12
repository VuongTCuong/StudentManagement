class scoreDTO:
    def __init__(self,mamonhoc,masinhvien,diem):
        self.mamonhoc = mamonhoc
        self.masinhvien = masinhvien
        self.diem = diem
    
    def __str__(self):
        return f"Masv: {self.masinhvien}, Mamonhoc: {self.mamonhoc}, Diem: {self.diem}"
    
