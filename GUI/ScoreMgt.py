import customtkinter as ctk
from tkinter import ttk, messagebox
from DTO import scoreDTO
from BUS import scoreBUS, studentBUS, subjectBUS



class ScoreMgt:
    def __init__(self):
        self.root = ctk.CTk()
        self.scoreBUS = scoreBUS.scoreBUS()
    
    def create_interactframe(self,frame):

        masv_lab = ctk.CTkLabel(frame,text="Mã Sinh Viên:")
        masv_lab.place(x=10,y=10)
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
        self.masv_entry.place(x=100,y=10)
        self.masv_entry.bind('<FocusOut>',self.set_tensv_entry)
        tensv_lab = ctk.CTkLabel(frame,text="Tên Sinh Viên:")
        tensv_lab.place(x=10,y=50)

        self.tensv_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Vui lòng nhập mã sinh viên trước",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,
            fg_color='#cfe2f3',          
            text_color="#333333",         
            placeholder_text_color="#888888",
        )
        self.tensv_entry.place(x=100,y=50)
        self.tensv_entry.configure(state='disabled')
        

        mamon_lab = ctk.CTkLabel(frame,text="Mã Môn:")
        mamon_lab.place(x=10,y=90)
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
        self.mamon_entry.place(x=100,y=90)
        self.mamon_entry.bind('<FocusOut>',self.set_tenmon_entry)

        tenmon_lab = ctk.CTkLabel(frame,text="Tên Môn:")
        tenmon_lab.place(x=10,y=130)

        self.tenmon_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Vui lòng nhập mã môn trước",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,
            fg_color='#cfe2f3',      
            text_color="#333333",         
            placeholder_text_color="#888888"
        )
        self.tenmon_entry.place(x=100, y=130)
        self.tenmon_entry.configure(state='disabled')
        

        diemgk_lab = ctk.CTkLabel(frame,text="Điểm giữa kỳ:")
        diemgk_lab.place(x=10,y=170)
        self.diemgk_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Điểm giữa kỳ",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.diemgk_entry.place(x=100,y=170)

        diemthi_lab = ctk.CTkLabel(frame,text="Điểm thi:")
        diemthi_lab.place(x=10,y=210)
        self.diemthi_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập Điểm thi",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.diemthi_entry.place(x=100,y=210)
        #button 
        add_button = ctk.CTkButton(frame,text='Thêm',width=90,command=self.add_score)
        add_button.place(x=10,y=260)
        reset_button = ctk.CTkButton(frame,text='Reset',width=90,command=self.clear_input)
        reset_button.place(x=105,y=260)
        update_button = ctk.CTkButton(frame,text='Cập nhật',width=90,command=self.update_score)
        update_button.place(x=200,y=260)
        delete_button = ctk.CTkButton(frame,text='Xoá',width=90,command=self.delete_score)
        delete_button.place(x=295,y=260)
    
    def create_tableframe(self,frame):
        search_lab = ctk.CTkLabel(frame,text="Tìm kiếm:")
        search_lab.place(x=10,y=10)
        self.search_entry = ctk.CTkEntry(
            frame,
            placeholder_text="Nhập mã sinh viên để tìm kiếm",  
            width=230,                    
            height=35,                    
            border_width=0,               
            corner_radius=10,             
            fg_color="#f2f2f2",           
            text_color="#333333",         
            placeholder_text_color="#888888" 
        )
        self.search_entry.place(x=100,y=10)

        search_button = ctk.CTkButton(frame,width=100,text='Tìm kiếm',command=self.get_score_by_IDorName)
        search_button.place(x=350,y=10)
        reset_button = ctk.CTkButton(frame,width=100,text='Reset',command=self.reset_search)
        reset_button.place(x=460,y=10)

        #Add scrollbar
        scrollbar = ctk.CTkScrollableFrame(frame,width=600,height=450)
        scrollbar.place(x=10,y=50)
        # Create Treeview
        self.table = ttk.Treeview(scrollbar,height=23)
        self.table['columns'] = ('Mã Môn', 'Mã Sinh Viên', 'Điểm giữa kỳ', 'Điểm thi')
        
        # Define columns
        self.table.heading('Mã Môn', text='Mã Môn')

        self.table.heading('Mã Sinh Viên', text='Mã Sinh Viên') 
        self.table.heading('Điểm giữa kỳ', text='Điểm giữa kỳ')
        self.table.heading('Điểm thi', text='Điểm thi')

        # Configure column widths
        self.table.column("#0", width=0, stretch=ctk.NO)
        self.table.column('Mã Môn', width=150)
   
        self.table.column('Mã Sinh Viên', width=300)
        self.table.column('Điểm giữa kỳ', width=150)
        self.table.column('Điểm thi', width=150)
        self.table.pack(side='left')
        self.table.bind('<ButtonRelease-1>', self.write_all_input)
        
        self.get_all_scores()
    
    def clear_input(self):
        if(self.masv_entry._state=='disabled'):
            self.masv_entry.configure(state='normal',fg_color='white')
        self.masv_entry.delete(0, 'end')
        
        self.tensv_entry.configure(state='normal')
        self.tensv_entry.delete(0, 'end')
        self.tensv_entry.configure(placeholder_text='Vui lòng nhập mã sinh viên trước')
        self.tensv_entry.configure(state='disabled')

        if(self.mamon_entry._state=='disabled'):
            self.mamon_entry.configure(state='normal',fg_color='white')
        self.mamon_entry.delete(0, 'end')
        
        self.tenmon_entry.configure(state='normal')
        self.tenmon_entry.delete(0, 'end')
        self.tenmon_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
        self.tenmon_entry.configure(state='disabled')

        self.diemgk_entry.delete(0, 'end')
        self.diemthi_entry.delete(0, 'end')
    def is_valid_input(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        diemgk = self.diemgk_entry.get()
        diemthi = self.diemthi_entry.get()

        if(mamon.strip()=='' or masv.strip()==''):
            return False,'Vui lòng nhập đầy đủ thông tin'
        
        if any(not char.isalnum() for char in mamon):
            return False, "Mã môn học không chứa ký tự đặc biệt"
        if any(not char.isalnum() for char in masv):
            return False, "Mã sinh viên không chứa ký tự đặc biệt"
        if not masv.isdigit():
            return False,"Mã sinh viên chỉ nhập số"
        if not diemgk.replace(".","").isdigit():
            return False,'Điểm giữa kỳ chỉ nhập số'
        if not diemthi.replace(".","").isdigit():
            return False,'Điểm thi chỉ nhập số'
        return True,' thành công'
    

    def add_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        diemgk = self.diemgk_entry.get()
        diemthi = self.diemthi_entry.get()
        is_valid, message = self.is_valid_input()
        if is_valid:
            # Check if subject and student exist
            if not self.scoreBUS.check_subject_exists(mamon):
                messagebox.showerror('Error', 'Mã môn không tồn tại')
                return
            if not self.scoreBUS.check_student_exists(masv):
                messagebox.showerror('Error', 'Mã sinh viên không tồn tại') 
                return
                
            score_obj = scoreDTO.scoreDTO(mamon,masv,diemgk,diemthi)
            if(self.scoreBUS.add_score(score_obj)):
                self.clear_input()
                self.get_all_scores()
                messagebox.showinfo('Success','Thêm'+message)   
            else:
                messagebox.showerror('Error','Thêm thất bại')
        else:
            messagebox.showerror('Error',message)
    
    def update_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        diemgk = self.diemgk_entry.get()
        diemthi = self.diemthi_entry.get()
        is_valid,message = self.is_valid_input()
        if is_valid:
            # Check if subject and student exist
            if not self.scoreBUS.check_subject_exists(mamon):
                messagebox.showerror('Error', 'Mã môn không tồn tại')
                return
            if not self.scoreBUS.check_student_exists(masv):
                messagebox.showerror('Error', 'Mã sinh viên không tồn tại') 
                return
            score_obj = scoreDTO.scoreDTO(mamon,masv,diemgk,diemthi)
            if(self.scoreBUS.update_score(score_obj)):
                self.clear_input()
                self.get_all_scores()
                messagebox.showinfo('Success','Cập nhật'+message)
            else:
                messagebox.showerror('Error','Cập nhật thất bại')
        else:
            messagebox.showerror('Error',message)
    
    def delete_score(self):
        mamon = self.mamon_entry.get()
        masv = self.masv_entry.get()
        if not self.scoreBUS.check_subject_exists(mamon):
            messagebox.showerror('Error', 'Mã môn không tồn tại')
            return
        if not self.scoreBUS.check_student_exists(masv):
            messagebox.showerror('Error', 'Mã sinh viên không tồn tại') 
            return
        
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
    
    def get_score_by_IDorName(self):
        search_text = self.search_entry.get()
        result = self.scoreBUS.get_all_scores()
        
        self.table.delete(*self.table.get_children())

        for i in result:
            if search_text.lower() in str(i[0]) or search_text.lower() in str(i[1]).lower():
                self.table.insert('', 'end', values=i)  

    def write_all_input(self,event):
        clicked_item = self.table.identify('item',event.x,event.y)
        
        clicked_data = self.table.item(clicked_item)['values']

        # Clear previous entries first
        if clicked_item != '':
            self.clear_input()
            self.mamon_entry.insert(0,clicked_data[0])
            self.masv_entry.insert(0,clicked_data[1])
            self.diemgk_entry.insert(0,clicked_data[2])
            self.diemthi_entry.insert(0,clicked_data[3])
            self.mamon_entry.configure(state='disabled',fg_color='#cfe2f3')
            self.masv_entry.configure(state='disabled',fg_color='#cfe2f3')
        self.set_tensv_entry(event)
        self.set_tenmon_entry(event)

    


    def reset_search(self):
        self.clear_input()
        self.get_all_scores()
    
    def set_tensv_entry(self,event):
        masv = self.masv_entry.get()
        stuBUS = studentBUS.studentBUS()
        sinhvien_result = stuBUS.get_one_student(masv)
        if masv.strip()!='':
            if sinhvien_result:
                self.tensv_entry.configure(state='normal')
                self.tensv_entry.delete(0,'end')
                self.tensv_entry.insert(0,sinhvien_result[1])
                self.tensv_entry.configure(state='disabled')
            else:
                self.tensv_entry.configure(state='normal')
                self.tensv_entry.delete(0, 'end')
                self.tensv_entry.configure(placeholder_text='Không tìm thấy mã sinh viên')
                self.tensv_entry.configure(state='disabled')
        else:
            self.tensv_entry.configure(state='normal')
            self.tensv_entry.delete(0, 'end')
            self.tensv_entry.configure(placeholder_text='Vui lòng nhập mã sinh viên trước')
            self.tensv_entry.configure(state='disabled')

    def set_tenmon_entry(self,event):
        mamon = self.mamon_entry.get()
        subBUS = subjectBUS.subjectBUS()
        mon_result = subBUS.get_one_subject(mamon)
        if mamon.strip()!='':
            if mon_result:
                self.tenmon_entry.configure(state='normal')
                self.tenmon_entry.delete(0,'end')
                self.tenmon_entry.insert(0,mon_result[1])
                self.tenmon_entry.configure(state='disabled')
            else:
                self.tenmon_entry.configure(state='normal')
                self.tenmon_entry.delete(0, 'end')
                self.tenmon_entry.configure(placeholder_text='Không tìm thấy mã môn ')
                self.tenmon_entry.configure(state='disabled')
        else:
            self.tenmon_entry.configure(state='normal')
            self.tenmon_entry.delete(0, 'end')
            self.tenmon_entry.configure(placeholder_text='Vui lòng nhập mã môn trước')
            self.tenmon_entry.configure(state='disabled')

        


