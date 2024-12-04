import customtkinter as ctk
import tkinter as ttk
from PIL import Image,ImageTk
import os

class RegisterSubject:
    def __init__(self):
        self.root = ctk.CTk()
        self.current_page = 1
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
        content_frame = ctk.CTkFrame(main_canvas,width=870,height=450,fg_color='red')
        content_frame.place(x=0,y=100)

       
        
        add_button_ar = dict()
        add_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "plus.png"))
        add_icon_ctk = ctk.CTkImage(light_image=add_icon,dark_image=add_icon,size=(15,15))
        zoomed_add_icon_ctk = ctk.CTkImage(light_image=add_icon,dark_image=add_icon,size=(20,20))

        content = [
            ('713', 'Machine Learning', 'TTNT', '4', 'Võ Tắc Thiên', '0/10'),
            ('714', 'Deep Learning', 'TTNT', '3', 'Nguyễn Văn A', '5/30'),
            ('715', 'Computer Vision', 'TTNT', '4', 'Trần Thị B', '15/40'),
            ('716', 'Natural Language Processing', 'TTNT', '3', 'Lê Văn C', '20/50'),
            ('717', 'Data Mining', 'TTNT', '3', 'Phạm Thị D', '10/35'),
            ('718', 'Artificial Intelligence', 'TTNT', '4', 'Hoàng Văn E', '25/45'),
            ('719', 'Neural Networks', 'TTNT', '3', 'Đỗ Thị F', '30/40'),
            ('720', 'Pattern Recognition', 'TTNT', '3', 'Ngô Văn G', '12/30'),
            ('721', 'Big Data Analytics', 'TTNT', '4', 'Bùi Thị H', '18/40'),
            ('722', 'Robotics', 'TTNT', '3', 'Vũ Văn I', '22/35'),
            ('723', 'Expert Systems', 'TTNT', '3', 'Đinh Thị K', '8/25'),
            ('724', 'Knowledge Representation', 'TTNT', '4', 'Lý Văn L', '15/35'),
            ('725', 'Cognitive Computing', 'TTNT', '3', 'Mai Thị M', '20/40'),
            ('726', 'Reinforcement Learning', 'TTNT', '4', 'Trương Văn N', '25/45'),
            ('727', 'Computer Graphics', 'TTNT', '3', 'Đặng Thị P', '30/50'),
            ('728', 'Image Processing', 'TTNT', '3', 'Hồ Văn Q', '17/35'),
            ('729', 'Speech Recognition', 'TTNT', '4', 'Phan Thị R', '23/40'),
            ('730', 'Evolutionary Computing', 'TTNT', '3', 'Tống Văn S', '19/35'),
            ('731', 'Fuzzy Logic', 'TTNT', '3', 'Dương Thị T', '27/45'),
            ('732', 'Data Visualization', 'TTNT', '4', 'Lương Văn U', '14/30')
        ]
        length = len(content)
        left_limit = (self.current_page-1)*10
        right_limit = (self.current_page*10)-1
        print(left_limit)
        print(right_limit)
        for i in range((self.current_page-1)*10,(self.current_page*10)):
            mamon_row = ctk.CTkLabel(main_canvas,text='713',font=('Roboto',13))
            mamon_row.place(x=10,y=i*45+110)
            
            tenmon_row = ctk.CTkLabel(main_canvas,text='Machine Learning',font=('Roboto',13))
            tenmon_row.place(x=100,y=i*45+110)
            
            makhoa_row = ctk.CTkLabel(main_canvas,text='TTNT',font=('Roboto',13))
            makhoa_row.place(x=330,y=i*45+110)

            sotc_row = ctk.CTkLabel(main_canvas,text='4',font=('Roboto',13))
            sotc_row.place(x=420,y=i*45+110)

            giangvien_row = ctk.CTkLabel(main_canvas,text='Võ Tắc Thiên',font=('Roboto',13))
            giangvien_row.place(x=500,y=i*45+110)
            
            siso_row = ctk.CTkLabel(main_canvas,text='0/10',font=('Roboto',13))
            siso_row.place(x=700,y=i*45+110)
            

            add_button_ar[i] = ctk.CTkButton(main_canvas,
                                    image=add_icon_ctk, 
                                    text='',
                                    width=10,
                                    height=25,
                                    hover_color='#dbdbdb',
                                    fg_color='transparent',
                                    command=lambda x=i: print(x))
            add_button_ar[i].place(x=800,y=i*45+110)

            add_button_ar[i].bind('<Enter>',lambda e,x=i: add_button_ar[x].configure(image=zoomed_add_icon_ctk))
            add_button_ar[i].bind('<Leave>',lambda e,x=i: add_button_ar[x].configure(image=add_icon_ctk))
        
