import customtkinter as ctk
from tkinter import ttk, messagebox
#from BUS import scoreBUS

class ScoreMgt:
    def __init__(self):
        self.root = ctk.CTk()
        #self.scoreBUS = scoreBUS.scoreBUS()
    
    def create_interactframe(self,frame):
        pass
    
    def create_tableframe(self,frame):
        # Create Treeview
        self.table = ttk.Treeview(frame,height=23)
        self.table['columns'] = ('ID Subject', 'Subject', 'Score')
        
        # Define columns
        self.table.heading('ID Subject', text='ID Subject')
        self.table.heading('Subject', text='Subject') 
        self.table.heading('Score', text='Score')

        # Configure column widths
        self.table.column('ID Subject', width=150)
        self.table.column('Subject', width=300)
        self.table.column('Score', width=150)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.table.yview)
        self.table.configure(yscrollcommand=scrollbar.set)

        # Pack the table and scrollbar
        self.table.grid(row=0, column=0, sticky='nsew')
        scrollbar.grid(row=0, column=1, sticky='ns')
    
    def search_by_ID(self):
        pass
    
    def get_class_to_table(self):
        pass       
    
    

