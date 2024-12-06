import customtkinter as ctk
from BUS import studentjoinclassBUS,StudentScoreBUS
import os
from PIL import Image
class StudentScore:
    def __init__(self):
        self.root = ctk.CTk()
        self.current_user = ''
        self.studentjoinclass = studentjoinclassBUS.studentjoinclassBUS()
        self.studentscore = StudentScoreBUS.StudentScoreBUS()
    def create_maincanvas(self,main_canvas):
    
        main_canvas.create_rectangle((0,0,870,40),fill='#d2cfcf')
        main_canvas.create_text((52,22),text='Xem điểm',fill='#02578a',font=('Roboto 13 bold'))
        main_canvas.create_line((0,40,870,40),fill='#b8bec9')
        hocki_namhoc_join = self.studentjoinclass.get_hocki_namhoc_joined(self.current_user)
        
        thoigian_value = ["Học kì {0} - Năm học {1} - {2}".format(i[0],i[1],i[2]) for i in hocki_namhoc_join]
        thoigian_cb = ctk.CTkComboBox(main_canvas,values=thoigian_value,width=270,height=30,font=('Roboto',15),state='readonly',command=lambda s,canvas=main_canvas:self.set_bangdiem(s,canvas))
        thoigian_cb.place(x=10,y=50)
        thoigian_cb.set(thoigian_value[0])

        #draw header
        main_canvas.create_rectangle((10,100,860,140),fill='#2781af',outline='#dbdbdb')

        main_canvas.create_line((10,100,10,140),fill='white')
        main_canvas.create_text((45,120),text='Mã MH',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((80,100,80,140),fill='white')
        
        main_canvas.create_text((215,120),text='Tên môn học',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((350,100,350,140),fill='white')
        
        main_canvas.create_text((380,120),text='Số TC',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((410,100,410,140),fill='white')

        main_canvas.create_text((460,120),text='Điểm TK\n   (10)',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((510,100,510,140),fill='white')

        main_canvas.create_text((560,120),text='Điểm TK\n    (4)',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((610,100,610,140),fill='white')

        main_canvas.create_text((660,120),text='Điểm TK\n    (C)',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((710,100,710,140),fill='white')

        main_canvas.create_text((745,120),text='Kết quả',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((780,100,780,140),fill='white')
   
        main_canvas.create_text((819,120),text='Chi tiết',fill='white',font=('Roboto 11 bold'))
        main_canvas.create_line((860,100,860,140),fill='white')

        self.set_bangdiem(thoigian_cb.get(),main_canvas)
       
    def set_bangdiem(self,selection,main_canvas):
        hocki = selection[0:8]
        namhoc = selection[19:]
        self.bangdiem = self.studentscore.get_score_info(self.current_user,hocki,namhoc)
        print(self.bangdiem)
        chitiet_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "info.png"))
        chitiet_icon_ctk = ctk.CTkImage(light_image=chitiet_icon,dark_image=chitiet_icon,size=(20,20))
        zoomed_chitiet_icon_ctk = ctk.CTkImage(light_image=chitiet_icon,dark_image=chitiet_icon,size=(25,25))
        
        chitiet_button = dict()

        for i in main_canvas.winfo_children():
            if(type(i)!=ctk.CTkComboBox):
                i.destroy()
        for i in range(0,len(self.bangdiem)):
            main_canvas.create_line((10,140+i*40,10,180+i*40),fill='#348cd4')
            lab = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][0],font=('Roboto',14))
            lab.place(x=20,y=145+i*40)
            main_canvas.create_line((80,140+i*40,80,180+i*40),fill='#348cd4')
            lab1 = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][1],font=('Roboto',14))
            lab1.place(x=85,y=145+i*40)
            main_canvas.create_line((350,140+i*40,350,180+i*40),fill='#348cd4')
            lab2 = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][2],font=('Roboto',14))
            lab2.place(x=375,y=145+i*40)
            main_canvas.create_line((410,140+i*40,410,180+i*40),fill='#348cd4')

            if self.bangdiem[i][3]!='' and self.bangdiem[i][4]!='':
                dtk_he10 = round((float(self.bangdiem[i][3])+float(self.bangdiem[i][4]))/2,1)
            else: dtk_he10=''
            lab3 = ctk.CTkLabel(main_canvas,text=str(dtk_he10),font=('Roboto',14))
            lab3.place(x=450,y=145+i*40)
            main_canvas.create_line((510,140+i*40,510,180+i*40),fill='#348cd4')

            if dtk_he10!='':
                if float(dtk_he10)>=8.5:
                    dtk_he_4 = 4.0
                elif float(dtk_he10)>=7.0:
                    dtk_he_4 = 3.0
                elif float(dtk_he10)>=5.5:
                    dtk_he_4 = 2.0
                elif float(dtk_he10)>=4.0:
                    dtk_he_4 = 1.0
                else: dtk_he_4 = 0.0
            else: dtk_he_4=''
            lab4 = ctk.CTkLabel(main_canvas,text=str(dtk_he_4),font=('Roboto',14))
            lab4.place(x=550,y=145+i*40)
            main_canvas.create_line((610,140+i*40,610,180+i*40),fill='#348cd4')
            if dtk_he_4!='':
                if float(dtk_he_4)==4.0:
                    dtk_c = 'A'
                elif float(dtk_he_4)==3.0:
                    dtk_c = 'B'
                elif float(dtk_he_4)==2.0:
                    dtk_c = 'C'
                elif float(dtk_he_4)==1.0:
                    dtk_c = 'D'
                else: dtk_c = 'F'
            else: dtk_c=''
            lab5 = ctk.CTkLabel(main_canvas,text=dtk_c ,font=('Roboto',14))
            lab5.place(x=655,y=145+i*40)
            main_canvas.create_line((710,140+i*40,710,180+i*40),fill='#348cd4')
    
            if dtk_c=='F' or dtk_c=='':
                x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "blue_x.png"))
                kq_icon_ctk = ctk.CTkImage(light_image=x_icon,dark_image=x_icon,size=(17,17))
            else: 
                x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "blue_tick.png"))
                kq_icon_ctk = ctk.CTkImage(light_image=x_icon,dark_image=x_icon,size=(20,20))
    
            lab6 = ctk.CTkLabel(main_canvas,text='',image=kq_icon_ctk)
            lab6.place(x=739,y=145+i*40)
            main_canvas.create_line((780,140+i*40,780,180+i*40),fill='#348cd4')
            
            chitiet_button[self.bangdiem[i][0]] = ctk.CTkButton(main_canvas,text='',
                                 image=chitiet_icon_ctk,
                                 width=20,
                                 height=20,
                                 fg_color='transparent',
                                 hover_color='#dbdbdb',
                                 command=lambda y=main_canvas,x=self.bangdiem[i]: self.chitiet_canvas(y,x))
            chitiet_button[self.bangdiem[i][0]].place(x=802,y=145+i*40)
            chitiet_button[self.bangdiem[i][0]].bind('<Enter>',lambda e,x=self.bangdiem[i][0]: chitiet_button[x].configure(image=zoomed_chitiet_icon_ctk))
            chitiet_button[self.bangdiem[i][0]].bind('<Leave>',lambda e,x=self.bangdiem[i][0]: chitiet_button[x].configure(image=chitiet_icon_ctk))
            main_canvas.create_line((860,140+i*40,860,180+i*40),fill='#348cd4')
            main_canvas.create_line((10,180+i*40,860,180+i*40),fill='#348cd4')
    def chitiet_canvas(self,main_canvas,mon):
        chitiet_canvas = ctk.CTkCanvas(main_canvas,width=500,height=180,bg='white')
        chitiet_canvas.place(x=200,y=220)
        
        tenmon_lab = ctk.CTkLabel(chitiet_canvas,text=mon[1],text_color='#02578a',font=('Roboto',16,'bold'))
        tenmon_lab.place(x=10,y=10)

        chitiet_canvas.create_text((68,50),text='Tên thành phần',fill='black',font=('Roboto 11 bold'))
        chitiet_canvas.create_text((250,50),text='Trọng số (%)',fill='black',font=('Roboto 11 bold'))
        chitiet_canvas.create_text((420,50),text='Điểm thành phần',fill='black',font=('Roboto 11 bold'))

        thanhphan_1 = ctk.CTkLabel(chitiet_canvas,text='Kiểm tra',font=('Roboto',15))
        thanhphan_1.place(x=11,y=70)

        thanhphan_2 = ctk.CTkLabel(chitiet_canvas,text='Điểm thi',font=('Roboto',15))
        thanhphan_2.place(x=11,y=110)

        trongso = ctk.CTkLabel(chitiet_canvas,text='50',font=('Roboto',15))
        trongso.place(x=235,y=70)

        trongso = ctk.CTkLabel(chitiet_canvas,text='50',font=('Roboto',15))
        trongso.place(x=235,y=110)
        diemtp_1 = ctk.CTkLabel(chitiet_canvas,text=str(mon[3]),font=('Roboto',15))
        diemtp_1.place(x=415,y=70)
        diemtp_2 = ctk.CTkLabel(chitiet_canvas,text=str(mon[4]),font=('Roboto',15))
        diemtp_2.place(x=415,y=110)
        close_button = ctk.CTkButton(chitiet_canvas,
                                     text='Đóng',
                                     width=60,
                                     height=30,
                                     text_color='red',
                                     corner_radius=5,
                                     
                                     command=lambda : chitiet_canvas.destroy())
        close_button.place(x=430,y=145)


        