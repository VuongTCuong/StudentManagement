import customtkinter as ctk
from tkinter import ttk, messagebox
from DTO import scoreDTO
from BUS import scoreBUS



class ScoreMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.scoreBUS = scoreBUS.scoreBUS()
    
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

        masv_lab = ctk.CTkLabel(frame,text="Mã Sinh Viên:")
        masv_lab.place(x=10,y=50)
        self.masv_entry = ctk.CTkEntry(
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
        self.masv_entry.place(x=100,y=50)

        diem_lab = ctk.CTkLabel(frame,text="Điểm:")
        diem_lab.place(x=10,y=90)
        self.diem_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Điểm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.diem_entry.place(x=100,y=90)
        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_score)
        add_button.place(x=10,y=160)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=160)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_score)
        update_button.place(x=200,y=160)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_score)
        delete_button.place(x=295,y=160)
    
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
        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.search_score)
        search_button.place(x=350,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.reset_search)
        reset_button.place(x=460,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=600,height=450)
        scrollbar.place(x=10,y=50)
        # Create Treeview
        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã Môn', 'Mã Sinh Viên', 'Điểm')
        
        # Define columns
        self.table.heading('Mã Môn', text='Mã Môn')
        self.table.heading('Mã Sinh Viên', text='Mã Sinh Viên') 
        self.table.heading('Điểm', text='Điểm')

        # Configure column widths
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã Môn', width=150)
        self.table.column('Mã Sinh Viên', width=300)
        self.table.column('Điểm', width=150)
    
        self.table.pack(side='left')
        self.table.bind('<ButtonRelease-1>', self.write_all_input)
        
        self.get_all_scores()
    
    def clear_input(self):
        if(self.mamon_entry._state=='disabled'):
            self.mamon_entry.configure(state='normal',fg_color='white')
        self.mamon_entry.delete(0, 'end')
        self.masv_entry.delete(0, 'end')
        self.diem_entry.delete(0, 'end')
    
    def is_valid_input(self):
        if(self.mamon_entry.get()=='' or self.masv_entry.get()=='' or self.diem_entry.get()==''):
            return False,'Không được để trống'
        return True,'Thêm thành công'
    

    def add_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        diem = self.diem_entry.get()
        is_valid,message = self.is_valid_input()
        if is_valid:
            score_obj = scoreDTO.scoreDTO(mamon,masv,diem)
            if(self.scoreBUS.add_score(score_obj)):
                self.clear_input()
                self.get_all_scores()
                messagebox.showinfo('Success',message)   
            else:
                messagebox.showerror('Error',message)
        else:
            messagebox.showerror('Error',message)
    
    def update_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        diem = self.diem_entry.get()
        is_valid,message = self.is_valid_input()
        if is_valid:
            score_obj = scoreDTO.scoreDTO(mamon,masv,diem)
            if(self.scoreBUS.update_score(score_obj)):
                self.clear_input()
                self.get_all_scores()
                messagebox.showinfo('Success','Cập nhật'+message)
    
    def delete_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        if(self.scoreBUS.delete_score(mamon,masv)):
            self.clear_input()
            self.get_all_scores()
            messagebox.showinfo('Success','Xoá thành công')
    
    def get_all_scores(self):
        result = self.scoreBUS.get_all_scores()
        # Clear existing items
        for item in self.table.get_children():
            self.table.delete(item)
        # Only insert if we have results
        if result:
            for i in result:
                self.table.insert('', 'end', values=i)
    
    def get_score_by_id(self,mamon,masv):
        result = self.scoreBUS.get_score_by_student_and_subject_id(masv,mamon)
        for i in result:
            self.table.insert('', 'end', values=i)  

    def write_all_input(self,event):
        clicked_item = self.table.identify('item',event.x,event.y)
        
        clicked_data = self.table.item(clicked_item)['values']

        # Clear previous entries first
        if clicked_item != '':
            self.clear_input()
            self.mamon_entry.insert(0,clicked_data[0])
            self.masv_entry.insert(0,clicked_data[1])
            self.diem_entry.insert(0,clicked_data[2])
            self.mamon_entry.configure(state='disabled',fg_color='#cfe2f3')
        


    
    def search_score(self):
        mamon = self.search_entry.get()
        self.get_score_by_id(mamon)

    def reset_search(self):
        self.clear_input()
        self.get_all_scores()
    
    def close_window(self):
        self.root.destroy()
    
    

        


