import customtkinter as ctk
from tkinter import ttk

class DepartmentMgt:
    def __init__(self):
        self.root = ctk.CTk()   
        
    def create_interactframe(self,frame):
        #student form   
        makhoa_lab = ctk.CTkLabel(frame,text="Mã Khoa:")
        makhoa_lab.place(x=10,y=10)
        makhoa_entry = ctk.CTkEntry(frame,width=230)
        makhoa_entry.place(x=100,y=10)

        tenkhoa_lab = ctk.CTkLabel(frame,text="Tên Khoa:")
        tenkhoa_lab.place(x=10,y=50)
        tenkhoa_entry = ctk.CTkEntry(frame,width=230)
        tenkhoa_entry.place(x=100,y=50)



        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90)
        add_button.place(x=10,y=90)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90)
        reset_button.place(x=105,y=90)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90)
        update_button.place(x=200,y=90)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90)
        delete_button.place(x=295,y=90)


    def create_tableframe(self,frame):
        #student table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập mã khoa để tìm kiếm')
        search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm')
        search_button.place(x=350,y=10)

        table = ttk.Treeview(frame,height=23)
        table['columns'] = ('Mã Khoa', 'Tên Khoa')
        table.heading('Mã Khoa', text='Mã Khoa')
        table.heading('Tên Khoa', text='Tên Khoa')

        # Adjust column widths to fit within table_frame
        table.column("#0", width=0, stretch=ctk.NO)
        table.column('Mã Khoa', width=300)
        table.column('Tên Khoa', width=400)
        table.place(x=10,y=50)
    

