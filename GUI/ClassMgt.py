import customtkinter as ctk
from tkinter import ttk, messagebox
from BUS import departmentBUS, classBUS
from DTO import classDTO

class ClassMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.classBUS = classBUS.classBUS()

        
    def create_interactframe(self,frame):
        #class form   
        malop_lab = ctk.CTkLabel(frame,text="Mã Lớp:")
        malop_lab.place(x=10,y=10)
        # self.malop_entry = ctk.CTkEntry(frame,width=230)
        self.malop_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Mã Lớp",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.malop_entry.place(x=100,y=10)

        tenlop_lab = ctk.CTkLabel(frame,text="Tên Lớp:")
        tenlop_lab.place(x=10,y=50)
        # self.tenlop_entry = ctk.CTkEntry(frame,width=230)
        self.tenlop_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Tên Lớp: ",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.tenlop_entry.place(x=100,y=50)

        khoa_lab = ctk.CTkLabel(frame,text="Mã Khoa:")
        khoa_lab.place(x=10,y=90)

        #name of department base on department id
        tenkhoa_lab = ctk.CTkLabel(frame,text="Tên Khoa:")
        tenkhoa_lab.place(x=10,y=130)
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
            placeholder_text_color="#888888", state="disable" 
        )
        self.tenkhoa_entry.place(x=100,y=130)
        #self.tenkhoa_entry.configure(state='disabled',fg_color='lightgray')

        #get all department
        department_BUS = departmentBUS.departmentBUS()
        all_department = department_BUS.get_all_department()
        makhoa = [str(makhoa[0]) for makhoa in all_department] 
        self.khoa_cb = ctk.CTkComboBox(frame,width=230,values=makhoa,state='readonly',command=self.on_department_select)
        self.khoa_cb.place(x=100,y=90)

        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_class)
        add_button.place(x=10,y=170)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=170)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_class)
        update_button.place(x=200,y=170)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_class)
        delete_button.place(x=295,y=170)


    def create_tableframe(self,frame):
        #class table
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        # self.search_entry = ctk.CTkEntry(frame,width=230,placeholder_text='Nhập mã lớp để tìm kiếm')
        self.search_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Tên lớp để tìm kiếm",  
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


        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.search_by_ten)
        search_button.place(x=460,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.get_class_to_table)
        reset_button.place(x=580,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=700,height=450)
        scrollbar.place(x=10,y=50)

        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã Lớp', 'Tên Lớp', 'Mã Khoa')
        self.table.heading('Mã Lớp', text='Mã Lớp')
        self.table.heading('Tên Lớp', text='Tên Lớp')
        self.table.heading('Mã Khoa', text='Mã Khoa')

        # Adjust column widths to fit within table_frame
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã Lớp', width=200)
        self.table.column('Tên Lớp', width=300)
        self.table.column('Mã Khoa', width=200)
        self.table.pack(side='left')
        self.table.bind('<Button-1>',self.write_all_input)

        self.get_class_to_table()
    
    # check input
    def is_valid_input(self):
        malop = self.malop_entry.get()
        tenlop = self.tenlop_entry.get() 
        makhoa = self.khoa_cb.get()

        if malop == '' or tenlop == '' or makhoa == '':
            return False,"Vui lòng nhập đầy đủ thông tin"
        if not malop.isdigit():
            return False,"Mã lớp chỉ nhập số"
        if any(not char.isalnum() for char in tenlop.replace(" ","")):
            return False, "Tên lớp không chứa ký tự đặc biệt"
        
        if self.classBUS.get_one_class(malop):
            return False, "Mã lớp đã tồn tại"
        
        return True,' thành công'
        
    # check input and add class to database
    def add_class(self):
        malop = self.malop_entry.get()
        tenlop = self.tenlop_entry.get()
        makhoa = self.khoa_cb.get()

        is_valid,message = self.is_valid_input()
        if is_valid:
            if(self.classBUS.add_class(malop, tenlop, makhoa)):
                self.clear_input()
                self.get_class_to_table()
                messagebox.showinfo('Success','Thêm'+message)
        else:
            messagebox.showerror('Error',message)

    # clear input
    def clear_input(self):
        if(self.malop_entry._state=='disabled'):
            self.malop_entry.configure(state='normal',fg_color='white')
        self.malop_entry.delete(0, 'end')
        self.tenlop_entry.delete(0, 'end')
        self.khoa_cb.set('')
        self.tenkhoa_entry.configure(state='normal')
        self.tenkhoa_entry.delete(0, 'end')
        self.tenkhoa_entry.configure(state='disabled')


    # update class
    def update_class(self):
        malop = self.malop_entry.get()
        tenlop = self.tenlop_entry.get()
        makhoa = self.khoa_cb.get()

        #check if class exists
        if not self.classBUS.get_class_by_id(malop):
            messagebox.showerror('Error', 'Mã lớp không tồn tại')
            return
        
        is_valid,message = self.is_valid_input()
        if is_valid:
            if(self.classBUS.update_class(malop, tenlop, makhoa)):
                self.clear_input()
                self.get_class_to_table()
                messagebox.showinfo('Success','Cập nhật'+message)
            else:
                messagebox.showerror('Error','Cập nhật thất bại')
        else:
            messagebox.showerror('Error',message)

            
    # delete class
    def delete_class(self):
        malop = self.malop_entry.get()
        if(self.classBUS.delete_class(malop)):
            self.clear_input()
            self.get_class_to_table()
            messagebox.showinfo('Success','Xoá thành công')
        else:
            messagebox.showerror('Error','Không tồn tại mã lớp')

 
    # get all class to table
    def get_class_to_table(self):
        self.table.delete(*self.table.get_children())

        #reset filter
        self.search_entry.delete(0,'end')
        self.khoa_cb_filter.set('Khoa')

        result = self.classBUS.get_all_class()
        for i in result:
            self.table.insert('','end',value=i)
        
    def search_by_ten(self):
        search_text = self.search_entry.get()
        self.table.delete(*self.table.get_children())

        khoa = self.khoa_cb_filter.get()
        if khoa!='Khoa':
            result = self.classBUS.get_class_by_depart(self.khoa_cb_filter.get())
        else:
            result = self.classBUS.get_all_class()
        for i in result:
            if search_text.lower() in str(i[1]).lower():
                self.table.insert('','end',values=i)

    def write_all_input(self,event): #event is required when using bind 
        
        #get item based on click position
        clicked_item = self.table.identify('item',event.x,event.y)
        #get data of clicked row
        clicked_data = self.table.item(clicked_item)['values']
        
        
        if clicked_item!='':
            #clear before insert new data
            self.clear_input()
            self.malop_entry.insert(0, clicked_data[0])
            self.tenlop_entry.insert(0, clicked_data[1])
            self.khoa_cb.set(clicked_data[2])
            self.malop_entry.configure(state='disabled',fg_color='lightgray')

            # Get department name based on makhoa
            department_BUS = departmentBUS.departmentBUS()
            department = department_BUS.get_department_by_id(clicked_data[2])
            if department:
                self.tenkhoa_entry.configure(state='normal')
                self.tenkhoa_entry.delete(0, 'end')
                self.tenkhoa_entry.insert(0, department[1])  # Assuming department name is at index 1
                self.tenkhoa_entry.configure(state='disabled')

    #get department name based on makhoa (combobox)
    def on_department_select(self, selected_makhoa):
        department_BUS = departmentBUS.departmentBUS()
        department = department_BUS.get_department_by_id(selected_makhoa)
        if department:
            self.tenkhoa_entry.configure(state='normal')
            self.tenkhoa_entry.delete(0, 'end')
            self.tenkhoa_entry.insert(0, department[1])
            self.tenkhoa_entry.configure(state='disabled')

    def filter_by_khoa(self,selected_khoa):
        if selected_khoa != 'Khoa':
            filter_result = self.classBUS.get_class_by_depart(selected_khoa)
        else:
            filter_result = self.classBUS.get_all_class()
        self.table.delete(*self.table.get_children())

        search_text = self.search_entry.get()
        for i in filter_result:
            if search_text.lower() in i[1].lower():
                self.table.insert('','end',value=i)
        
            




        

  