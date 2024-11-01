from DAL import classDAL

class classBUS:
    def __init__(self):
        self.classDAL = classDAL.classDAL()

    def get_all_class(self):
        return self.classDAL.get_all_class()
