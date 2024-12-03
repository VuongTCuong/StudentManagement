import customtkinter as ctk
from PIL import Image
import StudentProfile
class StudentPage:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title('Trang sinh viên - thông tin')
        self.root.geometry('1200x600')
        
        self.cur_tab = 'thongtin'
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

        mssv_lab = ctk.CTkLabel(user_canvas,text='3121411033',text_color='#3d6d8b',font=('Roboto',16))
        mssv_lab.place(x=120,y=45)

        user_canvas.create_line((0,75,305,75),fill='#b8bec9')
        hoten_lab = ctk.CTkLabel(user_canvas,text='Họ và tên',text_color='#3d6d8b',font=('Roboto',16))
        hoten_lab.place(x=10,y=80)
        
        hotenuser_lab = ctk.CTkLabel(user_canvas,text='Vương Tiểu Cường',text_color='#3d6d8b',font=('Roboto',16))
        hotenuser_lab.place(x=120,y=80)

        logout_button = ctk.CTkButton(user_canvas,text='Đăng xuất',fg_color='#fec107',width=280,text_color='black',font=('Roboto',16))
        logout_button.place(x=10,y=110)
        logout_button.configure(hover_color='#cfa619')
        doimk_button = ctk.CTkButton(user_canvas,text='Đổi mật khẩu',text_color='#3d6d8b',font=('Roboto',15,'underline'),width=20)
        doimk_button.place(x=190,y=140)
        doimk_button.configure(fg_color="transparent",hover_color='#3d6d8b')

        doimk_button.bind('<Enter>',lambda e:doimk_button.configure(text_color='#1b2f3d'))
        doimk_button.bind('<Leave>',lambda e:doimk_button.configure(text_color='#3d6d8b'))

    def menu_canvas(self):
        menu_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=300,height=390)
        menu_canvas.place(x=10,y=200)

        self.thongtin_button = ctk.CTkButton(menu_canvas,text='Thông tin',text_color='#3d6d8b',font=('Roboto',16),width=280)
        self.thongtin_button.place(x=10,y=10)
        self.thongtin_button.configure(fg_color='#aab0b6',corner_radius=0,hover_color='#dbdbdb',anchor='w')
        self.thongtin_button.bind('<Enter>',lambda e:self.thongtin_button.configure(text_color='#1b2f3d'))
        self.thongtin_button.bind('<Leave>',lambda e:self.thongtin_button.configure(text_color='#3d6d8b'))
        
        menu_canvas.create_line((0,45,305,45),fill='#b8bec9')

        dangkymon_button = ctk.CTkButton(menu_canvas,text='Đăng ký môn học',text_color='#3d6d8b',font=('Roboto',16),width=280)
        dangkymon_button.place(x=10,y=55)
        dangkymon_button.configure(fg_color='transparent',corner_radius=0,hover_color='#dbdbdb',anchor='w')
        dangkymon_button.bind('<Enter>',lambda e:dangkymon_button.configure(text_color='#1b2f3d'))
        dangkymon_button.bind('<Leave>',lambda e:dangkymon_button.configure(text_color='#3d6d8b'))

        menu_canvas.create_line((0,90,305,90),fill='#b8bec9')

    def main_canvas(self):
        self.main_canvas = ctk.CTkCanvas(self.root,bg='#dbdbdb',width=865,height=580)
        self.main_canvas.place(x=320,y=10)



        
StudentPage()