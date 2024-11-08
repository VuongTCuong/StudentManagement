import customtkinter as ctk
from tkinter import messagebox

#for importing DTO and BUS module
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DTO import userDTO
from BUS import userBUS

import re #library for using re.match() 
import random #random function
from email.mime.text import MIMEText #Email handling
import smtplib #Email handling

class Forgot_pwdGUI:
    def __init__(self):
        self.userBUS = userBUS.userBUS()

        # Main login window
        self.root = ctk.CTk()
        self.root.title("Student Management System - Quên mật khẩu")
        self.root.geometry("450x150")
        self.root.resizable(False, False)

        # Set appearance mode and default theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Adding widgets and create a login screen
        self.create_forgot_pwd_screen()

        #run
        self.root.mainloop()
    
    def create_forgot_pwd_screen(self):
        #create forgot_frame to contains components
        forgot_frame = ctk.CTkFrame(self.root)
        forgot_frame.pack(pady=20)

        #Create email label
        # email_label = ctk.CTkLabel(register_frame, text="Email:",anchor="w")
        email_label = ctk.CTkLabel(
            forgot_frame,
            text="Nhập email của bạn:",
            anchor="w",                 
            text_color="#333333",        
            font=("Arial", 14, "bold")   
        )
        email_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        #Create email entry
        self.email_entry = ctk.CTkEntry(
            forgot_frame,
            placeholder_text="Nhập Email",  
            width=200,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.email_entry.grid(row=0, column=1, columnspan=2, pady=12, padx=10)
        # Create send OTPs button
        self.sendOTP_button = ctk.CTkButton(forgot_frame, text="Gửi mã xác thực", command=self.on_send_otp)
        self.sendOTP_button.grid(row=1, column=0, columnspan=3, pady=12)


    def email_is_valid(self, email):
        # Define the regular expression for validating an email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Check if the email matches the pattern
        return re.match(email_regex, email) is not None #return True if matchs, False if not match

    def on_send_otp(self):
        user_email = self.email_entry.get()
        if not user_email:
            messagebox.showerror("Lỗi", "Hãy nhập email của bạn.")
        else:
            if self.email_is_valid(user_email):
                #check if email is in database or not
                if not self.userBUS.userDAL.existed_email(user_email):
                    messagebox.showerror("Lỗi", "Email không tồn tại trong database.")
                else:
                    #generate 4 OTPs 
                    self.otp_code = random.randint(1000,9999)
                    #send code via email
                    if self.send_otp_codes(user_email):
                        messagebox.showinfo("Thành công", "Mã xác thực đã được gửi đến email của bạn.")
                        self.sendOTP_button.configure(state = "disabled")
                        self.create_otp_window(user_email)
                    else:
                        messagebox.showerror("Lỗi", "Không thể gửi mã xác thực.")
            else:
                messagebox.showerror("Lỗi", "Email không hợp lệ.")

    def send_otp_codes(self, reciever_email):
        try: 
            subject = f"Bạn đang đổi mật khẩu tài khoản Student Management."
            body = f"Mã xác thực của bạn là: {self.otp_code} . Không chia sẽ mã này với ai để bảo mật."

            #config email
            smtp_server = 'smtp.gmail.com' #This specifies the SMTP (Simple Mail Transfer Protocol) server for Gmail.
            smtp_port = 587 #is commonly used for TLS (Transport Layer Security) encryption with SMTP.
            sender_email = 'thuando.contact@gmail.com'
            sender_pwd = 'nodc miwi odav tepq'

            #create email
            msg = MIMEText(body)
            msg["Subject"] = subject
            msg["From"] = sender_email
            msg["To"] = reciever_email

            #send mail via SMTP
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # Start TLS encryption
                server.login(sender_email, sender_pwd)
                server.sendmail(sender_email,reciever_email, msg.as_string())
            return True
        except Exception as e:
            print("Error when sending email", e)
            return False
        
    
    def create_otp_window(self, email):
        #create OTP window
        OTP_window = ctk.CTkToplevel(self.root)
        OTP_window.title("Student Management System - Xác thực đổi mật khẩu")
        OTP_window.geometry("500x170")
        OTP_window.resizable(False,False)

        #Title Label
        title_lbl = ctk.CTkLabel(OTP_window, text="Nhập mã xác thực đã được gửi qua email", font=("Arial", 24, "bold"), text_color="dark blue")
        title_lbl.pack(pady = 15)

        #####   Entry for OTP  ######
        otp_entry = ctk.CTkEntry(
            OTP_window,
            placeholder_text="nhập mã xác thực",  
            width=200,                    
            height=35,                    
            border_width=1,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        otp_entry.pack(pady = 10)

        def verify_otp():
            entered_code = otp_entry.get()
            if entered_code != str(self.otp_code):
                messagebox.showerror("Lỗi", "Mã xác thực không đúng")
            else:
                OTP_window.destroy()
                self.create_new_pwd_window(email)
                
        submit_button = ctk.CTkButton(OTP_window, text="Xác thực", command=verify_otp)
        submit_button.pack(pady = 10)


    def create_new_pwd_window(self, email):
        #create OTP window
        newpwd_window = ctk.CTkToplevel(self.root)
        newpwd_window.title("Student Management System - Mật Khẩu Mới")
        newpwd_window.geometry("500x370")
        newpwd_window.resizable(False, False)

        #Title Label
        title_lbl = ctk.CTkLabel(newpwd_window, text="Đổi mật khẩu", font=("Arial", 24, "bold"), text_color="dark blue")
        title_lbl.pack(pady = 15)

        #Create new password label
        newpwd_label = ctk.CTkLabel(
            newpwd_window,
            text="Mật khẩu mới:",
            anchor="w",                 
            text_color="#333333",        
            font=("Arial", 14, "bold")   
        )
        newpwd_label.pack(pady = 5)

        #Create new password entry
        newpwd_entry = ctk.CTkEntry(
            newpwd_window,
            placeholder_text="Nhập mật khẩu mới", show = "*",
            width=200,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        newpwd_entry.pack(pady = 5)

        #Create new conf-password label
        confpwd_label = ctk.CTkLabel(
            newpwd_window,
            text="Xác nhận mật khẩu: ",
            anchor="w",                 
            text_color="#333333",        
            font=("Arial", 14, "bold")   
        )
        confpwd_label.pack(pady = 5)

        #Create new conf-password entry
        confpwd_entry = ctk.CTkEntry(
            newpwd_window,
            placeholder_text="Xác nhận mật khẩu",  show = "*",
            width=200,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        confpwd_entry.pack(pady = 5)

        def update_pwd():
            new_pwd = newpwd_entry.get()
            conf_pwd = confpwd_entry.get()
            if new_pwd != conf_pwd:
                messagebox.showerror("Lỗi", "Mật khẩu không khớp.")
            else:
                #Update password in database
                if self.userBUS.update_pwd(email, new_pwd):
                    messagebox.showinfo("Thành công", "Mật khẩu đã được đổi.")
                    # newpwd_window.destroy()
                    self.root.destroy()
                else:
                    messagebox.showerror("Lỗi", "Không thể đổi mật khẩu")
        submit_button = ctk.CTkButton(newpwd_window, text="Đổi mật khẩu", command=update_pwd)
        submit_button.pack(pady = 10)


if __name__ == "__main__":
    Forgot_pwdGUI()



