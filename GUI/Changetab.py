import customtkinter as ctk
import StudentMgt, ClassMgt, DepartmentMgt, ScoreMgt, SubjectMgt, OpenClass

import sys
from tkinter import messagebox
import LoginGUI
import tkinter as tk
import os
from cryptography.fernet import Fernet
from PIL import Image, ImageTk 

class Changetab:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Student Management System - Student Management") 
        self.root.configure(fg_color='#F2DDDC')
        #center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1400
        window_height = 600
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.resizable(False,False)

        #current tab
        self.cur_tab = 'StudentMgt'
        
        #menu frame
        self.top_frame()

        #left and right frame
        self.left_frame()
        self.right_frame()

        #current tab
        self.set_current_tab(self.cur_tab)

        self.root.mainloop()

    def top_frame(self):
        #parent
        self.top_frame = ctk.CTkFrame(self.root,fg_color='#F6BCBA',width=1400,height=40)
        self.top_frame.pack(side='top',padx=20,pady=5)
        
        #center top-down button in parent (28 is default height of any button)
        y_center = (self.top_frame._current_height-28)/2
       
        #child
        sv_tab_button = ctk.CTkButton(self.top_frame,text='Sinh Viên',width=80,command=self.changeto_student_tab)
        sv_tab_button.place(x=5,y=y_center)
        
        lop_tab_button = ctk.CTkButton(self.top_frame, text='Lớp',width=80,command=self.changeto_class_tab)
        lop_tab_button.place(x=90, y=y_center)

        khoa_tab_button = ctk.CTkButton(self.top_frame, text='Khoa',width=80,command=self.changeto_department_tab)
        khoa_tab_button.place(x=175, y=y_center)

        diem_tab_button = ctk.CTkButton(self.top_frame, text='Điểm',width=80,command=self.changeto_score_tab)
        diem_tab_button.place(x=260, y=y_center)

        #align 85px each
        mon_tab_button = ctk.CTkButton(self.top_frame, text='Môn học',width=80,command=self.changeto_subject_tab)
        mon_tab_button.place(x=345, y=y_center)

        open_class_button = ctk.CTkButton(self.top_frame, text='Mở lớp',width=80,command=self.changeto_openclass_tab)
        open_class_button.place(x=430, y=y_center)
        #current user label
        if os.path.exists('user.txt'):
            f = Fernet(b'LkQhEOBncRePoyysixPYu-I2Q-uDd-UZH18e8M2_HJE=')
            user_file = open('user.txt','rb')
            username = user_file.readline()
            username = f.decrypt(username).decode()
            
            len_label = len('Xin chào, '+username)
            username_label = ctk.CTkLabel(self.top_frame, text = 'Xin chào, '+username)
            username_label.place(x=1060-(len_label*2),y=y_center)

        
        
        #logout
        logout_button = ctk.CTkButton(self.top_frame, text='Đăng xuất',width=80,command=self.logout)
        
        logout_button.place(x=1180,y=y_center)
        #need EXIT button
        exit_button = ctk.CTkButton(self.top_frame, text='Thoát',width=80,command=self.on_exit)
        exit_button.place(x=1270, y=y_center)

    def logout(self):
        result = messagebox.askyesno("Confirmation", "Bạn có muốn đăng xuất không?")
        if result:
            self.root.destroy()
            os.remove('user.txt')
            LoginGUI.LoginGUI()
    def on_exit(self):
    # Ask for confirmation
        result = messagebox.askyesno("Confirmation", "Bạn có muốn thoát không?")
        if result:
            # Destroy the root window
            self.root.destroy()
            # Terminate the program
            sys.exit()
            
    def left_frame(self):
        self.left_frame = ctk.CTkFrame(self.root,fg_color='#F6BCBA',height=self.root._current_height-70,width=self.root._current_width/3)
        self.left_frame.pack(side='left',padx=20)

    def right_frame(self):
        self.right_frame = ctk.CTkFrame(self.root,fg_color='#F6BCBA',height=self.root._current_height-70,width=self.root._current_width*2/3)
        self.right_frame.pack(side='right',padx=20)
    def center_frame(self):
        self.center_frame = ctk.CTkFrame(self.root,fg_color='#F6BCBA',height=self.root._current_height-70,width=self.root._current_width*2/3)
        self.center_frame.pack(side='left',padx=20)

    def set_current_tab(self,tab_name):
        if tab_name=='StudentMgt':
            student = StudentMgt.StudentMgt()
            student.create_interactframe(self.left_frame)
            student.create_tableframe(self.right_frame)
        elif tab_name=='ClassMgt':
            class_obj = ClassMgt.ClassMgt()
            class_obj.create_interactframe(self.left_frame)
            class_obj.create_tableframe(self.right_frame)
        elif tab_name=='DepartmentMgt':
            department = DepartmentMgt.DepartmentMgt()
            department.create_interactframe(self.left_frame)
            department.create_tableframe(self.right_frame)
        elif tab_name=='ScoreMgt':
            score = ScoreMgt.ScoreMgt()
            score.create_interactframe(self.left_frame)
            score.create_tableframe(self.right_frame)

    def destroy_LeftRight_children(self):
        for i in self.left_frame.winfo_children():
            i.destroy()
        for j in self.right_frame.winfo_children():
            j.destroy()

    def changeto_student_tab(self):
        if self.cur_tab!='StudentMgt':
            self.destroy_LeftRight_children()

            student = StudentMgt.StudentMgt()
            self.root.title("Student Management System - Quản lý sinh viên") 
            student.create_interactframe(self.left_frame)
            student.create_tableframe(self.right_frame)
            self.cur_tab ='StudentMgt'

    def changeto_class_tab(self):
        if self.cur_tab!='ClassMgt':
            self.destroy_LeftRight_children()

            class_obj = ClassMgt.ClassMgt()
            self.root.title("Student Management System - Quản lý lớp")
            class_obj.create_interactframe(self.left_frame)
            class_obj.create_tableframe(self.right_frame)
            self.cur_tab='ClassMgt'

    def changeto_department_tab(self):
        if self.cur_tab!='DepartmentMgt':
            self.destroy_LeftRight_children()
            department = DepartmentMgt.DepartmentMgt()
            self.root.title("Student Management System - Quản lý khoa")
            department.create_interactframe(self.left_frame)
            department.create_tableframe(self.right_frame)
            self.cur_tab='DepartmentMgt'
    
    def changeto_score_tab(self):
        if self.cur_tab!='ScoreMgt':
            self.destroy_LeftRight_children()

            score = ScoreMgt.ScoreMgt()
            self.root.title("Student Management System - Quản lý điểm")
            score.create_interactframe(self.left_frame) 
            score.create_tableframe(self.right_frame)
            self.cur_tab='ScoreMgt'

    def changeto_subject_tab(self):
        if self.cur_tab!='SubjectMgt':
            self.destroy_LeftRight_children()

            subject = SubjectMgt.SubjectMgt()
            self.root.title("Student Management System - Quản lý Môn học")
            subject.create_interactframe(self.left_frame) 
            subject.create_tableframe(self.right_frame)
            self.cur_tab='SubjectMgt'

    def changeto_openclass_tab(self):
        if self.cur_tab!='Openclass':
            self.destroy_LeftRight_children()
            openclass = OpenClass.OpenClass()
            openclass.root=self.root
            self.root.title("Student Management System - Mở lớp dạy")
            openclass.create_interactframe(self.left_frame)
            openclass.create_tableframe(self.right_frame)
            self.cur_tab='Openclass'