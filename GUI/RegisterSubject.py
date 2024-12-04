import customtkinter as ctk
import tkinter as ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
from BUS import OpenClassBUS,studentjoinclassBUS
class RegisterSubject:
    def __init__(self):
        self.root = ctk.CTk()
        self.current_page = 1
        self.current_user = ''
        self.studentjoinclass = studentjoinclassBUS.studentjoinclassBUS()
    def create_maincanvas(self,main_canvas):
        main_canvas.create_rectangle((0,0,870,40),fill='#d2cfcf')
        main_canvas.create_text((220,22),text='Đăng ký môn học - Học kì 1 Năm học 2024 - 2025',fill='#02578a',font=('Roboto 13 bold'))
        main_canvas.create_line((0,40,870,40),fill='#b8bec9')

        self.search_entry = ctk.CTkEntry(main_canvas,width=150,placeholder_text='Mã/Tên môn học')
        self.search_entry.place(x=10,y=50)

        search_button = ctk.CTkButton(main_canvas,text='Tìm kiếm',width=70,height=27,text_color='black',command=self.search)
        search_button.place(x=170,y=50)

        reset_button = ctk.CTkButton(main_canvas,text='Reset',width=70,height=27,text_color='black',command=self.reset)
        reset_button.place(x=250,y=50)

        my_class_button = ctk.CTkButton(main_canvas,
                                        text='Lớp đã đăng ký',
                                        width=70,
                                        height=27,
                                        text_color='black',
                                        font=('Roboto',15,'underline'),
                                        fg_color='transparent',
                                        hover_color='#c3c3c3',
                                        command=self.filter_my_class)
        my_class_button.place(x=720,y=50)

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
        self.content_frame = ctk.CTkFrame(main_canvas,width=870,height=450)
        self.content_frame.place(x=0,y=100)
        #lay tat ca cac lop ở trạng thái mở
        openclass_BUS = OpenClassBUS.OpenClassBUS()
        self.content = openclass_BUS.get_all_mo()

        #lấy tất cả các lớp mà sinh viên hiện tại đã tham gia
        
        self.current_join = self.studentjoinclass.get_all_class_joined(self.current_user)
   
        self.changeto_X_page(self.current_page)

        previous_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "left.png"))
        previous_icon_ctk = ctk.CTkImage(light_image=previous_icon,dark_image=previous_icon,size=(25,25))
        zoomed_previous_icon_ctk = ctk.CTkImage(light_image=previous_icon,dark_image=previous_icon,size=(30,30))

        next_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "right.png"))
        next_icon_ctk = ctk.CTkImage(light_image=next_icon,dark_image=next_icon,size=(25,25))
        zoomed_next_icon_ctk = ctk.CTkImage(light_image=next_icon,dark_image=next_icon,size=(30,30))

        previous_page_button = ctk.CTkButton(main_canvas,
                                    image=previous_icon_ctk, 
                                    text='',
                                    width=10,
                                    height=20,
                                    hover_color='#c3c3c3',
                                    fg_color='transparent',
                                    command=self.changeto_previouspage)
        previous_page_button.place(x=745,y=545)

        previous_page_button.bind('<Enter>',lambda e: previous_page_button.configure(image=zoomed_previous_icon_ctk))
        previous_page_button.bind('<Leave>',lambda e: previous_page_button.configure(image=previous_icon_ctk))

        next_page_button = ctk.CTkButton(main_canvas,
                                    image=next_icon_ctk, 
                                    text='',
                                    width=10,
                                    height=20,
                                    hover_color='#c3c3c3',
                                    fg_color='transparent',
                                    command=self.changeto_nextpage)
        next_page_button.place(x=795,y=545)

        next_page_button.bind('<Enter>',lambda e: next_page_button.configure(image=zoomed_next_icon_ctk))
        next_page_button.bind('<Leave>',lambda e: next_page_button.configure(image=next_icon_ctk))

    def changeto_previouspage(self):
        if self.current_page-1>0:
            self.current_page-=1
            self.changeto_X_page(self.current_page)

    def changeto_nextpage(self):
        if self.current_page+1<=(len(self.content)//10+1):
            self.current_page+=1
            self.changeto_X_page(self.current_page)

    def changeto_X_page(self,x):
        for i in self.content_frame.winfo_children():
            i.destroy()
        length = len(self.content)
        left_limit = (x-1)*10
        right_limit = x*10
        if length<right_limit:
            right_limit = length
        add_button_ar = dict()
        add_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "plus.png"))
        add_icon_ctk = ctk.CTkImage(light_image=add_icon,dark_image=add_icon,size=(15,15))
        zoomed_add_icon_ctk = ctk.CTkImage(light_image=add_icon,dark_image=add_icon,size=(20,20))

        tick_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "check.png"))
        tick_icon_ctk = ctk.CTkImage(light_image=tick_icon,dark_image=tick_icon,size=(17,17))

        for i in range(left_limit,right_limit):
            mamon_row = ctk.CTkLabel(self.content_frame,text=self.content[i][1],font=('Roboto',13))
            mamon_row.place(x=10,y=(i%10)*45+10)
            
            tenmon_row = ctk.CTkLabel(self.content_frame,text=self.content[i][2],font=('Roboto',13))
            tenmon_row.place(x=100,y=(i%10)*45+10)
            
            makhoa_row = ctk.CTkLabel(self.content_frame,text=self.content[i][3],font=('Roboto',13))
            makhoa_row.place(x=330,y=(i%10)*45+10)

            sotc_row = ctk.CTkLabel(self.content_frame,text=self.content[i][4],font=('Roboto',13))
            sotc_row.place(x=420,y=(i%10)*45+10)

            giangvien_row = ctk.CTkLabel(self.content_frame,text=self.content[i][7],font=('Roboto',13))
            giangvien_row.place(x=500,y=(i%10)*45+10)
            
            siso_row = ctk.CTkLabel(self.content_frame,text=self.content[i][8],font=('Roboto',13))
            siso_row.place(x=700,y=(i%10)*45+10)
            
            
            if self.content[i][0] not in self.current_join:

                add_button_ar[self.content[i][0]] = ctk.CTkButton(self.content_frame,
                                                    image=add_icon_ctk, 
                                                    text='',
                                                    width=10,
                                                    height=25,
                                                    hover_color='#dbdbdb',
                                                    fg_color='transparent',
                                                    command=lambda x=self.content[i][0]: self.student_join(x))
                add_button_ar[self.content[i][0]].place(x=800,y=(i%10)*45+10)
                add_button_ar[self.content[i][0]].bind('<Enter>',lambda e,x=self.content[i][0]: add_button_ar[x].configure(image=zoomed_add_icon_ctk))
                add_button_ar[self.content[i][0]].bind('<Leave>',lambda e,x=self.content[i][0]: add_button_ar[x].configure(image=add_icon_ctk))
            else:
 
                tick_button = ctk.CTkButton(self.content_frame,
                                            image=tick_icon_ctk, 
                                            text='',
                                            width=10,
                                            height=25,
                                            hover_color='#dbdbdb',
                                            fg_color='transparent',
                                            command=lambda x=self.content[i][0]: self.cancel_join(x))
                tick_button.place(x=800,y=(i%10)*45+10)

    def student_join(self,current_lop):
        result = messagebox.askyesno("Xác nhận", "Bạn có muốn đăng ký lớp này không ?")
        if result:
            messagebox.showinfo('Thông báo','Đăng ký thành công!')
            studentjoinclass_bus = studentjoinclassBUS.studentjoinclassBUS()
            studentjoinclass_bus.add_student(current_lop,self.current_user)
        self.current_join = self.studentjoinclass.get_all_class_joined(self.current_user)
        self.changeto_X_page(self.current_page)
    
    def cancel_join(self,current_lop):
        result = messagebox.askyesno("Xác nhận", "Bạn có muốn huỷ lớp này không ?")
        if result:
            messagebox.showinfo('Thông báo','Huỷ thành công!')
            studentjoinclass_bus = studentjoinclassBUS.studentjoinclassBUS()
            studentjoinclass_bus.delete_student(current_lop,self.current_user)
        self.current_join = self.studentjoinclass.get_all_class_joined(self.current_user)
        self.changeto_X_page(self.current_page)

    def filter_my_class(self):
        self.content = [i for i in self.content if i[0] in self.current_join]
        self.changeto_X_page(1)

    def search(self):
        search = self.search_entry.get()
        self.content = [i for i in self.content if search in str(i[1]) or search.lower() in i[2].lower()]
        self.changeto_X_page(1)

    def reset(self):
        self.search_entry.delete(0,'end')
        self.content_frame.focus()
        openclass_BUS = OpenClassBUS.OpenClassBUS()
        self.content = openclass_BUS.get_all_mo()
        self.changeto_X_page(1)

             