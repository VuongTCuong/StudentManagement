import customtkinter as ctk
import StudentMgt
import ClassMgt
import DepartmentMgt
class Changetab:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Student Management System - Student Management") 
        #center window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 1400
        window_height = 600
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
        self.root.resizable(False,False)

        #current tab
        self.cur_tab = 'StudentMgt'
        
        #menu frame
        self.top_frame()

        #left and right frame
        self.left_frame()
        self.right_frame()

        #current tab
        self.set_current_tab(self.cur_tab)

        self.root.mainloop()

    def top_frame(self):
        #parent
        self.top_frame = ctk.CTkFrame(self.root,width=1400,height=40)
        self.top_frame.pack(side='top',padx=20,pady=5)
        
        #center top-down button in parent (28 is default height of any button)
        y_center = (self.top_frame._current_height-28)/2
       
        #child
        sv_tab_button = ctk.CTkButton(self.top_frame,text='Sinh Viên',width=80,command=self.changeto_student_tab)
        sv_tab_button.place(x=5,y=y_center)
        
        lop_tab_button = ctk.CTkButton(self.top_frame, text='Lớp',width=80,command=self.changeto_class_tab)
        lop_tab_button.place(x=90, y=y_center)

        khoa_tab_button = ctk.CTkButton(self.top_frame, text='Khoa',width=80,command=self.changeto_department_tab)
        khoa_tab_button.place(x=175, y=y_center)

        #need EXIT button

    def left_frame(self):
        self.left_frame = ctk.CTkFrame(self.root,height=self.root._current_height-50,width=self.root._current_width/3)
        self.left_frame.pack(side='left',padx=20)

    def right_frame(self):
        self.right_frame = ctk.CTkFrame(self.root,height=self.root._current_height-50,width=self.root._current_width*2/3)
        self.right_frame.pack(side='left',padx=20)

    def set_current_tab(self,tab_name):
        if tab_name=='StudentMgt':
            student = StudentMgt.StudentMgt()
            student.create_interactframe(self.left_frame)
            student.create_tableframe(self.right_frame)
        elif tab_name=='ClassMgt':
            class_obj = ClassMgt.ClassMgt()
            class_obj.create_interactframe(self.left_frame)
            class_obj.create_tableframe(self.right_frame)
        elif tab_name=='DepartmentMgt':
            department = DepartmentMgt.DepartmentMgt()
            department.create_interactframe(self.left_frame)
            department.create_tableframe(self.right_frame)

    def destroy_LeftRight_children(self):
        for i in self.left_frame.winfo_children():
            i.destroy()
        for j in self.right_frame.winfo_children():
            j.destroy()

    def changeto_student_tab(self):
        if self.cur_tab!='StudentMgt':
            self.destroy_LeftRight_children()

            student = StudentMgt.StudentMgt()
            self.root.title("Student Management System - Student Management") 
            student.create_interactframe(self.left_frame)
            student.create_tableframe(self.right_frame)
            self.cur_tab ='StudentMgt'

    def changeto_class_tab(self):
        if self.cur_tab!='ClassMgt':
            self.destroy_LeftRight_children()

            class_obj = ClassMgt.ClassMgt()
            self.root.title("Student Management System - Class Management")
            class_obj.create_interactframe(self.left_frame)
            class_obj.create_tableframe(self.right_frame)
            self.cur_tab='ClassMgt'

    def changeto_department_tab(self):
        if self.cur_tab!='DepartmentMgt':
            self.destroy_LeftRight_children()
            department = DepartmentMgt.DepartmentMgt()
            self.root.title("Student Management System - Department Management")
            department.create_interactframe(self.left_frame)
            department.create_tableframe(self.right_frame)
            self.cur_tab='DepartmentMgt'