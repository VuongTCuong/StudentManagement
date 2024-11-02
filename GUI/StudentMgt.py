import customtkinter as ctk
from tkinter import ttk,messagebox
from BUS import classBUS,studentBUS
from DTO import studentDTO
class StudentMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Student Management System - Student Management") 
         
        
    def create_interactframe(self,frame):
        #student form   
        msv_lab = ctk.CTkLabel(frame,text="Mã SV:")
        msv_lab.place(x=10,y=10)
        self.msv_entry = ctk.CTkEntry(frame,width=230)
        self.msv_entry.place(x=100,y=10)

        hoten_lab = ctk.CTkLabel(frame,text="Họ Tên:")
        hoten_lab.place(x=10,y=50)
        self.hoten_entry = ctk.CTkEntry(frame,width=230)
        self.hoten_entry.place(x=100,y=50)

        namsinh_lab = ctk.CTkLabel(frame,text="Năm Sinh:")
        namsinh_lab.place(x=10,y=90)
        self.namsinh_entry = ctk.CTkEntry(frame,width=230)
        self.namsinh_entry.place(x=100,y=90)

        gioitinh_lab = ctk.CTkLabel(frame,text="Giới Tính:")
        gioitinh_lab.place(x=10,y=130)
        self.gioitinh_cb = ctk.CTkComboBox(frame,width=230,values=['Nam','Nữ'],state='readonly')
        self.gioitinh_cb.place(x=100,y=130)

        email_lab = ctk.CTkLabel(frame,text="Email:")
        email_lab.place(x=10,y=170)
        self.email_entry = ctk.CTkEntry(frame,width=230)
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
        reset_button = ctk.CTkButton(frame,text='Reset',width=90)
        reset_button.place(x=105,y=280)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90)
        update_button.place(x=200,y=280)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90)
        delete_button.place(x=295,y=280)

    def create_tableframe(self,frame):
        #student table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập MSSV hoặc tên để tìm kiếm')
        search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm')
        search_button.place(x=350,y=10)

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
    
    def add_student(self):
        #valid_flag = 1 : hợp lệ; valid_flag=0: không hợp lệ
        valid_flag = 1
        masv = self.msv_entry.get()
        hoten = self.hoten_entry.get()
        namsinh = self.namsinh_entry.get()
        gioitinh = self.gioitinh_cb.get()
        email = self.email_entry.get()
        malop = self.malop_cb.get()

        if masv=='' or hoten =='' or namsinh=='' or gioitinh=='' or email=='' or malop=='':
            valid_flag = 0

        if valid_flag!=0:
            student = studentBUS.studentBUS()
            student_obj  = studentDTO.studentDTO(masv,hoten,namsinh,gioitinh,email,malop)
            if(student.add_student(student_obj)):
                messagebox.showinfo('Success','Added Successfuly')
            
            self.get_student_to_table()
        else: messagebox.showerror('Error','Invalid input!')

    def get_student_to_table(self):
        pass