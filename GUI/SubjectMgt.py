import customtkinter as ctk
from tkinter import ttk, messagebox
from BUS import departmentBUS, classBUS, subjectBUS
#from BUS import scoreBUS

class SubjectMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.subjectBUS = subjectBUS.subjectBUS()
    
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
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_subject)
        add_button.place(x=10,y=180)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=180)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_subject)
        update_button.place(x=200,y=180)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_subject)
        delete_button.place(x=295,y=180)
    
    def create_tableframe(self,frame):
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        self.search_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã môn hoặc tên môn để tìm kiếm",  
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

        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.search_by_IDorName)
        search_button.place(x=460,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.reset_table)
        reset_button.place(x=580,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=600,height=450)
        scrollbar.place(x=10,y=50)
        # Create Treeview
        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('mamonhoc', 'tenmonhoc', 'makhoa')
        
        # Define columns
        self.table.heading('mamonhoc', text='Mã Môn')
        self.table.heading('tenmonhoc', text='Tên Môn') 
        self.table.heading('makhoa', text='Khoa')

        # Configure column widths
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('mamonhoc', width=150)
        self.table.column('tenmonhoc', width=300)
        self.table.column('makhoa', width=150)
    
        self.table.pack(side='left')
        self.table.bind('<ButtonRelease-1>', self.write_all_input)
        self.get_subject_to_table()
        
    def clear_input(self):
        self.mamon_entry.configure(state='normal',fg_color='white')
        self.mamon_entry.delete(0, 'end')
        self.tenmon_entry.delete(0, 'end')
        self.khoa_cb.set('')
        self.tenkhoa_entry.configure(state='normal')
        self.tenkhoa_entry.delete(0, 'end')
        self.tenkhoa_entry.configure(state='disabled')

    def get_subject_to_table(self):
        try:
            self.table.delete(*self.table.get_children())
            subject_bus = subjectBUS.subjectBUS()
            subjects = subject_bus.get_all_subjects()
            print("Fetched subjects:", subjects)  # Debug print
            for subject in subjects:
                self.table.insert('', 'end', values=subject)
        except Exception as e:
            print("Error loading subjects:", str(e))  # Debug print
            messagebox.showerror("Error", f"Failed to load subjects: {str(e)}")

    def search_by_IDorName(self):
        search_value = self.search_entry.get()
        if search_value:
            self.table.delete(*self.table.get_children())
            subject_bus = subjectBUS.subjectBUS()
            filter_khoa = self.khoa_cb_filter.get()
            if filter_khoa=='Khoa':
                subjects = subject_bus.get_all_subjects()
            else:
                subjects = subject_bus.get_subject_by_department_id(filter_khoa)
            for i in subjects:
                if search_value.lower() in str(i[0]) or search_value.lower() in i[1].lower():
                    self.table.insert('', 'end', values=i)
        else:
            messagebox.showwarning("Warning", "Please enter a subject ID to search")

    def reset_table(self):
        self.search_entry.delete(0, 'end')
        self.get_subject_to_table()

    def is_valid_input(self):
        mamonhoc = self.mamon_entry.get()
        tenmonhoc = self.tenmon_entry.get()
        makhoa = self.khoa_cb.get()
        
        if mamonhoc.strip()=='' or tenmonhoc.strip()=='' or makhoa.strip()=='':
            return False, "Vui lòng nhập đầy đủ thông tin"

        if any(not char.isalnum() for char in mamonhoc):
            return False, "Mã môn học không chứa ký tự đặc biệt"
        if any(not char.isalnum() for char in tenmonhoc.replace(" ","")):
            return False, "Tên môn học không chứa ký tự đặc biệt"
        
        return True,' thành công'
    def add_subject(self):
        mamonhoc = self.mamon_entry.get().strip()
        tenmonhoc = self.tenmon_entry.get().strip()
        makhoa = self.khoa_cb.get().strip()  # Get selected department from combobox

        is_valid,message = self.is_valid_input()

        if is_valid:
            result = self.subjectBUS.add_subject(mamonhoc, tenmonhoc, makhoa)
            if result:
                self.clear_input()
                self.get_subject_to_table()
                messagebox.showinfo("Success", "Thêm"+message)
            else:
                messagebox.showerror("Error", "Thêm thất bại")
        else: messagebox.showwarning("Warning", message)

    def update_subject(self):
        mamonhoc = self.mamon_entry.get()
        tenmonhoc = self.tenmon_entry.get()
        makhoa = self.khoa_cb.get()

        is_valid,message = self.is_valid_input()
        if is_valid:
            result = self.subjectBUS.update_subject(mamonhoc, tenmonhoc, makhoa)
            if result:
                messagebox.showinfo("Success", "Cập nhật"+message)
                self.clear_input()
                self.get_subject_to_table()
                self.mamon_entry.configure(state='normal', fg_color='#f2f2f2')
            else:
                messagebox.showerror("Error", "Cập nhật thất bại")
        else:
            messagebox.showwarning("Warning", message)

    def delete_subject(self):
        mamonhoc = self.mamon_entry.get()
        if mamonhoc:
            confirm = messagebox.askyesno("Confirm", "Bạn có muốn xoá không?")
            if confirm:
                try:
                    result = self.subjectBUS.delete_subject(mamonhoc)
                    if result:
                        messagebox.showinfo("Success", "Xoá thành công")
                        self.clear_input()
                        self.get_subject_to_table()
                        self.mamon_entry.configure(state='normal', fg_color='#f2f2f2')
                    else:
                        messagebox.showerror("Error", "Xoá thất bại")
                except Exception as e:
                    messagebox.showerror("Error", f"Delete failed: {str(e)}")
        else:
            messagebox.showwarning("Warning", "Không tồn tại mã sinh viên")

    def write_all_input(self, event):
        # Get item based on click position
        clicked_item = self.table.identify('item', event.x, event.y)
        # Get data of clicked row 
        clicked_data = self.table.item(clicked_item)['values']

        if clicked_item != '':
            # Clear and re-enable before insert new data
            self.mamon_entry.configure(state='normal')
            self.clear_input()
            
            self.mamon_entry.insert(0, clicked_data[0])
            self.tenmon_entry.insert(0, clicked_data[1]) 
            self.khoa_cb.set(clicked_data[2])
            
            # Disable after setting the value
            self.mamon_entry.configure(state='disabled', fg_color='lightgray')
            
            # Get department name based on makhoa
            department_BUS = departmentBUS.departmentBUS()
            department = department_BUS.get_department_by_id(clicked_data[2])
            if department:
                self.tenkhoa_entry.configure(state='normal')
                self.tenkhoa_entry.delete(0, 'end')
                self.tenkhoa_entry.insert(0, department[1])  # Assuming department name is at index 1
                self.tenkhoa_entry.configure(state='disabled')
    
    def on_department_select(self, selected_makhoa):
        department_BUS = departmentBUS.departmentBUS()
        department = department_BUS.get_department_by_id(selected_makhoa)
        if department:
            self.tenkhoa_entry.configure(state='normal')
            self.tenkhoa_entry.delete(0, 'end')
            self.tenkhoa_entry.insert(0, department[1])
            self.tenkhoa_entry.configure(state='disabled')
    
    def filter_by_khoa(self,selected_khoa):
        search_text = self.search_entry.get()
        
        self.table.delete(*self.table.get_children())
        if selected_khoa=='Khoa':
            filter_result = self.subjectBUS.get_all_subjects()
        else:
            filter_result = self.subjectBUS.get_subject_by_department_id(selected_khoa)
        for i in filter_result:
            if search_text.lower() in str(i[0]) or search_text.lower() in i[1].lower():
                self.table.insert('','end',value=i)
