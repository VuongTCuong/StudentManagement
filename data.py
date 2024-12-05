import customtkinter as ctk

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x450")

        # Create a frame
        frame = ctk.CTkFrame(root)
        frame.pack(fill="both", expand=True)

        # Create a StringVar to track text field input
        self.text_var = ctk.StringVar()

        # Create a text entry field
        entry = ctk.CTkEntry(frame, textvariable=self.text_var)
        entry.place(x=50, y=330)

        # Create a button and initially disable it
        self.mail_button = ctk.CTkButton(frame, text='Liên hệ SV', width=90, command=self.open_contact_gui, state='disabled')
        self.mail_button.place(x=105, y=370)

        # Trace changes in the text variable
        self.text_var.trace_add('write', self.update_button_state)

    def update_button_state(self, *args):
        """Enable or disable the button based on the entry field content."""
        if self.text_var.get().strip():  # Check if the entry is not empty
            self.mail_button.configure(state='normal')
        else:
            self.mail_button.configure(state='disabled')

    def open_contact_gui(self):
        """Handle button click event."""
        print("Button clicked, opening contact GUI!")

# Run the application
if __name__ == "__main__":
    root = ctk.CTk()
    app = App(root)
    root.mainloop()
