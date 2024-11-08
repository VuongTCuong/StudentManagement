import customtkinter as ctk
from tkinter import ttk, messagebox
from BUS import departmentBUS, classBUS
#from BUS import scoreBUS

class SubjectMgt:
    def __init__(self):
        self.root = ctk.CTk()
        #self.scoreBUS = scoreBUS.scoreBUS()
    
    def create_interactframe(self,frame):
        mamon_lab = ctk.CTkLabel(frame,text="Mã Môn:")
        mamon_lab.place(x=10,y=10)

        self.mamon_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Mã Môn",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.mamon_entry.place(x=100,y=10)

        tenmon_lab = ctk.CTkLabel(frame,text="Tên Môn:")
        tenmon_lab.place(x=10,y=50)
        self.tenmon_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Tên Môn",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.tenmon_entry.place(x=100,y=50)


        tenkhoa_lab = ctk.CTkLabel(frame,text="Tên Khoa:")
        tenkhoa_lab.place(x=10,y=130)
        self.tenkhoa_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Tên Khoa",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888", state="disable" 
        )
        self.tenkhoa_entry.place(x=100,y=130)

        chonkhoa_lab = ctk.CTkLabel(frame,text="Khoa:")
        chonkhoa_lab.place(x=10,y=90)
        department_BUS = departmentBUS.departmentBUS()
        all_department = department_BUS.get_all_department()
        makhoa = [str(makhoa[0]) for makhoa in all_department] 
        self.khoa_cb = ctk.CTkComboBox(frame,width=230,values=makhoa,state='readonly',command=self.on_department_select)
        self.khoa_cb.place(x=100,y=90)

        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90)
        add_button.place(x=10,y=180)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90)
        reset_button.place(x=105,y=180)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90)
        update_button.place(x=200,y=180)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90)
        delete_button.place(x=295,y=180)
    
    def create_tableframe(self,frame):
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        # self.search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập mã khoa để tìm kiếm')
        self.search_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã khoa để tìm kiếm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm')
        search_button.place(x=350,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset')
        reset_button.place(x=460,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=600,height=450)
        scrollbar.place(x=10,y=50)
        # Create Treeview
        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã Môn', 'Tên Môn', 'Khoa')
        
        # Define columns
        self.table.heading('Mã Môn', text='Mã Môn')
        self.table.heading('Tên Môn', text='Tên Môn') 
        self.table.heading('Khoa', text='Khoa')

        # Configure column widths
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã Môn', width=150)
        self.table.column('Tên Môn', width=300)
        self.table.column('Khoa', width=150)
    
        self.table.pack(side='left')
        self.table.bind('<ButtonRelease-1>')
   
    def search_by_ID(self):
        pass
    
    def get_class_to_table(self):
        pass       
    
    def on_department_select(self, selected_makhoa):
        department_BUS = departmentBUS.departmentBUS()
        department = department_BUS.get_department_by_id(selected_makhoa)
        if department:
            self.tenkhoa_entry.configure(state='normal')
            self.tenkhoa_entry.delete(0, 'end')
            self.tenkhoa_entry.insert(0, department[1])
            self.tenkhoa_entry.configure(state='disabled')

