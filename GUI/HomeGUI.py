import customtkinter as ctk
from tkinter import messagebox, ttk, W
from PIL import Image, ImageTk #library Pillow for handling images
import sqlite3
from LoginGUI import *

class HomeGUI:
    def __init__(self):
        # Main window
        self.root = ctk.CTk()
        self.root.title("Student Management System")

        #custom window_size and window_bgcolor
        self.root.geometry("400x400")
        self.root.configure(fg_color = "light blue") #light blue

        #load widgets
        self.create_home_screen()

        #run window
        self.root.mainloop()

    def create_home_screen(self):
        #Title
        title_label = ctk.CTkLabel(self.root, text="Welcome to the Student Management System", font=("Arial", 18, "bold"), text_color="dark blue")
        title_label.pack(pady = 10)
        
        #MenuTitle
        title_label = ctk.CTkLabel(self.root, text=f"Hi! Teacher", font=("Arial", 18, "bold"), text_color="dark blue")
        title_label.pack(pady=10)
        
        #Frame that contains all of the button
        btn_frame = ctk.CTkFrame(self.root, fg_color="light blue") #dark green frame
        btn_frame.pack(pady = 10)

        #Add student
        addStudent_btn = ctk.CTkButton(btn_frame, text="Add Student", command=self.define_later, fg_color="dark blue", text_color="white")
        addStudent_btn.grid(row = 0, column = 0, columnspan = 2, ipadx = 100, pady = 5)

        #Exit button
        exit_btn = ctk.CTkButton(btn_frame, text="Quit", command=self.root.destroy, fg_color="dark blue", text_color="white")
        exit_btn.grid(row = 1, column = 0, columnspan = 2, ipadx = 100, pady = 5)


    def define_later():
        pass


#run GUI
if __name__ == "__main__":
    HomeGUI()