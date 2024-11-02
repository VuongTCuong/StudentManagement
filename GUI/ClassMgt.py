import customtkinter as ctk
from tkinter import ttk

class ClassMgt:
    def __init__(self):
        self.root = ctk.CTk()
     
        
    def create_interactframe(self,frame):
        #student form   
        malop_lab = ctk.CTkLabel(frame,text="Mã Lớp:")
        malop_lab.place(x=10,y=10)
        malop_entry = ctk.CTkEntry(frame,width=230)
        malop_entry.place(x=100,y=10)

        tenlop_lab = ctk.CTkLabel(frame,text="Tên Lớp:")
        tenlop_lab.place(x=10,y=50)
        tenlop_entry = ctk.CTkEntry(frame,width=230)
        tenlop_entry.place(x=100,y=50)

        khoa_lab = ctk.CTkLabel(frame,text="Mã Khoa:")
        khoa_lab.place(x=10,y=90)
        khoa_entry = ctk.CTkComboBox(frame,width=230,state='readonly')
        khoa_entry.place(x=100,y=90)

        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90)
        add_button.place(x=10,y=140)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90)
        reset_button.place(x=105,y=140)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90)
        update_button.place(x=200,y=140)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90)
        delete_button.place(x=295,y=140)


    def create_tableframe(self,frame):
        #student table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập mã lớp để tìm kiếm')
        search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm')
        search_button.place(x=350,y=10)

        table = ttk.Treeview(frame,height=23)
        table['columns'] = ('Mã Lớp', 'Tên Lớp', 'Mã Khoa')
        table.heading('Mã Lớp', text='Mã Lớp')
        table.heading('Tên Lớp', text='Tên Lớp')
        table.heading('Mã Khoa', text='Mã Khoa')

        # Adjust column widths to fit within table_frame
        table.column("#0", width=0, stretch=ctk.NO)
        table.column('Mã Lớp', width=200)
        table.column('Tên Lớp', width=300)
        table.column('Mã Khoa', width=200)
        table.place(x=10,y=50)
  