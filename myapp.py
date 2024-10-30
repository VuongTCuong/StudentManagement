import customtkinter as ctk
from tkinter import messagebox, ttk, W
import sqlite3

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("300x300")
        
        # Set appearance mode and default theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Initialize user database (for demonstration purposes)
        self.users = {"username": "password"}

        #connect db
        try:
            self.conn = sqlite3.connect('student_management.db')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không có cơ sở dữ liệu: {e}")
        # Main application layout
        self.create_login_screen()

    def create_login_screen(self):
        # Center the window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 250) // 2
        y = (screen_height - 250) // 2
        self.root.geometry(f"300x300+{x}+{y}")
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        # Login screen layout
        ctk.CTkLabel(self.root, text="Login", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(self.root, text="Username:").pack()
        self.username_entry = ctk.CTkEntry(self.root)
        self.username_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Password:").pack()
        self.password_entry = ctk.CTkEntry(self.root, show="*")
        self.password_entry.pack(pady=5)

        ctk.CTkButton(self.root, text="Login", command=self.check_login).pack(pady=20)

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Query the users table to check credentials
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.create_main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def create_menu(self):
        # Create Menu bar
        menu_bar = ctk.CTkFrame(self.root)
        menu_bar.pack(fill="x")

        # Create menu buttons instead of traditional menus
        #student_frame = ctk.CTkFrame(menu_bar)
        #student_frame.pack(side="left", padx=5)
        
        #ctk.CTkButton(student_frame, text="Search Student", command=self.create_search_screen).pack(side="left", padx=2)
        #ctk.CTkButton(student_frame, text="Update Student Info", command=self.create_update_screen).pack(side="left", padx=2)

        account_frame = ctk.CTkFrame(menu_bar)
        account_frame.pack(side="right", padx=5)
        
        ctk.CTkButton(account_frame, text="Logout",
                     command=self.create_login_screen).pack(side="left", padx=2)
        ctk.CTkButton(account_frame, text="Exit",
                     command=self.root.quit).pack(side="left", padx=2)

    def create_main_menu(self):
        # Clear the window
        self.root.geometry(f"1920x1080") 
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.create_menu()
           
        # Welcome Label
        ctk.CTkLabel(self.root, text="Welcome to the Student Management System", 
                    font=("Arial", 16)).pack(pady=50)
      
        self.search_screen()
        self.update_screen()
        
        #quit button
        quit_button = ctk.CTkButton(self.root, text="Quit", command=self.root.quit)
        quit_button.pack(pady=50)

    def update_screen(self):
        #self.create_menu()
        # Update screen layout
        ctk.CTkLabel(self.root, text="Update Student Info", font=("Arial", 18)).pack(pady=20)

        # Add form fields to add or delete a student
        ctk.CTkLabel(self.root, text="Student ID:").pack()
        self.student_id_entry = ctk.CTkEntry(self.root)
        self.student_id_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Student Name:").pack()
        self.student_name_entry = ctk.CTkEntry(self.root)
        self.student_name_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Semester:").pack()
        self.semester_entry = ctk.CTkEntry(self.root)
        self.semester_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Class ID:").pack()
        self.class_id_entry = ctk.CTkEntry(self.root)
        self.class_id_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Course Name:").pack()
        self.course_name_entry = ctk.CTkEntry(self.root)
        self.course_name_entry.pack(pady=5)

        ctk.CTkButton(self.root, text="Add Student", command=self.add_student).pack(pady=10)
        ctk.CTkButton(self.root, text="Delete Student", command=self.delete_student).pack(pady=10)

    def search_screen(self):
        # self.root.geometry("1500x500")
        ctk.CTkLabel(self.root, text="Search Student", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(self.root, text="Enter Student Name or ID:").pack()

        self.search_entry = ctk.CTkEntry(self.root)
        self.search_entry.pack(pady=5)

        ctk.CTkButton(self.root, text="Search", command=self.search_student).pack(pady=10)
        ctk.CTkButton(self.root, text="Reset", command=self.reset_search).pack(pady=10)


        # Treeview to display search results (keeping ttk.Treeview as CustomTkinter doesn't have an equivalent)
        self.search_results = ttk.Treeview(self.root, columns=("Student ID", "Student Name", "Class Name", "Subject Name", "Total Sessions", "Absences", "Absence Dates"))
        self.search_results.column("#0", width=0, stretch=ctk.NO)
        self.search_results.heading("Student ID", text="Student ID")
        self.search_results.heading("Student Name", text="Student Name")
        self.search_results.heading("Class Name", text="Class Name")
        self.search_results.heading("Subject Name", text="Subject Name")
        self.search_results.heading("Total Sessions", text="Total Sessions")
        self.search_results.heading("Absences", text="Absences")
        self.search_results.heading("Absence Dates", text="Absence Dates")
        self.search_results.pack(pady=20, fill="both", expand=False)

        # Fetch data from the database and insert into the Treeview
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        for row in cursor.fetchall():
            self.search_results.insert("", "end", values=row)
        conn.close()
        
    def create_search_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            self.root.geometry("1500x500")

        self.create_menu()
        # Search screen layout
        ctk.CTkLabel(self.root, text="Search Student", font=("Arial", 18)).pack(pady=20)
        ctk.CTkLabel(self.root, text="Enter Student Name or ID:").pack()

        self.search_entry = ctk.CTkEntry(self.root)
        self.search_entry.pack(pady=5)

        ctk.CTkButton(self.root, text="Search", command=self.search_student).pack(pady=10)

        # Treeview to display search results
        self.search_results = ttk.Treeview(self.root, columns=("Student ID", "Student Name", "Class Name", "Subject Name", "Total Sessions", "Absences", "Absence Dates"))
        self.search_results.column("#0", width=0, stretch=ctk.NO)
        self.search_results.heading("Student ID", text="Student ID")
        self.search_results.heading("Student Name", text="Student Name")
        self.search_results.heading("Class Name", text="Class Name")
        self.search_results.heading("Subject Name", text="Subject Name")
        self.search_results.heading("Total Sessions", text="Total Sessions")
        self.search_results.heading("Absences", text="Absences")
        self.search_results.heading("Absence Dates", text="Absence Dates")
        self.search_results.pack(pady=20, fill="both", expand=False)

    def search_student(self):
        # This function should interact with the database to retrieve student data.
        # For this demo, we will use hardcoded data.
        query = self.search_entry.get()
        self.search_results.delete(*self.search_results.get_children())
        data = []
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        for row in cursor.fetchall():
            data.append(row)
        conn.close()
        #Display the results if the search query matches
        for student in data:
            if query.lower() in student[0].lower() or query.lower() in student[1].lower():
                self.search_results.insert("", "end", values=student)
                
    def reset_search(self):
        self.search_results.delete(*self.search_results.get_children())
        conn = sqlite3.connect('student_management.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM attendance")
        for row in cursor.fetchall():
            self.search_results.insert("","end",value=row)
        conn.close()

    def create_update_screen(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()
            self.root.geometry("500x450")

        self.create_menu()
        # Update screen layout
        ctk.CTkLabel(self.root, text="Update Student Info", font=("Arial", 18)).pack(pady=20)

        # Add form fields to add or delete a student
        ctk.CTkLabel(self.root, text="Student ID:").pack()
        self.student_id_entry = ctk.CTkEntry(self.root)
        self.student_id_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Student Name:").pack()
        self.student_name_entry = ctk.CTkEntry(self.root)
        self.student_name_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Semester:").pack()
        self.semester_entry = ctk.CTkEntry(self.root)
        self.semester_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Class ID:").pack()
        self.class_id_entry = ctk.CTkEntry(self.root)
        self.class_id_entry.pack(pady=5)

        ctk.CTkLabel(self.root, text="Course Name:").pack()
        self.course_name_entry = ctk.CTkEntry(self.root)
        self.course_name_entry.pack(pady=5)

        ctk.CTkButton(self.root, text="Add Student", command=self.add_student).pack(pady=10)
        ctk.CTkButton(self.root, text="Delete Student", command=self.delete_student).pack(pady=10)

    def add_student(self):
        # Add student logic (to be implemented with database)
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        semester = self.semester_entry.get()
        class_id = self.class_id_entry.get()
        course_name = self.course_name_entry.get()

        # Example success message
        messagebox.showinfo("Add Student", f"Student {student_name} added successfully!")

    def delete_student(self):
        # Delete student logic (to be implemented with database)
        student_id = self.student_id_entry.get()

        # Example success message
        messagebox.showinfo("Delete Student", f"Student ID {student_id} deleted successfully!")

# Create and run the application
root = ctk.CTk()
app = StudentApp(root)
root.mainloop()
