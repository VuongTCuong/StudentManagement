import customtkinter as ctk

class Mailbox:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry('600x400')
        self.root.mainloop()

Mailbox()