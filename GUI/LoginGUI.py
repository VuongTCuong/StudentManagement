import customtkinter as ctk
from tkinter import messagebox, ttk, W
from PIL import Image, ImageTk #library Pillow for handling images


#for importing DTO and BUS module
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DTO import userDTO
from BUS import userBUS

#import GUIs
import RegisterGUI
import Changetab
import Forgort_pwdGUI

class LoginGUI:
    def __init__(self):
        self.userBUS = userBUS.userBUS()


        # Main login window
        self.root = ctk.CTk()
        self.root.protocol("WM_DELETE_WINDOW", self.root.quit())
        self.root.title("Student Management System - Đăng Nhập")
        self.root.geometry("600x270")
        self.root.resizable(False, False)

        # Set appearance mode and default theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Adding widgets and create a login screen
        self.create_login_screen()

        #run
        self.root.mainloop()
    
    def create_login_screen(self):
        #logo frame
        logo_frame = ctk.CTkFrame(self.root, fg_color="#ebebeb")
        logo_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        #load logo
        try: 
            logo = Image.open(os.path.join(os.path.dirname(__file__), "assets", "logo.png"))

            # logo = logo.resize((200, 200), Image.LANCZOS) #resize
            # self.logo_image = ImageTk.PhotoImage(logo) #Put the logo in logo_image variable prevent it from being deleted
            logo_img = ctk.CTkImage(light_image=logo, dark_image=logo, size=(140,140))
            logo_label = ctk.CTkLabel(logo_frame,image=logo_img, text = "")
            logo_label.pack(expand = True)
        except Exception as e:
            messagebox.showerror("Error", f"Can not load logo: {e}")
        
        #create a frame that contains components of login box
        loginbox_frame = ctk.CTkFrame(self.root, fg_color="#ebebeb")
        loginbox_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        #Create labels
        #title Label
        login_title = ctk.CTkLabel(loginbox_frame, text="Đăng nhập", font=("Arial", 24, "bold"), text_color="dark blue")
        login_title.grid(row = 0, column = 0, columnspan = 3, pady = 5)

        #username label
        # username_label = ctk.CTkLabel(loginbox_frame, text="Username:")
        username_label = ctk.CTkLabel(
            loginbox_frame,
            text="Tên Đăng Nhập:",
            anchor="w",                 
            text_color="#333333",        
            font=("Arial", 14, "bold")   
        )
        username_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky="e")

        #username entry
        self.username_entry = ctk.CTkEntry(
            loginbox_frame,
            placeholder_text="Tên Đăng Nhập",  # Adds placeholder
            width=200,                    # Width of the entry field
            height=35,                    # Height of the entry
            border_width=0,               # no border
            corner_radius=10,             # rounded corner
            fg_color="#f2f2f2",           # light gray bg for entry.
            text_color="#333333",         # dark gray text color
            placeholder_text_color="#888888" # Placeholder text color
        )
        self.username_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
        #password label
        # pwd_label = ctk.CTkLabel(loginbox_frame, text="Password:")
        pwd_label = ctk.CTkLabel(
            loginbox_frame,
            text="Mật khẩu:",
            anchor="w",                 
            text_color="#333333",        
            font=("Arial", 14, "bold")   
        )
        pwd_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky="e")

        #password entry
        # Customize the entry field with a modern style
        self.password_entry = ctk.CTkEntry(
            loginbox_frame,
            placeholder_text="Mật khẩu",  show ="*",
            width=200,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.password_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

        #login button
        login_btn = ctk.CTkButton(loginbox_frame, text="Đăng Nhập", command=self.on_login)
        login_btn.grid(row = 3, column = 0, columnspan = 2, ipadx = 50, pady = 5)

        #register button
        btn_register = ctk.CTkButton(loginbox_frame, text="Tạo tài khoản", command=self.on_register)
        btn_register.grid(row = 4, column = 0, columnspan = 2,ipadx = 50, pady = 5)

        #forgot password button
        btn_forgot_pwd = ctk.CTkButton(loginbox_frame, text="Quên mật khẩu?", fg_color="transparent", 
                                        hover_color="light blue",
                                        text_color="black",
                                        anchor="center", 
                                        command=self.on_forgot)
        btn_forgot_pwd.configure(font=("Arial", 12, "underline")) # Underline the button text
        btn_forgot_pwd.grid(row = 5, column = 0, columnspan = 2,ipadx = 50, pady = 5)

    def on_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        #create object DTO user
        user = userDTO.userDTO(username,password)
        #check user using BUS method
        if self.userBUS.login(user):
            self.root.destroy() #close login
            Changetab.Changetab() #change manage screen
        else:
            messagebox.showerror("Đăng nhập thất bại", "Tên đăng nhập hoặc mật khẩu không đúng.")
       
    def on_register(self):
        RegisterGUI.RegisterGUI()

    def on_forgot(self ):
        Forgort_pwdGUI.Forgot_pwdGUI()

if __name__ == "__main__":
    LoginGUI()
