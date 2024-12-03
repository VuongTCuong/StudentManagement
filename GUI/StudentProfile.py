import customtkinter as ctk
from PIL import Image
class StudentProfile:
    def __init__(self):
        self.root = ctk.CTk()

    def create_maincanvas(self,main_canvas):
        main_canvas.create_rectangle((0,0,870,40),fill='#d2cfcf')
        main_canvas.create_text((89,22),text='Thông tin sinh viên',fill='#02578a',font=('Roboto 13 bold'))
        main_canvas.create_line((0,40,870,40),fill='#b8bec9')
        
        masv_lab = ctk.CTkLabel(main_canvas,text='Mã sinh viên:',font=('Roboto',16))
        masv_lab.place(x=10,y=50)

        hoten_lab = ctk.CTkLabel(main_canvas,text='Họ và tên:',font=('Roboto',16))
        hoten_lab.place(x=10,y=85)

        namsinh_lab = ctk.CTkLabel(main_canvas,text='Ngày sinh:',font=('Roboto',16))
        namsinh_lab.place(x=10,y=120)

        gioitinh_lab = ctk.CTkLabel(main_canvas,text='Giới tính:',font=('Roboto',16))
        gioitinh_lab.place(x=10,y=155)

        email_lab = ctk.CTkLabel(main_canvas,text='Email:',font=('Roboto',16))
        email_lab.place(x=10,y=190)

        khoa_lab = ctk.CTkLabel(main_canvas,text='Khoa:',font=('Roboto',16))
        khoa_lab.place(x=10,y=225)

        lop_lab = ctk.CTkLabel(main_canvas,text='Lớp:',font=('Roboto',16))
        lop_lab.place(x=10,y=260)

        main_canvas.create_rectangle((680,50,820,220),outline='black')