import customtkinter as ctk
from tkinter import messagebox, ttk, W
from PIL import Image, ImageTk #library Pillow for handling images
import LoginGUI

class HomeGUI:
    def __init__(self, current_user):
        self.current_user = current_user
        # Main window
        self.root = ctk.CTk()
        self.root.title("Student Management System - Home")

        # Set appearance mode and default theme
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        #custom window_size and window_bgcolor
        self.root.geometry("450x400")
        self.root.configure(fg_color="#ebebeb") #set window color
        
        #load widgets
        self.create_home_screen()

        #run window
        self.root.mainloop()

    def create_home_screen(self):
        #Title
        title_label = ctk.CTkLabel(self.root, text="Welcome to the Student Management System", font=("Arial", 18, "bold"), text_color="dark blue")
        title_label.pack(pady = 10)
        
        #MenuTitle
        title_label = ctk.CTkLabel(self.root, text=f"Hi! {self.current_user}", font=("Arial", 18, "bold"), text_color="dark blue")
        title_label.pack(pady = 10)
        
        #Frame that contains all of the button
        btn_frame = ctk.CTkFrame(self.root, fg_color="#ebebeb") #white frame
        btn_frame.pack(pady = 10)

        #Add student
        addStudent_btn = ctk.CTkButton(btn_frame, text="Add Student", command=self.add_student_GUI)
        addStudent_btn.grid(row = 0, column = 0, columnspan = 2, ipadx = 100, pady = 5)

        #Manage Student
        manageStudent_btn = ctk.CTkButton(btn_frame, text="Manage Student", command=self.manage_student_GUI)
        manageStudent_btn.grid(row = 1, column = 0, columnspan = 2, ipadx = 100, pady = 5)

        #Exit button
        exit_btn = ctk.CTkButton(btn_frame, text="Quit", command=self.root.destroy)
        exit_btn.grid(row = 2, column = 0, columnspan = 2, ipadx = 100, pady = 5)


    def add_student_GUI():
        pass
    
    def manage_student_GUI():
        pass

#run GUI
if __name__ == "__main__":
    HomeGUI()