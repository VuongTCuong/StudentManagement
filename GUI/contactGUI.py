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
from email.mime.multipart import MIMEMultipart
from cryptography.fernet import Fernet


class ContactGUI:
    def __init__(self, receiver):
        self.app = ctk.CTk()
        self.app.title("Student Management System - Form Gửi Email")
        self.app.geometry("500x500")
        self.app.resizable(False,False)
        self.receiver = receiver
        self.create_widgets()
        self.app.mainloop()

    def create_widgets(self):
        # Tiêu đề
        label_title = ctk.CTkLabel(self.app, text="Gửi Email Cho Sinh Viên", font=("Arial", 24, "bold"),
                             text_color="dark blue")
        label_title.pack(pady=10)

        # Email người nhận
        label_recipient = ctk.CTkLabel(self.app, text="Email Người Nhận:")
        label_recipient.pack(anchor="w", padx=20)
        # self.entry_recipient = ctk.CTkEntry(self.app, width=400, placeholder_text="Nhập email người nhận")

        self.entry_recipient = ctk.CTkEntry(
            self.app,
            placeholder_text="Nhập email người nhận",  
            width=400,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888"
        )
        self.entry_recipient.pack(padx=20, pady=5)
        self.entry_recipient.insert(0, self.receiver)
        if self.entry_recipient is not None: 
            self.entry_recipient.configure(state='disabled',fg_color='#cfe2f3')

        # Tiêu đề email
        label_subject = ctk.CTkLabel(self.app, text="Tiêu Đề:")
        label_subject.pack(anchor="w", padx=20)
        # self.entry_subject = ctk.CTkEntry(self.app, width=400, placeholder_text="Nhập tiêu đề email")
        self.entry_subject = ctk.CTkEntry(
            self.app,
            placeholder_text="Nhập tiêu đề email",  
            width=400,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.entry_subject.pack(padx=20, pady=5)

        # Nội dung email
        label_body = ctk.CTkLabel(self.app, text="Nội Dung:")
        label_body.pack(anchor="w", padx=20)
        self.text_body = ctk.CTkTextbox(self.app, width=400, height=150)
        self.text_body.pack(padx=20, pady=5)

        # Nút Gửi
        button_send = ctk.CTkButton(self.app, text="Gửi Email", command=self.send_email)
        button_send.pack(pady=20)

    def send_email(self):
        sender_email = 'thuando.contact@gmail.com'
        sender_pwd = 'nodc miwi odav tepq'  # Thay bằng mật khẩu ứng dụng (nếu dùng Gmail)


        if os.path.exists('user.txt'):
            f = Fernet(b'LkQhEOBncRePoyysixPYu-I2Q-uDd-UZH18e8M2_HJE=')
            user_file = open('user.txt','rb')
            username = user_file.readline()
            username = f.decrypt(username).decode()

        intro = "Thư được gửi bởi: " + username + " \n"
        recipient_email = self.entry_recipient.get()
        subject = self.entry_subject.get()
        body = intro + self.text_body.get("1.0", "end-1c")

        if not recipient_email or not subject or not body:
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return

        try:
            # Tạo email
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

            # Gửi email qua SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(sender_email, sender_pwd)
                server.send_message(msg)
            
            messagebox.showinfo("Thành công", "Email đã được gửi thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể gửi email: {str(e)}")


