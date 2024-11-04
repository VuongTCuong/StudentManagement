import customtkinter as ctk
from tkinter import ttk,messagebox
from datetime import datetime
from BUS import classBUS,studentBUS
from DTO import studentDTO
from RegisterGUI import RegisterGUI
class StudentMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Student Management System - Student Management") 
        self.studentBUS = studentBUS.studentBUS()
        
    def create_interactframe(self,frame):
        #student form   
        msv_lab = ctk.CTkLabel(frame,text="Mã SV:")
        msv_lab.place(x=10,y=10)
        # self.msv_entry = ctk.CTkEntry(frame,width=230)
        self.msv_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập MSSV",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.msv_entry.place(x=100,y=10)

        hoten_lab = ctk.CTkLabel(frame,text="Họ Tên:")
        hoten_lab.place(x=10,y=50)
        # self.hoten_entry = ctk.CTkEntry(frame,width=230)
        self.hoten_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Họ Tên",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.hoten_entry.place(x=100,y=50)

        namsinh_lab = ctk.CTkLabel(frame,text="Năm Sinh:")
        namsinh_lab.place(x=10,y=90)
        # self.namsinh_entry = ctk.CTkEntry(frame,width=230)
        self.namsinh_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Năm Sinh (dd/mm/yy)",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.namsinh_entry.place(x=100,y=90)

        gioitinh_lab = ctk.CTkLabel(frame,text="Giới Tính:")
        gioitinh_lab.place(x=10,y=130)
        self.gioitinh_cb = ctk.CTkComboBox(frame,width=230,values=['Nam','Nữ'],state='readonly')
        self.gioitinh_cb.place(x=100,y=130)

        email_lab = ctk.CTkLabel(frame,text="Email:")
        email_lab.place(x=10,y=170)
        # self.email_entry = ctk.CTkEntry(frame,width=230)
        self.email_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Email",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.email_entry.place(x=100,y=170)

        malop_lab = ctk.CTkLabel(frame,text="Mã Lớp:")
        malop_lab.place(x=10,y=210)

        #Get all class
        clas_BUS = classBUS.classBUS()
        all_class = clas_BUS.get_all_class()
        malop = [str(malop[0]) for malop in all_class] 
        self.malop_cb = ctk.CTkComboBox(frame,width=230,values=malop,state='readonly')
        self.malop_cb.place(x=100,y=210)

        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_student)
        add_button.place(x=10,y=280)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=280)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_student)
        update_button.place(x=200,y=280)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_student)
        delete_button.place(x=295,y=280)

    def create_tableframe(self,frame):
        #student table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        # self.search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập MSSV hoặc tên để tìm kiếm')
        self.search_entry  = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập MSSV hoặc tên để tìm kiếm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.search_by_IDorName)
        search_button.place(x=350,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.get_student_to_table)
        reset_button.place(x=460,y=10)
        self.table = ttk.Treeview(frame,height=23)
        self.table['columns'] = ('Mã SV', 'Họ Tên', 'Năm Sinh', 'Giới Tính', 'Email', 'Mã Lớp')
        self.table.heading('Mã SV', text='Mã SV')
        self.table.heading('Họ Tên', text='Họ Tên')
        self.table.heading('Năm Sinh', text='Năm Sinh')
        self.table.heading('Giới Tính', text='Giới Tính')
        self.table.heading('Email', text='Email')
        self.table.heading('Mã Lớp', text='Mã Lớp')

        # Adjust column widths to fit within table_frame
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã SV', width=100)
        self.table.column('Họ Tên', width=200)
        self.table.column('Năm Sinh', width=100)
        self.table.column('Giới Tính', width=100)
        self.table.column('Email', width=150)
        self.table.column('Mã Lớp', width=100)
        self.table.place(x=10,y=50)
        self.table.bind('<Button-1>',self.write_all_input)

        self.get_student_to_table()

    def is_valid_input(self):
        masv = self.msv_entry.get()
        hoten = self.hoten_entry.get()
        namsinh = self.namsinh_entry.get()
        gioitinh = self.gioitinh_cb.get()
        email = self.email_entry.get()
        malop = self.malop_cb.get()
        if masv=='' or hoten =='' or namsinh=='' or gioitinh=='' or email=='' or malop=='':
            return False,"Vui lòng nhập đầy đủ thông tin"
        if not masv.isdigit():
            return False, "Mã số sinh viên chỉ nhập số"
        if any(char.isdigit() for char in hoten):
            return False, "Tên sinh viên chỉ nhập ký tự"
        try:
            dt_start = datetime.strptime(namsinh, '%d/%m/%Y')
        except ValueError:
            return False, "Năm sinh không hợp lệ"
        if not RegisterGUI.email_is_valid(RegisterGUI,email):
            return False, "Email sinh viên không hợp lệ"
        
        return True,' thành công'
    

    def add_student(self):
        masv = self.msv_entry.get()
        hoten = self.hoten_entry.get()
        namsinh = self.namsinh_entry.get()
        gioitinh = self.gioitinh_cb.get()
        email = self.email_entry.get()
        malop = self.malop_cb.get()

        #thêm vào bảng cũng như database
        is_valid,message = self.is_valid_input()
        if is_valid:
            student_obj  = studentDTO.studentDTO(masv,hoten,namsinh,gioitinh,email,malop)
            if(self.studentBUS.add_student(student_obj)):
                self.clear_input()
                self.get_student_to_table()
                messagebox.showinfo('Success','Thêm'+message)
            
        else: messagebox.showerror('Error',message)

    def update_student(self):
        masv = self.msv_entry.get()
        hoten = self.hoten_entry.get()
        namsinh = self.namsinh_entry.get()
        gioitinh = self.gioitinh_cb.get()
        email = self.email_entry.get()
        malop = self.malop_cb.get()
        is_valid,message = self.is_valid_input()
        if is_valid:
            student_obj  = studentDTO.studentDTO(masv,hoten,namsinh,gioitinh,email,malop)
            if(self.studentBUS.update_student(student_obj)):
                self.clear_input()
                self.get_student_to_table()
                messagebox.showinfo('Success','Cập nhật'+message)
            else: messagebox.showerror('Error','Không tồn tại mã sinh viên')
        else: messagebox.showerror('Error',message)

    def delete_student(self):
        masv = self.msv_entry.get()
        if(self.studentBUS.delete_student(masv)):
                self.clear_input()
                self.get_student_to_table()
                messagebox.showinfo('Success','Xoá thành công')
            
        else: messagebox.showerror('Error','Không tồn tại mã sinh viên')

    def search_by_IDorName(self):
        search_text = self.search_entry.get()
        self.table.delete(*self.table.get_children())
        result = self.studentBUS.get_all_student()
        for i in result:
            if search_text.lower() in str(i[0]) or search_text.lower() in i[1].lower():
                self.table.insert('','end',values=i)
        

    def get_student_to_table(self):
        self.table.delete(*self.table.get_children())
        result = self.studentBUS.get_all_student()
        for i in result:
            self.table.insert('','end',value=i)

    def write_all_input(self,event): #tham chiếu biến event bắt buộc khi muốn dùng hàm bind
        
        #lấy item dựa vào ví trí click
        clicked_item = self.table.identify('item',event.x,event.y)
        #get data of clicked row
        clicked_data = self.table.item(clicked_item)['values']
        
        
        if clicked_item!='':
            #clear trước khi bỏ dòng vừa nhập vào
            self.clear_input()
            self.msv_entry.insert(0, clicked_data[0])
            self.hoten_entry.insert(0, clicked_data[1]) 
            self.namsinh_entry.insert(0, clicked_data[2])
            self.gioitinh_cb.set(clicked_data[3])
            self.email_entry.insert(0, clicked_data[4])
            self.malop_cb.set(clicked_data[5])

            self.msv_entry.configure(state='disabled',fg_color='#cfe2f3')

    def clear_input(self):
        if(self.msv_entry._state=='disabled'):
            self.msv_entry.configure(state='normal',fg_color='white')
        self.msv_entry.delete(0, 'end')
        self.hoten_entry.delete(0, 'end')
        self.namsinh_entry.delete(0, 'end')
        self.gioitinh_cb.set('')
        self.email_entry.delete(0, 'end')
        self.malop_cb.set('')