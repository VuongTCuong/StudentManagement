import customtkinter as ctk
from tkinter import ttk, messagebox
from BUS import departmentBUS
from DTO import departmentDTO

class DepartmentMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.departmentBUS = departmentBUS.departmentBUS()
        
    def create_interactframe(self,frame):
        #student form   
        makhoa_lab = ctk.CTkLabel(frame,text="Mã Khoa:")
        makhoa_lab.place(x=10,y=10)
        # self.makhoa_entry = ctk.CTkEntry(frame,width=230)
        self.makhoa_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Mã Khoa",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.makhoa_entry.place(x=100,y=10)

        tenkhoa_lab = ctk.CTkLabel(frame,text="Tên Khoa:")
        tenkhoa_lab.place(x=10,y=50)
        # self.tenkhoa_entry = ctk.CTkEntry(frame,width=230)
        self.tenkhoa_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Tên Khoa",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.tenkhoa_entry.place(x=100,y=50)


        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_department)
        add_button.place(x=10,y=90)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=90)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_department)
        update_button.place(x=200,y=90)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_department)
        delete_button.place(x=295,y=90)


    def create_tableframe(self,frame):
        #student table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        # self.search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập mã khoa để tìm kiếm')
        self.search_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Mã Khoa để tìm kiếm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.search_entry.place(x=100,y=10)
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.search_by_ID)
        search_button.place(x=350,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.get_department_to_table)
        reset_button.place(x=460,y=10)
        
        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=700,height=450)
        scrollbar.place(x=10,y=50)

        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã Khoa', 'Tên Khoa')
        self.table.heading('Mã Khoa', text='Mã Khoa')
        self.table.heading('Tên Khoa', text='Tên Khoa')

        # Adjust column widths to fit within table_frame
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã Khoa', width=300)
        self.table.column('Tên Khoa', width=400)
        self.table.pack(side='left')
        self.table.bind('<ButtonRelease-1>', self.write_all_input)

        self.get_department_to_table()
    
    def add_department(self):
        is_valid,message = self.is_valid_input()
        if is_valid:
            makhoa = self.makhoa_entry.get()
            tenkhoa = self.tenkhoa_entry.get()
            
            if self.departmentBUS.add_department(makhoa, tenkhoa):
                messagebox.showinfo("Success", "Thêm"+message)
                self.clear_input()
                self.table.delete(*self.table.get_children())
                self.get_department_to_table()
            else:
                messagebox.showerror("Error", "Mã khoa đã tồn tại")
        else: messagebox.showerror("Error",message)
    def is_valid_input(self):
        makhoa = self.makhoa_entry.get()
        tenkhoa = self.tenkhoa_entry.get()
        if makhoa == '' or tenkhoa == '':
            return False,"Vui lòng nhập đầy đủ thông tin"
        if any(not char.isalnum() for char in makhoa):
            return False, "Mã khoa không chứa ký tự đặc biệt"
        if any(char.isdigit() for char in makhoa):
            return False,"Mã khoa chỉ nhập chữ"
        if any(not char.isalnum() for char in makhoa.replace(" ","")):
            return False, "Tên khoa không chứa ký tự đặc biệt"
        if any(char.isdigit() for char in tenkhoa):
            return False,"Tên khoa chỉ nhập chữ"
        return True,' thành công'
    
    def clear_input(self):
        if(self.makhoa_entry._state=='disabled'):
            self.makhoa_entry.configure(state='normal',fg_color='white')
        self.makhoa_entry.delete(0, ctk.END)
        self.tenkhoa_entry.delete(0, ctk.END)

    def get_department_to_table(self):
        self.table.delete(*self.table.get_children())
        all_department = self.departmentBUS.get_all_department()
        for department in all_department:
            self.table.insert('', ctk.END, values=department)  
        
    def search_by_ID(self):
        search_ID = self.search_entry.get()
        self.table.delete(*self.table.get_children())
        result = self.departmentBUS.get_all_department()
        for i in result:
            if search_ID.lower() in str(i[0]):
                self.table.insert('','end',values=i)

    def update_department(self):
        makhoa = self.makhoa_entry.get()
        tenkhoa = self.tenkhoa_entry.get()

        is_valid,message = self.is_valid_input()
        if is_valid:
        # Remove the extra check since the ID will exist if it's selected from table
            if self.departmentBUS.update_department(makhoa, tenkhoa):
                messagebox.showinfo('Success','Cập nhật'+message)
                self.clear_input()
                self.table.delete(*self.table.get_children())  # Clear table
                self.get_department_to_table()  # Refresh table
            else:
                messagebox.showerror('Error','Không tồn tại mã khoa')
        else:
            messagebox.showerror('Error',message)

    def delete_department(self):
        makhoa = self.makhoa_entry.get()
        if makhoa:  # Check if ID exists
            if self.departmentBUS.delete_department(makhoa):
                messagebox.showinfo('Success','Xoá thành công')
                self.clear_input()
                self.table.delete(*self.table.get_children())  # Clear table
                self.get_department_to_table()  # Refresh table
            else:
                messagebox.showerror('Error','Không tồn tại mã khoa')
        else:
            messagebox.showerror('Error','Chọn mã khoa để xoá')

    def write_all_input(self, event):
        # Get item based on click position
        clicked_item = self.table.identify('item', event.x, event.y)
        # Get data of clicked row
        clicked_data = self.table.item(clicked_item)['values']
        
        if clicked_item != '':
            # Clear before inserting new row data
            self.clear_input()
            self.makhoa_entry.insert(0, clicked_data[0])
            self.tenkhoa_entry.insert(0, clicked_data[1])
            self.makhoa_entry.configure(state='disabled', fg_color='lightgray')

    
    

            
    


