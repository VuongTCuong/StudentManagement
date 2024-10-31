import customtkinter as ctk
from tkinter import messagebox, ttk, W
from PIL import Image, ImageTk #library Pillow for handling images
import HomeGUI

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

class RegisterGUI:
    def __init__(self):
        self.userBUS = userBUS.userBUS()

        # Main login window
        self.root = ctk.CTk()
        self.root.title("Student Management System - Register")
        self.root.geometry("400x400")

        # Set appearance mode and default theme
        ctk.set_appearance_mode("light") #Change to white mode
        ctk.set_default_color_theme("blue")

        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Adding widgets and create a login screen
        self.create_register_screen()

        #run
        self.root.mainloop()
    def create_register_screen(self):
        # Create widgets
        register_frame = ctk.CTkFrame(self.root, fg_color="#ebebeb")
        register_frame.grid(row=0, column=0, columnspan = 3 , padx=50, pady=20, sticky="nsew")

        # Create title label
        label = ctk.CTkLabel(register_frame, text="Create New Account", font=("Arial", 24, "bold"),
                             text_color="dark blue")
        label.grid(row=0, column=0, columnspan=3, ipadx = 3, pady=12, padx=10,)

        #Create email label
        email_label = ctk.CTkLabel(register_frame, text="Email:",anchor="w")
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        #Create email entry
        self.email_entry = ctk.CTkEntry(register_frame, placeholder_text="Enter Email")
        self.email_entry.grid(row=1, column=1, columnspan=2, pady=12, padx=10)

        #username label
        username_label = ctk.CTkLabel(register_frame, text="Username:",anchor="w")
        username_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

        #Create username entry
        self.username_entry = ctk.CTkEntry(register_frame, placeholder_text="Enter Username")
        self.username_entry.grid(row=2, column=1, columnspan=2, pady=12, padx=10)

        #Create password label
        password_label = ctk.CTkLabel(register_frame, text="Password:", anchor="w")
        password_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        #Create password entry
        self.password_entry = ctk.CTkEntry(register_frame, placeholder_text="Enter Password", show="*")
        self.password_entry.grid(row=3, column=1, columnspan=2, pady=12, padx=10)

        #Create confirm password label
        confirm_password_label = ctk.CTkLabel(register_frame, text="Confirm Password:",anchor="w")
        confirm_password_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        # Create confirm password entry
        self.confirm_password_entry = ctk.CTkEntry(register_frame, placeholder_text="Confirm Password", show="*")
        self.confirm_password_entry.grid(row=4, column=1, columnspan=2, pady=12, padx=10)

        # Create sign up button
        self.signup_button = ctk.CTkButton(register_frame, text="Register", command=self.on_register)
        self.signup_button.grid(row=5, column=0, columnspan=3, pady=12, padx=10, sticky="ew")

        # Create Exit button
        self.exit_button = ctk.CTkButton(register_frame, text="Exit", command=self.on_exit)
        self.exit_button.grid(row=6, column=0, columnspan=3, pady=12, padx=10, sticky="ew")

    def email_is_valid(self, email):
        # Define the regular expression for validating an email
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Check if the email matches the pattern
        return re.match(email_regex, email) is not None #return True if matchs, False if not match

    def on_register(self):
        # get informations
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        ##CHECKING INPUT
        #check all empty entries
        if not email or not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required. Please ensure no fields are left empty.")

        #check email valid, email existed?
        if self.email_is_valid(email) == False:
            messagebox.showerror("Error", "Email is invalid.")
        if self.userBUS.userDAL.existed_email(email):
            messagebox.showerror("Error", "Email is existed.")

        #check pwd == confirm_pwd
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")


        ##SENDING CODE FOR REGISTERING
        #random OTP 4 numbers
        self.OTP = random.randint(1000,9999)

        #send OTP via email
        if self.send_otp_codes(email):
            self.create_otp_window(email, username, password) #if sent, create otp input window.
        else:
            messagebox.showerror("Error", "Cannot send OTP via Email.")
    
    def send_otp_codes(self, reciever_email):
        try:
                #Email content
                subject = "Here's your OTP Code"
                body = f"Your code is: {self.OTP}"

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

    def create_otp_window(self, email, username, password):
        #create OTP window
        OTP_window = ctk.CTkToplevel(self.root)
        OTP_window.title("Student Management System - OTP Verification")
        OTP_window.geometry("500x150")
        # Set appearance mode and default theme
        ctk.set_appearance_mode("light") #Change to white mode
        ctk.set_default_color_theme("blue")
        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        #Title Label
        title_lbl = ctk.CTkLabel(OTP_window, text="Enter your OTPs sent via email", font=("Arial", 24, "bold"), text_color="dark blue")
        title_lbl.pack(pady = 15)

        #####   Entry for OTP  ######
        otp_entry = ctk.CTkEntry(OTP_window)
        otp_entry.pack(pady = 10)
        
        # Function to get OTP and verify it
        def verify_otp():
            otp_code = otp_entry.get()
            # Check if the OTP code is exactly 4 digits and convert to integer
            try:
                if otp_code.isdigit() and int(otp_code) == self.OTP:
                    #Create account
                    user = userDTO.userDTO(email, password)
                    self.userBUS.register(user, username)
                    messagebox.showinfo("Success", "Account is created.")
                    OTP_window.destroy()
                else:
                    messagebox.showerror("Error", "OTP is not correct.")
            except Exception as e:
                messagebox.showerror("Error", f"{e}")

        submit_button = ctk.CTkButton(OTP_window, text="Verify OTP", command=verify_otp)
        submit_button.pack(pady = 10)


    def on_exit(self):
        # Ask for confirmation
        result = messagebox.askyesno("Confirmation", "Do you want to exit?")
        if result:
            # Save data and exit
            self.root.destroy()



if __name__ == "__main__":
    RegisterGUI()