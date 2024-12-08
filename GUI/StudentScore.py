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
        main_canvas.delete('draw')
        chitiet_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "info.png"))
        chitiet_icon_ctk = ctk.CTkImage(light_image=chitiet_icon,dark_image=chitiet_icon,size=(20,20))
        zoomed_chitiet_icon_ctk = ctk.CTkImage(light_image=chitiet_icon,dark_image=chitiet_icon,size=(25,25))
        
        chitiet_button = dict()
        xuat_diemtb=True
        for i in main_canvas.winfo_children():
            if(type(i)!=ctk.CTkComboBox):
                i.destroy()
        dtb_he4_value = 0
        dtb_he10_value = 0
        sotc_hk_value = 0 
        
        for i in range(0,len(self.bangdiem)):
            main_canvas.create_line((10,140+i*40,10,180+i*40),fill='#348cd4',tags='draw')
            lab = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][0],font=('Roboto',14))
            lab.place(x=20,y=145+i*40)
            main_canvas.create_line((80,140+i*40,80,180+i*40),fill='#348cd4',tags='draw')
            lab1 = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][1],font=('Roboto',14))
            lab1.place(x=85,y=145+i*40)
            main_canvas.create_line((350,140+i*40,350,180+i*40),fill='#348cd4',tags='draw')
            lab2 = ctk.CTkLabel(main_canvas,text=self.bangdiem[i][2],font=('Roboto',14))
            lab2.place(x=375,y=145+i*40)
            main_canvas.create_line((410,140+i*40,410,180+i*40),fill='#348cd4',tags='draw')

            if self.bangdiem[i][3]!='' and self.bangdiem[i][4]!='':
                dtk_he10 = round((float(self.bangdiem[i][3])+float(self.bangdiem[i][4]))/2+0000000000.1,1)
            else: 
                dtk_he10=''
                xuat_diemtb = False
            lab3 = ctk.CTkLabel(main_canvas,text=str(dtk_he10),font=('Roboto',14))
            lab3.place(x=450,y=145+i*40)
            main_canvas.create_line((510,140+i*40,510,180+i*40),fill='#348cd4',tags='draw')

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
            main_canvas.create_line((610,140+i*40,610,180+i*40),fill='#348cd4',tags='draw')
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
            main_canvas.create_line((710,140+i*40,710,180+i*40),fill='#348cd4',tags='draw')
    
            if dtk_c=='F' or dtk_c=='':
                x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "blue_x.png"))
                kq_icon_ctk = ctk.CTkImage(light_image=x_icon,dark_image=x_icon,size=(17,17))
            else: 
                x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "blue_tick.png"))
                kq_icon_ctk = ctk.CTkImage(light_image=x_icon,dark_image=x_icon,size=(20,20))
    
            lab6 = ctk.CTkLabel(main_canvas,text='',image=kq_icon_ctk)
            lab6.place(x=739,y=145+i*40)
            main_canvas.create_line((780,140+i*40,780,180+i*40),fill='#348cd4',tags='draw')
            
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
            main_canvas.create_line((860,140+i*40,860,180+i*40),fill='#348cd4',tags='draw')
            main_canvas.create_line((10,180+i*40,860,180+i*40),fill='#348cd4',tags='draw')

            #tính điểm dtb các hệ khi các môn đủ điểm
            if xuat_diemtb:
                dtb_he4_value += dtk_he_4*int(self.bangdiem[i][2])
                dtb_he10_value += dtk_he10*int(self.bangdiem[i][2])
                sotc_hk_value += int(self.bangdiem[i][2])

            
        dtb_he4 = ctk.CTkLabel(main_canvas,text='- Điểm trung bình học kỳ hệ 4:',text_color='#2288aa',font=('Roboto',15))
        dtb_he4.place(x=10,y=160+40*len(self.bangdiem))
        dtb_he10 = ctk.CTkLabel(main_canvas,text='- Điểm trung bình học kỳ hệ 10:',text_color='#2288aa',font=('Roboto',15))
        dtb_he10.place(x=10,y=200+40*len(self.bangdiem))
        sotc_hk = ctk.CTkLabel(main_canvas,text='- Số tín chỉ đạt học kỳ:',text_color='#2288aa',font=('Roboto',15))
        sotc_hk.place(x=10,y=240+40*len(self.bangdiem))
        dtb_tichluy_he4 = ctk.CTkLabel(main_canvas,text='- Điểm trung bình tích luỹ hệ 4:',text_color='#2288aa',font=('Roboto',15))
        dtb_tichluy_he4.place(x=500,y=160+40*len(self.bangdiem))
        dtb_tichluy_he10 = ctk.CTkLabel(main_canvas,text='- Điểm trung bình tích luỹ hệ 10:',text_color='#2288aa',font=('Roboto',15))
        dtb_tichluy_he10.place(x=500,y=200+40*len(self.bangdiem))
        sotc_tichluy = ctk.CTkLabel(main_canvas,text='- Số tín chỉ tích luỹ:',text_color='#2288aa',font=('Roboto',15))
        sotc_tichluy.place(x=500,y=240+40*len(self.bangdiem))

        whole_score = self.studentscore.get_whole_score(self.current_user)
        dtb_tichluy_he4_value = 0
        dtb_tichluy_he10_value = 0
        sotc_tichluy_value = 0
        for i in whole_score:
            sotc_tichluy_value += int(i[1])
            dtb_tichluy_he10_value += float(i[2])*int(i[1])
            dtb_tichluy_he4_value += float(i[3])*int(i[1])

        dtb_tichluy_he4_value = round(dtb_tichluy_he4_value/sotc_tichluy_value,2)
        dtb_tichluy_he10_value = round(dtb_tichluy_he10_value/sotc_tichluy_value,2)

        if xuat_diemtb:
            dtb_he4_value = round(dtb_he4_value/sotc_hk_value,2)
            dtb_he10_value = round(dtb_he10_value/sotc_hk_value,2)
            dtb_he4_value_lab = ctk.CTkLabel(main_canvas,text=str(dtb_he4_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            dtb_he4_value_lab.place(x=250,y=160+40*len(self.bangdiem))
            dtb_he10_value_lab = ctk.CTkLabel(main_canvas,text=str(dtb_he10_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            dtb_he10_value_lab.place(x=250,y=200+40*len(self.bangdiem))
            sotc_hk_value_lab = ctk.CTkLabel(main_canvas,text=str(sotc_hk_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            sotc_hk_value_lab.place(x=250,y=240+40*len(self.bangdiem))
            dtb_tichluy_he4_value_lab = ctk.CTkLabel(main_canvas,text=str(dtb_tichluy_he4_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            dtb_tichluy_he4_value_lab.place(x=750,y=160+40*len(self.bangdiem))
            dtb_tichluy_he10_value_lab = ctk.CTkLabel(main_canvas,text=str(dtb_tichluy_he10_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            dtb_tichluy_he10_value_lab.place(x=750,y=200+40*len(self.bangdiem))
            sotc_tichluy_value_lab = ctk.CTkLabel(main_canvas,text=str(sotc_tichluy_value),text_color='#2288aa',font=('Roboto',15,'bold'))
            sotc_tichluy_value_lab.place(x=750,y=240+40*len(self.bangdiem))

        
    def chitiet_canvas(self,main_canvas,mon):
        chitiet_canvas = ctk.CTkCanvas(main_canvas,width=500,height=200,bg='white')
        chitiet_canvas.place(x=200,y=220)
        
        tenmon_lab = ctk.CTkLabel(chitiet_canvas,text=mon[1],text_color='#02578a',font=('Roboto',16,'bold'))
        tenmon_lab.place(x=10,y=10)
        chitiet_canvas.create_rectangle((0,40,510,80),fill='#07689f',outline='white')
        chitiet_canvas.create_text((68,60),text='Tên thành phần',fill='white',font=('Roboto 11 bold'))
        chitiet_canvas.create_line((150,40,150,150),fill='#e0e1e2')

        chitiet_canvas.create_text((250,60),text='Trọng số (%)',fill='white',font=('Roboto 11 bold'))
        chitiet_canvas.create_line((340,40,340,150),fill='#e0e1e2')

        chitiet_canvas.create_text((420,60),text='Điểm thành phần',fill='white',font=('Roboto 11 bold'))
        
        thanhphan_1 = ctk.CTkLabel(chitiet_canvas,text='Kiểm tra',font=('Roboto',15))
        thanhphan_1.place(x=11,y=80)

        thanhphan_2 = ctk.CTkLabel(chitiet_canvas,text='Điểm thi',font=('Roboto',15))
        thanhphan_2.place(x=11,y=120)

        trongso = ctk.CTkLabel(chitiet_canvas,text='50',font=('Roboto',15))
        trongso.place(x=235,y=80)

        trongso = ctk.CTkLabel(chitiet_canvas,text='50',font=('Roboto',15))
        trongso.place(x=235,y=120)
        diemtp_1 = ctk.CTkLabel(chitiet_canvas,text=str(mon[3]),font=('Roboto',15))
        diemtp_1.place(x=415,y=80)
        diemtp_2 = ctk.CTkLabel(chitiet_canvas,text=str(mon[4]),font=('Roboto',15))
        diemtp_2.place(x=415,y=120)

        chitiet_canvas.create_line((0,115,510,115),fill='#e0e1e2')
        chitiet_canvas.create_line((0,150,510,150),fill='#e0e1e2')
        red_x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "red_x.png"))
        red_x_icon_ctk = ctk.CTkImage(light_image=red_x_icon,dark_image=red_x_icon,size=(15,15))
        black_x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "black_x.png"))
        black_x_icon_ctk = ctk.CTkImage(light_image=black_x_icon,dark_image=black_x_icon,size=(15,15))
        close_button = ctk.CTkButton(chitiet_canvas,
                                     text='Đóng',
                                     width=60,
                                     height=30,
                                     image=red_x_icon_ctk,
                                     text_color='#ff4a5d',
                                     corner_radius=5,
                                     border_color='#ff4a5d',
                                     border_width=1.5,
                                     fg_color='transparent',
                                     font=('Roboto',16),
                                     command=lambda : chitiet_canvas.destroy())
        close_button.bind('<Enter>',lambda e: close_button.configure(image=black_x_icon_ctk,text_color='black',fg_color='#ff4a5d'))
        close_button.bind('<Leave>',lambda e: close_button.configure(image=red_x_icon_ctk,text_color='#ff4a5d',fg_color='transparent'))
        close_button.place(x=425,y=165)


        