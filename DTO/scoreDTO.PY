class ScoreDTO:
    _next_id = 1  # Class variable to keep track of the next available ID
    
    def __init__(self, masv, mamonhoc, diem):
        self._id = ScoreDTO._next_id
        ScoreDTO._next_id += 1
        self.masv = masv
        self.mamonhoc = mamonhoc
        self.diem = diem
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
