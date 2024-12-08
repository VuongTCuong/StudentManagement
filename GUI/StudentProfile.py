import customtkinter as ctk
from PIL import Image
import os
from cryptography.fernet import Fernet
from BUS import studentBUS,studentjoinclassBUS,StudentScoreBUS
class StudentProfile:
    def __init__(self):
        self.root = ctk.CTk()
    
        self.studentjoinclass = studentjoinclassBUS.studentjoinclassBUS()
        self.studentscore = StudentScoreBUS.StudentScoreBUS()
    def create_maincanvas(self,main_canvas):
        main_canvas.create_rectangle((0,0,870,40),fill='#d2cfcf')
        main_canvas.create_text((89,22),text='Thông tin sinh viên',fill='#02578a',font=('Roboto 13 bold'))
        main_canvas.create_line((0,40,870,40),fill='#b8bec9')

        if os.path.exists('user.txt'):
            f = Fernet(b'LkQhEOBncRePoyysixPYu-I2Q-uDd-UZH18e8M2_HJE=')
            user_file = open('user.txt','rb')
            username = user_file.readline()
            username = f.decrypt(username).decode()

        student_bus = studentBUS.studentBUS()
        student = student_bus.get_one_student(username)
        self.current_user=username
        masv_lab = ctk.CTkLabel(main_canvas,text='Mã sinh viên:',font=('Roboto',16,'bold'))
        masv_lab.place(x=10,y=50)
        masv_result_lab = ctk.CTkLabel(main_canvas,text=student[0],font=('Roboto',16))
        masv_result_lab.place(x=180,y=50)

        hoten_lab = ctk.CTkLabel(main_canvas,text='Họ và tên:',font=('Roboto',16,'bold'))
        hoten_lab.place(x=10,y=85)
        hoten_result_lab = ctk.CTkLabel(main_canvas,text=student[1],font=('Roboto',16))
        hoten_result_lab.place(x=180,y=85)

        namsinh_lab = ctk.CTkLabel(main_canvas,text='Ngày sinh:',font=('Roboto',16,'bold'))
        namsinh_lab.place(x=10,y=120)
        namsinh_result_lab = ctk.CTkLabel(main_canvas,text=student[2],font=('Roboto',16))
        namsinh_result_lab.place(x=180,y=120)

        gioitinh_lab = ctk.CTkLabel(main_canvas,text='Giới tính:',font=('Roboto',16,'bold'))
        gioitinh_lab.place(x=10,y=155)
        gioitinh_result_lab = ctk.CTkLabel(main_canvas,text=student[3],font=('Roboto',16))
        gioitinh_result_lab.place(x=180,y=155)

        email_lab = ctk.CTkLabel(main_canvas,text='Email:',font=('Roboto',16,'bold'))
        email_lab.place(x=450,y=50)
        email_result_lab = ctk.CTkLabel(main_canvas,text=student[4],font=('Roboto',16))
        email_result_lab.place(x=600,y=50)

        khoa_lab = ctk.CTkLabel(main_canvas,text='Khoa:',font=('Roboto',16,'bold'))
        khoa_lab.place(x=450,y=85)
        khoa_result_lab = ctk.CTkLabel(main_canvas,text=student[5],font=('Roboto',16))
        khoa_result_lab.place(x=600,y=85)

        lop_lab = ctk.CTkLabel(main_canvas,text='Lớp:',font=('Roboto',16,'bold'))
        lop_lab.place(x=450,y=120)  
        lop_result_lab = ctk.CTkLabel(main_canvas,text=student[6],font=('Roboto',16))
        lop_result_lab.place(x=600,y=120)
        
        #main_canvas.create_rectangle((680,50,820,220),outline='black')
        #biểu đồ điểm
        self.chart_canvas = ctk.CTkCanvas(main_canvas,width=845,height=370,bg='white',highlightcolor='#ebebeb')
        self.chart_canvas.place(x=10,y=200)
        #2596be
        self.chart_canvas.create_text((70,20),text='Kết quả học tập',fill='#02578a',font=('Roboto 13'))
        

        hocki_namhoc_join = self.studentjoinclass.get_hocki_namhoc_joined(username)
        print(hocki_namhoc_join)
        thoigian_value = ["Học kì {0} - Năm học {1} - {2}".format(i[0],i[1],i[2]) for i in hocki_namhoc_join]
        thoigian_cb = ctk.CTkComboBox(self.chart_canvas,values=thoigian_value,width=270,height=30,font=('Roboto',15),state='readonly',command=lambda s:self.set_chartdiem(s))
        thoigian_cb.place(x=180,y=8)
        thoigian_cb.set(thoigian_value[0])
        hk = 'Học kì {0}'.format(hocki_namhoc_join[0][0])
        namhoc = 'Năm học {0} - {1}'.format(hocki_namhoc_join[0][1],hocki_namhoc_join[0][2])
        self.bangdiem = self.studentscore.get_score_info(self.current_user,hk,namhoc)
        self.set_chartdiem(thoigian_cb.get())
    def set_chartdiem(self,selection):
        hocki = selection[0:8]
        namhoc = selection[19:]
        for i in range(len(self.bangdiem)):
            self.chart_canvas.delete('r'+str(i))
        self.bangdiem = self.studentscore.get_score_info(self.current_user,hocki,namhoc)
        for child in self.chart_canvas.winfo_children():
            if type(child)!=ctk.CTkComboBox:
                child.destroy()
        for i in range(0,11,2):
            lab = ctk.CTkLabel(self.chart_canvas,text=str(i))
            lab.place(x=10,y=320-i*26)
            self.chart_canvas.create_line((30,335-i*26,825,335-i*26),fill='#d6d3d3')
    
        for i in self.bangdiem:
            if i[4]=='':
                return
        
        for i,val in enumerate(self.bangdiem):
            lab = ctk.CTkLabel(self.chart_canvas,text=val[0])
            lab.place(x=60+i*85,y=345)
            self.chart_canvas.create_rectangle((60+i*85,335,100+i*85,335),fill='#287cfc',tags='r'+str(i),outline='white')
            self.chart_canvas.tag_bind('r'+str(i),'<Enter>',lambda e,x=i: self.hover_chart(x))
            self.chart_canvas.tag_bind('r'+str(i),'<Leave>',lambda e,x=i: self.out_hover_chart(x))
        #draw
        def increase(tag):
            coords = self.chart_canvas.coords(tag)
            self.chart_canvas.coords(tag,(coords[0],coords[1]-6,coords[2],coords[3]))
            dtb = round((self.bangdiem[int(tag[1:])][3]+self.bangdiem[int(tag[1:])][4])/2+00000000.1,1)
            if coords[1]>335-dtb*2/0.1-15:
                self.root.after(10, increase,tag)
            else:
                self.root.after(10,decrease,tag)
        def decrease(tag):
            coords = self.chart_canvas.coords(tag)
            self.chart_canvas.coords(tag,(coords[0],coords[1]+1,coords[2],coords[3]))
            dtb = round((self.bangdiem[int(tag[1:])][3]+self.bangdiem[int(tag[1:])][4])/2+00000000.1,1)
            if coords[1]<(335-dtb*2/0.1)-1:
                self.root.after(10,decrease,tag)

        fading_colors = ['#FFF','#EEE','#DDD','#CCC','#BBB','#AAA','#999','#888','#777','#666','#555','#444','#333','#222','#111','#000']
        def show(color_index,lab):
            if color_index<len(fading_colors):
                lab.configure(text_color=fading_colors[color_index])
                self.root.after(20,show,color_index+1,lab)
        
        def score(i):
            if i<len(self.bangdiem):
                dtb = round((self.bangdiem[i][3]+self.bangdiem[i][4])/2+00000000.1,1)
                lab = ctk.CTkLabel(self.chart_canvas,text=str(dtb),height=10,font=('Roboto',13,'bold'),fg_color='transparent',text_color='#FFF')
                lab.place(x=70+i*85,y=315-dtb*2/0.1)
                show(0,lab)
                self.root.after(60,score,i+1)
        def draw(i):
            if i<len(self.bangdiem):
                coords = self.chart_canvas.coords('r'+str(i))
                self.chart_canvas.coords('r'+str(i),(coords[0],335,coords[2],coords[3]))
                increase('r'+str(i))
                self.root.after(80,draw,i+1)
            else:
                self.root.after(800,score,0)
        draw(0)
    
    def hover_chart(self,i):
        self.chart_canvas.itemconfig('r'+str(i),fill='#78a4fc')
        left_hover = round((len(self.bangdiem))/2+0000000.1,0)-1
        hover_color = ['#C8A8E9','#CFE1B9','#F6BCBA','#FFBB94','#C3C7F4','#09D1C7']
        dtb = round((self.bangdiem[i][3]+self.bangdiem[i][4])/2+00000000.1,1)
        if i>6:
            color = hover_color[i%6]
        else:
            color = hover_color[i]
        self.hover_detail = ctk.CTkFrame(self.chart_canvas,fg_color=color,corner_radius=10,bg_color='transparent')
        if i<=3:
            self.hover_detail.place(x=120+i*85,y=(335-dtb*2/0.1)-100)
        else:
            self.hover_detail.place(x=60+i*85-(114+6*len(self.bangdiem[i][1])),y=(335-dtb*2/0.1)-100)
        lab = ctk.CTkLabel(self.hover_detail,text='Mã môn học:',font=('Roboto',13,'bold'))
        lab.grid(row=0,column=0,sticky='nw',padx=15)
        lab1 = ctk.CTkLabel(self.hover_detail,text='Tên môn học:',font=('Roboto',13,'bold'))
        lab1.grid(row=1,column=0,sticky='nw',padx=15)
        lab2 = ctk.CTkLabel(self.hover_detail,text='Số tín chỉ:',font=('Roboto',13,'bold'))
        lab2.grid(row=2,column=0,sticky='nw',padx=15)
        lab3 = ctk.CTkLabel(self.hover_detail,text='Điểm:',font=('Roboto',13,'bold'))
        lab3.grid(row=3,column=0,sticky='nw',padx=15)

        lab4 = ctk.CTkLabel(self.hover_detail,text=self.bangdiem[i][0],font=('Roboto',13))
        lab4.grid(row=0,column=1,sticky='nw',padx=5)
        lab5 = ctk.CTkLabel(self.hover_detail,text=self.bangdiem[i][1],font=('Roboto',13))
        lab5.grid(row=1,column=1,sticky='nw',padx=5)
        lab6 = ctk.CTkLabel(self.hover_detail,text=self.bangdiem[i][2],font=('Roboto',13))
        lab6.grid(row=2,column=1,sticky='nw',padx=5)
        lab7 = ctk.CTkLabel(self.hover_detail,text=str(dtb),font=('Roboto',13))
        lab7.grid(row=3,column=1,sticky='nw',padx=5)
   
    
    def out_hover_chart(self,i):
        self.chart_canvas.itemconfig('r'+str(i),fill='#287cfc')
        self.hover_detail.destroy()