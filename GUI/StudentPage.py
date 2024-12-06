import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import os
import StudentProfile,LoginGUI,RegisterSubject,Forgort_pwdGUI,StudentScore
from BUS import userBUS
from cryptography.fernet import Fernet
class StudentPage:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Trang thông tin sinh viên')
        self.root.geometry('1200x600')
        self.root.resizable(False,False)

        self.cur_tab = 'studentprofile'
        self.user_canvas()
        self.menu_canvas()
        self.main_canvas()

        studentprofile = StudentProfile.StudentProfile()
        studentprofile.create_maincanvas(self.main_canvas)

        self.root.mainloop()

    def user_canvas(self):
        user_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=300,height=180)
        user_canvas.place(x=10,y=10)
        user_canvas.create_rectangle((0,0,305,40),fill='#07689f')
        user_canvas.create_text((70,22),text='ĐĂNG NHẬP',fill='white',font=('20'))
        
        taikhoan_lab = ctk.CTkLabel(user_canvas,text='Tài khoản',text_color='#3d6d8b',font=('Roboto',16))
        taikhoan_lab.place(x=10,y=45)

        if os.path.exists('user.txt'):
            f = Fernet(b'LkQhEOBncRePoyysixPYu-I2Q-uDd-UZH18e8M2_HJE=')
            user_file = open('user.txt','rb')
            username = user_file.readline()
            username = f.decrypt(username).decode()
        self.current_user = username
        mssv_lab = ctk.CTkLabel(user_canvas,text=self.current_user,text_color='#3d6d8b',font=('Roboto',16))
        mssv_lab.place(x=120,y=45)

        user_canvas.create_line((0,75,305,75),fill='#b8bec9')

        user_bus = userBUS.userBUS()
        user = user_bus.get_user_by_id(username)
        
        hoten_lab = ctk.CTkLabel(user_canvas,text='Họ và tên',text_color='#3d6d8b',font=('Roboto',16))
        hoten_lab.place(x=10,y=80)
        
        hotenuser_lab = ctk.CTkLabel(user_canvas,text=user[2],text_color='#3d6d8b',font=('Roboto',16))
        hotenuser_lab.place(x=120,y=80)

        logout_button = ctk.CTkButton(user_canvas,text='Đăng xuất',fg_color='#fec107',width=280,text_color='black',font=('Roboto',16),command=self.logout)
        logout_button.place(x=10,y=110)
        logout_button.configure(hover_color='#cfa619')
        doimk_button = ctk.CTkButton(user_canvas,text='Đổi mật khẩu',text_color='#3d6d8b',font=('Roboto',15,'underline'),width=20,command=self.change_password)
        doimk_button.place(x=190,y=140)
        doimk_button.configure(fg_color="transparent",hover_color='#3d6d8b')

        doimk_button.bind('<Enter>',lambda e:doimk_button.configure(text_color='#1b2f3d'))
        doimk_button.bind('<Leave>',lambda e:doimk_button.configure(text_color='#3d6d8b'))

    def menu_canvas(self):
        menu_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=300,height=390)
        menu_canvas.place(x=10,y=200)

        self.thongtin_button = ctk.CTkButton(menu_canvas,text='Thông tin',text_color='#3d6d8b',font=('Roboto',16),width=280,command=self.changeto_studentprofile)
        self.thongtin_button.place(x=10,y=10)
        self.thongtin_button.configure(fg_color='#aab0b6',corner_radius=0,hover_color='#dbdbdb',anchor='w')
        self.thongtin_button.bind('<Enter>',lambda e:self.thongtin_button.configure(text_color='#1b2f3d'))
        self.thongtin_button.bind('<Leave>',lambda e:self.thongtin_button.configure(text_color='#3d6d8b'))
        
        menu_canvas.create_line((0,45,305,45),fill='#b8bec9')

        self.dangkymon_button = ctk.CTkButton(menu_canvas,text='Đăng ký môn học',text_color='#3d6d8b',font=('Roboto',16),width=280,command=self.changeto_registersubject)
        self.dangkymon_button.place(x=10,y=55)
        self.dangkymon_button.configure(fg_color='transparent',corner_radius=0,hover_color='#dbdbdb',anchor='w')
        self.dangkymon_button.bind('<Enter>',lambda e:self.dangkymon_button.configure(text_color='#1b2f3d'))
        self.dangkymon_button.bind('<Leave>',lambda e:self.dangkymon_button.configure(text_color='#3d6d8b'))

        menu_canvas.create_line((0,90,305,90),fill='#b8bec9')

        self.diem_button = ctk.CTkButton(menu_canvas,text='Xem điểm',text_color='#3d6d8b',font=('Roboto',16),width=280,command=self.changeto_score)
        self.diem_button.place(x=10,y=100)
        self.diem_button.configure(fg_color='transparent',corner_radius=0,hover_color='#dbdbdb',anchor='w')
        self.diem_button.bind('<Enter>',lambda e:self.diem_button.configure(text_color='#1b2f3d'))
        self.diem_button.bind('<Leave>',lambda e:self.diem_button.configure(text_color='#3d6d8b'))

        menu_canvas.create_line((0,135,305,135),fill='#b8bec9')

    def main_canvas(self):
        self.main_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=865,height=580,highlightcolor='#ebebeb')
        self.main_canvas.place(x=320,y=10)
        
    def cancel_highlight_currentchoose(self):
        if self.cur_tab=='studentprofile':
            self.thongtin_button.configure(fg_color='transparent')
        if self.cur_tab=='registersubject':
            self.dangkymon_button.configure(fg_color='transparent')
        if self.cur_tab=='studentscore':
            self.diem_button.configure(fg_color='transparent')

    def changeto_registersubject(self):
        if self.cur_tab!='registersubject':
            self.main_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=865,height=580,highlightcolor='#ebebeb')
            self.main_canvas.place(x=320,y=10)
            self.dangkymon_button.configure(fg_color='#aab0b6')
            register_sub = RegisterSubject.RegisterSubject()
            register_sub.current_user=self.current_user
            register_sub.create_maincanvas(self.main_canvas)
            self.cancel_highlight_currentchoose()
            self.root.title('Trang đăng ký môn học')
            self.cur_tab='registersubject'

    def changeto_studentprofile(self):
        if self.cur_tab!='studentprofile':
            self.main_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=865,height=580,highlightcolor='#ebebeb')
            self.main_canvas.place(x=320,y=10)
            self.thongtin_button.configure(fg_color='#aab0b6')
            studentprofile = StudentProfile.StudentProfile()
            studentprofile.create_maincanvas(self.main_canvas)
            self.cancel_highlight_currentchoose()
            self.root.title('Trang thông tin sinh viên')
            self.cur_tab='studentprofile'

    def changeto_score(self):
        if self.cur_tab!='studentscore':
            self.main_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=865,height=580,highlightcolor='#ebebeb')
            self.main_canvas.place(x=320,y=10)
            self.diem_button.configure(fg_color='#aab0b6')
            studentscore = StudentScore.StudentScore()
            studentscore.current_user=self.current_user
            studentscore.create_maincanvas(self.main_canvas)
            self.cancel_highlight_currentchoose()
            self.root.title('Trang điểm sinh viên')
            self.cur_tab='studentscore'

    def logout(self):
        result = messagebox.askyesno("Confirmation", "Bạn có muốn đăng xuất không?")
        if result:
            self.root.destroy()
            os.remove('user.txt')
            LoginGUI.LoginGUI()
        
    def change_password(self):
        Forgort_pwdGUI.Forgot_pwdGUI()