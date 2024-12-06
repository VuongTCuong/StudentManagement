import customtkinter as ctk
from tkinter import ttk,messagebox
from BUS import departmentBUS,subjectBUS, OpenClassBUS
from PIL import Image
import datetime
import os
class OpenClass:
    def __init__(self):
        self.root = ctk.CTk()
        self.openclass_bus = OpenClassBUS.OpenClassBUS()

    def create_interactframe(self,frame):
        maml_lab = ctk.CTkLabel(frame,text="Mã mở lớp:")
        maml_lab.place(x=10,y=10)

        self.maml_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã mở lớp",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.maml_entry.place(x=100,y=10)

        mamon_lab = ctk.CTkLabel(frame,text="Mã môn:")
        mamon_lab.place(x=10,y=50)

        self.mamon_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã môn",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.mamon_entry.place(x=100,y=50)
        self.mamon_entry.bind('<FocusOut>',self.set_thongtin_mon)
        tenmon_lab = ctk.CTkLabel(frame,text="Tên Môn:")
        tenmon_lab.place(x=10,y=90)

        self.tenmon_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Vui lòng nhập mã môn trước",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,
            fg_color='#cfe2f3',      
            text_color="#333333",         
            placeholder_text_color="#888888"
        )
        self.tenmon_entry.configure(state='disabled')
        self.tenmon_entry.place(x=100,y=90)

        khoa_lab = ctk.CTkLabel(frame,text="Khoa:")
        khoa_lab.place(x=10,y=130)

        self.khoa_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Vui lòng nhập mã môn trước",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,
            fg_color='#cfe2f3',      
            text_color="#333333",         
            placeholder_text_color="#888888"
        )
        self.khoa_entry.configure(state='disabled')
        self.khoa_entry.place(x=100,y=130)

        sotc_lab = ctk.CTkLabel(frame,text="Số tín chỉ:")
        sotc_lab.place(x=10,y=170)

        self.sotc_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Vui lòng nhập mã môn trước",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,
            fg_color='#cfe2f3',      
            text_color="#333333",         
            placeholder_text_color="#888888"
        )
        self.sotc_entry.configure(state='disabled')
        self.sotc_entry.place(x=100,y=170)

        hocki_lab = ctk.CTkLabel(frame,text='Học kì:')
        hocki_lab.place(x=10,y=210)

        self.hocki_cb = ctk.CTkComboBox(frame,values=['Học kì 1','Học kì 2','Học kì 3'],width=230,state='readonly')
        self.hocki_cb.place(x=100,y=210)
        self.hocki_cb.set('Học kì 1')
        namhoc_lab = ctk.CTkLabel(frame,text='Năm học')
        namhoc_lab.place(x=10,y=250)
        
        self.namhoc_entry = ctk.CTkEntry(
            frame,
            placeholder_text='Nhập năm học',
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="white",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.namhoc_entry.place(x=100,y=250)


        giangvien_lab = ctk.CTkLabel(frame,text='Giảng viên: ')
         
        giangvien_lab.place(x=10,y=290)

        self.giangvien_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập tên giảng viên",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888")
        self.giangvien_entry.place(x=100,y=290)

        siso_lab = ctk.CTkLabel(frame,text='Sỉ số:')
        siso_lab.place(x=10,y=330)

        self.siso_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập sỉ số lớp",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888")
        self.siso_entry.place(x=100,y=330)

        trangthai_lab = ctk.CTkLabel(frame,text='Trạng thái:')
        trangthai_lab.place(x=10,y=370)

        self.trangthai_cb = ctk.CTkComboBox(frame,values=['Mở','Đầy','Đóng'],width=230,state='readonly')
        self.trangthai_cb.place(x=100,y=370)
        self.trangthai_cb.set('Mở')
        #button
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_openclass)
        add_button.place(x=10,y=420)
        
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=420)
        
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_openclass)
        update_button.place(x=200,y=420)
        
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_openclass)
        delete_button.place(x=295,y=420)

    
    def create_tableframe(self,frame):
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        # self.search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập MSSV hoặc tên để tìm kiếm')
        self.search_entry  = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã môn để tìm kiếm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.search_entry.place(x=100,y=10)

        depart_BUS = departmentBUS.departmentBUS()
        all_depart = depart_BUS.get_all_department()
        ten_depart = ["Khoa"]+[str(tenkhoa[0]) for tenkhoa in all_depart]
        self.khoa_cb_filter = ctk.CTkComboBox(frame,width=90,values=ten_depart,state='readonly',command=self.filter_by_khoa)
        self.khoa_cb_filter.place(x=350,y=10)
        self.khoa_cb_filter.set("Khoa")

        self.hocki_cb_filter = ctk.CTkComboBox(frame,width=90,values=['Học kì','Học kì 1','Học kì 2','Học kì 3'],state='readonly',command=self.filter_by_hocki)
        self.hocki_cb_filter.place(x=450,y=10)
        self.hocki_cb_filter.set("Học kì")

        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.searching)
        search_button.place(x=560,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.reset_search)
        reset_button.place(x=670,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=810,height=450)
        scrollbar.place(x=10,y=50)

        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã mở lớp', 'Mã môn', 'Tên môn', 'Khoa', 'Số TC','Học kì' ,'Năm học','Giảng viên','Sỉ số','Trạng thái')
        self.table.heading('Mã mở lớp', text='Mã mở lớp')
        self.table.heading('Mã môn', text='Mã môn')
        self.table.heading('Tên môn', text='Tên môn')
        self.table.heading('Khoa', text='Khoa')
        self.table.heading('Số TC', text='Số TC')
        self.table.heading('Học kì', text='Học kì')
        self.table.heading('Năm học', text='Năm học')
        self.table.heading('Giảng viên', text='Giảng viên')
        self.table.heading('Sỉ số', text='Sỉ số')
        self.table.heading('Trạng thái', text='Trạng thái')

        # Adjust column widths to fit within table_frame
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã mở lớp', width=70)
        self.table.column('Mã môn', width=70)
        self.table.column('Tên môn', width=140)
        self.table.column('Khoa', width=60)
        self.table.column('Số TC', width=60)
        self.table.column('Học kì', width=60)
        self.table.column('Năm học', width=80)
        self.table.column('Giảng viên', width=120)
        self.table.column('Sỉ số', width=60)
        self.table.column('Trạng thái', width=80)
        self.table.pack(side='left')
        self.table.bind('<Button-1>',self.write_all_input)
        self.table.bind('<Double-Button-1>',self.danhsachsv)
        self.write_table()

    def set_thongtin_mon(self,event):
        mamon = self.mamon_entry.get()
        subBUS = subjectBUS.subjectBUS()
        mon_result = subBUS.get_one_subject(mamon)
        if mamon.strip()!='':
            if mon_result:
                self.tenmon_entry.configure(state='normal')
                self.tenmon_entry.delete(0,'end')
                self.tenmon_entry.insert(0,mon_result[1])
                self.tenmon_entry.configure(state='disabled')

                self.khoa_entry.configure(state='normal')
                self.khoa_entry.delete(0,'end')
                self.khoa_entry.insert(0,mon_result[2])
                self.khoa_entry.configure(state='disabled')

                self.sotc_entry.configure(state='normal')
                self.sotc_entry.delete(0,'end')
                self.sotc_entry.insert(0,mon_result[3])
                self.sotc_entry.configure(state='disabled')
            else:
                self.tenmon_entry.configure(state='normal')
                self.tenmon_entry.delete(0,'end')
                self.tenmon_entry.configure(placeholder_text='Không tìm thấy mã môn')
                self.tenmon_entry.configure(state='disabled')

                self.khoa_entry.configure(state='normal')
                self.khoa_entry.delete(0,'end')
                self.khoa_entry.configure(placeholder_text='Không tìm thấy mã môn')
                self.khoa_entry.configure(state='disabled')

                self.sotc_entry.configure(state='normal')
                self.sotc_entry.delete(0,'end')
                self.sotc_entry.configure(placeholder_text='Không tìm thấy mã môn')
                self.sotc_entry.configure(state='disabled')
        else:
            self.tenmon_entry.configure(state='normal')
            self.tenmon_entry.delete(0,'end')
            self.tenmon_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
            self.tenmon_entry.configure(state='disabled')

            self.khoa_entry.configure(state='normal')
            self.khoa_entry.delete(0,'end')
            self.khoa_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
            self.khoa_entry.configure(state='disabled')

            self.sotc_entry.configure(state='normal')
            self.sotc_entry.delete(0,'end')
            self.sotc_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
            self.sotc_entry.configure(state='disabled')
    
    def write_table(self):
        self.table.delete(*self.table.get_children())
        result = self.openclass_bus.get_all()
        for i in result:
            self.table.insert('','end',value=i)
    
    def clear_input(self):
        if self.maml_entry._state=='disabled':
            self.maml_entry.configure(state='normal',fg_color='white')
        self.maml_entry.delete(0,'end')
        self.mamon_entry.delete(0,'end')
        self.tenmon_entry.configure(state='normal')
        self.tenmon_entry.delete(0,'end')
        self.tenmon_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
        self.tenmon_entry.configure(state='disabled')
        self.khoa_entry.configure(state='normal')
        self.khoa_entry.delete(0,'end')
        self.khoa_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
        self.khoa_entry.configure(state='disabled')
        self.sotc_entry.configure(state='normal')
        self.sotc_entry.delete(0,'end')
        self.sotc_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
        self.sotc_entry.configure(state='disabled')
        self.hocki_cb.set('Học kì 1')
        self.namhoc_entry.delete(0,'end')
        self.giangvien_entry.delete(0,'end')
        self.siso_entry.delete(0,'end')
        self.trangthai_cb.set('Mở')

    def write_all_input(self,event):
        clicked_item = self.table.identify('item',event.x,event.y)
        clicked_data = self.table.item(clicked_item)['values']
    
        if clicked_item!='':
            self.clear_input()
            self.maml_entry.insert(0,clicked_data[0])
            self.maml_entry.configure(state='disabled',fg_color='#cfe2f3')
            self.mamon_entry.insert(0,clicked_data[1])
            
            self.tenmon_entry.configure(state='normal')
            self.tenmon_entry.insert(0,clicked_data[2])
            self.tenmon_entry.configure(state='readonly')
            self.khoa_entry.configure(state='normal')
            self.khoa_entry.insert(0,clicked_data[3])
            self.khoa_entry.configure(state='readonly')
            self.sotc_entry.configure(state='normal')
            self.sotc_entry.insert(0,clicked_data[4])
            self.sotc_entry.configure(state='readonly')

            self.hocki_cb.set(clicked_data[5])
            self.namhoc_entry.insert(0,clicked_data[6])
            self.giangvien_entry.insert(0,clicked_data[7])
            self.siso_entry.insert(0,clicked_data[8])
            self.trangthai_cb.set(clicked_data[9])

    def is_valid(self):
        maml = self.maml_entry.get().strip()
        mamon = self.mamon_entry.get().strip()
        giangvien = self.giangvien_entry.get().strip()
        siso = self.siso_entry.get().strip()

        if maml=='' or mamon=='' or giangvien=='' or siso=='':
            return False,'Vui lòng nhập đầy đủ thông tin'
        if not maml.isdigit():
            return False,'Mã mở lớp chỉ nhập số nguyên'
        if not mamon.isdigit():
            return False,'Mã môn chỉ nhập số nguyên'
        
        if any(not char.isalnum() for char in giangvien.replace(" ","")):
            return False, "Tên giảng viên không chứa ký tự đặc biệt"
        if any(char.isdigit() for char in giangvien):
            return False, "Tên giảng viên chỉ nhập ký tự"
        
        if not siso.isdigit():
            return False, "Sỉ số chỉ nhập số nguyên"
        return True,' thành công'

    def add_openclass(self):
        maml = self.maml_entry.get()
        mamon = self.mamon_entry.get()
        hocki = self.hocki_cb.get()
        namhoc = self.namhoc_entry.get()
        giangvien = self.giangvien_entry.get()
        siso = self.siso_entry.get()
        trangthai = self.trangthai_cb.get()
        subBUS = subjectBUS.subjectBUS()
        is_valid, message = self.is_valid()
        if is_valid:
            if subBUS.get_subject_by_id(mamon) is not None:
                if self.openclass_bus.add_OpenClass(maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
                    self.clear_input()
                    self.write_table()
                    messagebox.showinfo('Success','Thêm'+message)
            else: messagebox.showerror('Error','Không tìm thấy mã môn học')
        else: messagebox.showerror('Error',message)

    def update_openclass(self):
        maml = self.maml_entry.get()
        mamon = self.mamon_entry.get()
        hocki = self.hocki_cb.get()
        namhoc = self.namhoc_entry.get()
        giangvien = self.giangvien_entry.get()
        siso = self.siso_entry.get()
        trangthai = self.trangthai_cb.get()
        
        is_valid, message = self.is_valid()
        subBUS = subjectBUS.subjectBUS()
        if is_valid:
            if subBUS.get_subject_by_id(mamon) is not None:
                if self.openclass_bus.update_OpenClass(maml,mamon,hocki,namhoc,giangvien,siso,trangthai):
                    self.clear_input()
                    self.write_table()
                    messagebox.showinfo('Success','Cập nhật'+message)
            else: messagebox.showerror('Error','Không tìm thấy mã môn học')
        else:
            messagebox.showerror('Error',message)

    def delete_openclass(self):
        maml = self.maml_entry.get()
        if self.openclass_bus.delete_OpenClass(maml):
            self.clear_input()
            self.write_table()
            messagebox.showinfo('Success','Xoá thành công')
        else: messagebox.showerror('Error','Không tìm thấy mã mở lớp')

    def searching(self):
        search_text = self.search_entry.get()
        khoa = self.khoa_cb_filter.get()
        hocki = self.hocki_cb_filter.get()

        self.table.delete(*self.table.get_children())
        filter_result = self.openclass_bus.filter(khoa,hocki)
        for i in filter_result:
            if search_text.lower() in str(i[1]):
                self.table.insert('','end',value=i)

    def filter_by_khoa(self,selected_khoa):
        selected_hocki = self.hocki_cb_filter.get()
        
        self.table.delete(*self.table.get_children())
        search_text = self.search_entry.get()
        filter_result = self.openclass_bus.filter(selected_khoa,selected_hocki)

        for i in filter_result:
            if search_text.lower() in str(i[1]):
                self.table.insert('','end',value=i)

    def filter_by_hocki(self,selected_hocki):
        selected_khoa = self.khoa_cb_filter.get()
        
        self.table.delete(*self.table.get_children())
        search_text = self.search_entry.get()
        filter_result = self.openclass_bus.filter(selected_khoa,selected_hocki)
        for i in filter_result:
            if search_text.lower() in str(i[1]):
                self.table.insert('','end',value=i)

    def reset_search(self):
        self.search_entry.delete(0,'end')
        self.khoa_cb_filter.set('Khoa')
        self.hocki_cb_filter.set('Học kì')
        self.table.delete(*self.table.get_children())
        self.write_table()

    def danhsachsv(self,event):
        clicked_item = self.table.identify('item',event.x,event.y)
        clicked_data = self.table.item(clicked_item)['values']
        if clicked_data:
            scroll_frame = ctk.CTkScrollableFrame(self.root,width=750,height=500,fg_color='#fdfdc9')
            scroll_frame.place(x=300,y=50)
            header = ctk.CTkLabel(scroll_frame,text='Danh sách sinh viên của lớp: '+str(clicked_data[0]),font=('Roboto',17,'bold'))
            header.pack()

            table = ttk.Treeview(scroll_frame,height=23,)
            table['columns'] = ('Mã SV', 'Họ Tên', 'Năm Sinh', 'Giới Tính', 'Email','Mã Khoa' ,'Tên Lớp')
            table.heading('Mã SV', text='Mã SV')
            table.heading('Họ Tên', text='Họ Tên')
            table.heading('Năm Sinh', text='Năm Sinh')
            table.heading('Giới Tính', text='Giới Tính')
            table.heading('Email', text='Email')
            table.heading('Mã Khoa', text='Mã Khoa')
            table.heading('Tên Lớp', text='Tên Lớp')

            # Adjust column widths to fit within table_frame
            table.column("#0", width=0, stretch=ctk.NO)
            table.column('Mã SV', width=80)
            table.column('Họ Tên', width=140)
            table.column('Năm Sinh', width=100)
            table.column('Giới Tính', width=70)
            table.column('Email', width=150)
            table.column('Mã Khoa', width=60)
            table.column('Tên Lớp', width=100)
            table.pack()

            all_sv = self.openclass_bus.get_sv_by_malop(clicked_data[0])
            print(all_sv)
            for i in all_sv:
                table.insert('','end',value=i)
            red_x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "red_x.png"))
            red_x_icon_ctk = ctk.CTkImage(light_image=red_x_icon,dark_image=red_x_icon,size=(15,15))
            black_x_icon = Image.open(os.path.join(os.path.dirname(__file__), "assets", "black_x.png"))
            black_x_icon_ctk = ctk.CTkImage(light_image=black_x_icon,dark_image=black_x_icon,size=(15,15))
            close_button = ctk.CTkButton(scroll_frame,
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
                                        command=lambda: scroll_frame.place_forget())
            self.root.bind('<Escape>',lambda e: scroll_frame.place_forget())
            
                    
            close_button.bind('<Enter>',lambda e: close_button.configure(image=black_x_icon_ctk,text_color='black',fg_color='#ff4a5d'))
            close_button.bind('<Leave>',lambda e: close_button.configure(image=red_x_icon_ctk,text_color='#ff4a5d',fg_color='transparent'))
            close_button.pack(anchor='ne',padx=50,pady=20)
