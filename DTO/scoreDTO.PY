class scoreDTO:
    def __init__(self,mamonhoc,masinhvien,diemgk,diemthi):
        self.mamonhoc = mamonhoc
        self.masinhvien = masinhvien
        self.diemgk = diemgk
        self.diemthi= diemthi
    def __str__(self):
        return f"Masv: {self.masinhvien}, Mamonhoc: {self.mamonhoc}, DiemGK: {self.diemgk}, Diemthi: {self.diemthi} "
    
