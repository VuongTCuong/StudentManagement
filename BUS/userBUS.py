from DTO import userDTO
from DAL import userDAL

class userBUS:
    def __init__(self) -> None:
        self.userDAL = userDAL.userDAL()

    def login(self, userDTO):
        #call DAL method to check login
        print('calling login bus....')
        return self.userDAL.check_user(userDTO.username, userDTO.password)
    
    def register(self, user, email, fullname):
        #call DAL method to check if email exists
        if self.userDAL.existed_email(email):
            raise ValueError("Email is existed in database.") #if existed    
        else:
            self.userDAL.add_user(user.username, fullname, user.password, email) 


    def update_pwd(self, email, new_pwd):
        return self.userDAL.update_pwd(email, new_pwd)

    
    


