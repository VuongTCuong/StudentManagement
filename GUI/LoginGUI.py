import customtkinter as ctk
from tkinter import messagebox, ttk, W
from PIL import Image, ImageTk #library Pillow for handling images
import sqlite3
import HomeGUI


class LoginGUI:

    def __init__(self):
        # Main login window
        self.root = ctk.CTk()
        self.root.title("Student Management System")
        self.root.geometry("500x240")

        # Set appearance mode and default theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # connect db and handling error
        try:
            self.conn = sqlite3.connect('student_management.db')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Database is not created: {e}")

        # Adding widgets and create a login screen
        self.create_login_screen()

        #run
        self.root.mainloop()
    
    def create_login_screen(self):
        #logo frame
        logo_frame = ctk.CTkFrame(self.root)
        logo_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        #load logo
        try: 
            logo = Image.open("E:\\Study Stuff\\StudentManagement\\GUI\\assets\\logo.png")
            # logo = logo.resize((200, 200), Image.LANCZOS) #resize
            # self.logo_image = ImageTk.PhotoImage(logo) #Put the logo in logo_image variable prevent it from being deleted
            logo_img = ctk.CTkImage(light_image=logo, dark_image=logo, size=(140,140))
            logo_label = ctk.CTkLabel(logo_frame,image=logo_img, text = "")
            logo_label.pack(expand = True)
        except Exception as e:
            messagebox.showerror("Error", f"Can not load logo: {e}")
        
        #create a frame that contains components of login box
        loginbox_frame = ctk.CTkFrame(self.root)
        loginbox_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        #Create labels
        #title Label
        login_title = ctk.CTkLabel(loginbox_frame, text="Login", font=("Arial", 24, "bold"), text_color="light blue")
        login_title.grid(row = 0, column = 0, columnspan = 3, pady = 5)

        #username label
        username_label = ctk.CTkLabel(loginbox_frame, text="Username:")
        username_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky="e")

        #username entry
        self.username_entry = ctk.CTkEntry(loginbox_frame)
        self.username_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

        #password label
        pwd_label = ctk.CTkLabel(loginbox_frame, text="Password:")
        pwd_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky="e")

        #password entry
        self.password_entry = ctk.CTkEntry(loginbox_frame, show="*")
        self.password_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

        #login button
        login_btn = ctk.CTkButton(loginbox_frame, text="Login", command=self.check_login)
        login_btn.grid(row = 3, column = 0, columnspan = 2, ipadx = 50, pady = 5)

        #register button
        btn_register = ctk.CTkButton(loginbox_frame, text="Register", command=self.register)
        btn_register.grid(row = 4, column = 0, columnspan = 2,ipadx = 50, pady = 5)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the users table
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.root.destroy() #close login
            # print(f"Hello {user}")
            HomeGUI.HomeGUI()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
       
    def register(self):
        pass
if __name__ == "__main__":
    LoginGUI()