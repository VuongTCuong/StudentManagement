from DTO import userDTO
from DAL import userDAL
userDTO = userDTO.userDTO

class userBUS:
    def __init__(self) -> None:
        self.userDAL = userDAL.userDAL()

    def login(self, userDTO):
        #call DAL method to check login
        return self.userDAL.check_user(userDTO.username, userDTO.password)
    
    def register(self, user, email, fullname):
        #call DAL method to check if email exists
        if self.userDAL.existed_email(email):
            raise ValueError("Email is existed in database.") #if existed    
        else:
            self.userDAL.add_user(user.username, fullname, user.password, email) 

    
    


