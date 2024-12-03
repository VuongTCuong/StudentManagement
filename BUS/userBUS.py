from DTO import userDTO
from DAL import userDAL
from cryptography.fernet import Fernet
import os
class userBUS:
    def __init__(self) -> None:
        self.userDAL = userDAL.userDAL()

    def login(self, userDTO):
        #call DAL method to check login
        print('calling login bus....')


        #temp file for saving login account
        is_login_success = self.userDAL.check_user(userDTO.username, userDTO.password)

        f = Fernet(b'LkQhEOBncRePoyysixPYu-I2Q-uDd-UZH18e8M2_HJE=') #private key
        is_success,role = self.userDAL.check_user(userDTO.username, userDTO.password)
        if is_success:
            if not os.path.exists('user.txt'):
                user_file = open('user.txt','wb')
                user_file.write(f.encrypt(userDTO.username.encode()))
                user_file.write(b'\n')
                user_file.write(f.encrypt(role.encode()))

        return is_success,role
    
    def register(self, user, email, fullname):
        #call DAL method to check if email exists
        if self.userDAL.existed_email(email):
            raise ValueError("Email is existed in database.") #if existed    
        else:
            self.userDAL.add_user(user.username, fullname, user.password, email) 


    def update_pwd(self, email, new_pwd):
        return self.userDAL.update_pwd(email, new_pwd)

    def get_user_by_id(self,id):
        return self.userDAL.get_user_by_id(id)
    
    


