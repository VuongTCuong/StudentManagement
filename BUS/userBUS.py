from DTO import userDTO
from DAL import userDAL
userDTO = userDTO.userDTO

class userBUS:
    def __init__(self) -> None:
        self.userDAL = userDAL.userDAL()

    def login(self, userDTO):
        #call DAL method to check login
        return self.userDAL.check_user(userDTO.username, userDTO.password)
    


