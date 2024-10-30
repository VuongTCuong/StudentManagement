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


class RegisterGUI:
    def __init__(self):
        self.userBUS = userBUS.userBUS()

        # Main login window
        self.root = ctk.CTk()
        self.root.title("Student Management System- Register")
        self.root.geometry("500x240")

        # Set appearance mode and default theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Đặt cấu trúc cột cho cửa sổ chính để chia đều trái và phải
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)

        # Adding widgets and create a login screen
        self.create_register_screen()

        #run
        self.root.mainloop()
    def create_register_screen(self):
        pass