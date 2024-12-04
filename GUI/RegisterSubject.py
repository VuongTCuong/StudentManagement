import customtkinter as ctk
import tkinter as ttk
from PIL import Image
import os

class RegisterSubject:
    def __init__(self):
        self.root = ctk.CTk()

    def create_maincanvas(self,main_canvas):
        main_canvas.create_rectangle((0,0,870,40),fill='#d2cfcf')
        main_canvas.create_text((89,22),text='Đăng ký môn học',fill='#02578a',font=('Roboto 13 bold'))
        main_canvas.create_line((0,40,870,40),fill='#b8bec9')

        self.search_entry = ctk.CTkEntry(main_canvas,width=150,placeholder_text='Mã/Tên môn học')
        self.search_entry.place(x=10,y=50)

        search_button = ctk.CTkButton(main_canvas,text='Tìm kiếm',width=70,height=27,text_color='black')
        search_button.place(x=170,y=50)

        reset_button = ctk.CTkButton(main_canvas,text='Reset',width=70,height=27,text_color='black')
        reset_button.place(x=250,y=50)


        #table
        mamon_header = ctk.CTkLabel(main_canvas,text='Mã môn',font=('Roboto',15,'bold'),text_color='black')
        mamon_header.place(x=10,y=80)
        
        tenmon_header = ctk.CTkLabel(main_canvas,text='Tên môn',font=('Roboto',15,'bold'))
        tenmon_header.place(x=100,y=80)
        
        makhoa_header = ctk.CTkLabel(main_canvas,text='Khoa',font=('Roboto',15,'bold'))
        makhoa_header.place(x=330,y=80)

        sotc_header = ctk.CTkLabel(main_canvas,text='Số TC',font=('Roboto',15,'bold'))
        sotc_header.place(x=420,y=80)

        giangvien_header = ctk.CTkLabel(main_canvas,text='Giảng viên',font=('Roboto',15,'bold'))
        giangvien_header.place(x=500,y=80)
        
        siso_header = ctk.CTkLabel(main_canvas,text='Sỉ số',font=('Roboto',15,'bold'))
        siso_header.place(x=700,y=80)

        # Row below header
        mamon_row = ctk.CTkLabel(main_canvas,text='713',font=('Roboto',13))
        mamon_row.place(x=10,y=110)
        
        tenmon_row = ctk.CTkLabel(main_canvas,text='Machine Learning',font=('Roboto',13))
        tenmon_row.place(x=100,y=110)
        
        makhoa_row = ctk.CTkLabel(main_canvas,text='TTNT',font=('Roboto',13))
        makhoa_row.place(x=330,y=110)

        sotc_row = ctk.CTkLabel(main_canvas,text='4',font=('Roboto',13))
        sotc_row.place(x=420,y=110)

        giangvien_row = ctk.CTkLabel(main_canvas,text='Võ Tắc Thiên',font=('Roboto',13))
        giangvien_row.place(x=500,y=110)
        
        siso_row = ctk.CTkLabel(main_canvas,text='0/10',font=('Roboto',13))
        siso_row.place(x=700,y=110)
        
        add_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "plus.png"))

        add_icon_ctk = ctk.CTkImage(light_image=add_icon,dark_image=add_icon,size=(15,15))
        add_button = ctk.CTkButton(main_canvas,
                                   image=add_icon_ctk,
                                   text='',
                                   width=10,
                                   height=25,
                                   hover_color='#dbdbdb',
                                   fg_color='transparent')
        add_button.place(x=800,y=110)