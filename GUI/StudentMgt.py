import customtkinter as ctk
from tkinter import ttk
from PIL import Image, ImageTk
import HomeGUI
class StudentMgt:
    def __init__(self):
        self.root = ctk.CTk()  
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1400
        window_height = 600
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.resizable(False,False)

        self.create_interactframe()
        self.create_tableframe()
        #Run
        self.root.mainloop()
    
    
    def create_interactframe(self):
        #parent
        self.inter_frame = ctk.CTkFrame(self.root,height=self.root._current_height-50,width=self.root._current_width/3)
        self.inter_frame.pack(side='left',padx=20)
        
        #student form 
        
        msv_lab = ctk.CTkLabel(self.inter_frame,text="Mã SV:")
        msv_lab.place(x=10,y=10)
        msv_entry = ctk.CTkEntry(self.inter_frame,width=230)
        msv_entry.place(x=100,y=10)

        hoten_lab = ctk.CTkLabel(self.inter_frame,text="Họ Tên:")
        hoten_lab.place(x=10,y=50)
        hoten_entry = ctk.CTkEntry(self.inter_frame,width=230)
        hoten_entry.place(x=100,y=50)

        namsinh_lab = ctk.CTkLabel(self.inter_frame,text="Năm Sinh:")
        namsinh_lab.place(x=10,y=90)
        namsinh_entry = ctk.CTkEntry(self.inter_frame,width=230)
        namsinh_entry.place(x=100,y=90)

        gioitinh_lab = ctk.CTkLabel(self.inter_frame,text="Giới Tính:")
        gioitinh_lab.place(x=10,y=130)
        gioitinh_cb = ctk.CTkComboBox(self.inter_frame,width=230,values=['Nam','Nữ'],state='readonly')
        gioitinh_cb.place(x=100,y=130)

        email_lab = ctk.CTkLabel(self.inter_frame,text="Email:")
        email_lab.place(x=10,y=170)
        email_entry = ctk.CTkEntry(self.inter_frame,width=230)
        email_entry.place(x=100,y=170)

        malop_lab = ctk.CTkLabel(self.inter_frame,text="Mã Lớp:")
        malop_lab.place(x=10,y=210)
        malop_cb = ctk.CTkComboBox(self.inter_frame,width=230)
        malop_cb.place(x=100,y=210)

        #button 
        add_button = ctk.CTkButton(self.inter_frame,text='Thêm',width=100)
        add_button.place(x=10,y=280)
        reset_button = ctk.CTkButton(self.inter_frame,text='Reset',width=100)
        reset_button.place(x=120,y=280)
        update_button = ctk.CTkButton(self.inter_frame,text='Cập nhật',width=100)
        update_button.place(x=230,y=280)
        delete_button = ctk.CTkButton(self.inter_frame,text='Xoá',width=100)
        delete_button.place(x=340,y=280)
        menu_button = ctk.CTkButton(self.inter_frame,text='Về Menu',width=150,command='BacktoMenu')
        menu_button.place(relx=0.3,y=320)

    def create_tableframe(self):
        #parent
        self.table_frame = ctk.CTkFrame(self.root,height=self.root._current_height-50,width=self.root._current_width*2/3)
        self.table_frame.pack(side='right',padx=20)


        #student table
        search_lab = ctk.CTkLabel(self.table_frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        search_entry = ctk.CTkEntry(self.table_frame,width=230,placeholder_text='Nhập MSSV hoặc tên để tìm kiếm')
        search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(self.table_frame,width=100,text='Tìm kiếm')
        search_button.place(x=350,y=10)

        self.table = ttk.Treeview(self.table_frame,height=23)
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
    
    def BacktoMenu(self):
        pass
StudentMgt()