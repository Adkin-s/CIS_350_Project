import tkinter as tk    #What is going on with these import statements? -Eli
from tkinter import ttk
from ttkbootstrap import Style

class window():
    def __init__(self):
        # Create the main application window
        self.root = tk.Tk()
        root = self.root
        root.title("SNRK")
        self.style = Style(theme="darkly")

        # Create a chat frame
        self.chat_frame = ttk.Frame(root)
        chat_frame = self.chat_frame
        chat_frame.pack(fill='both', expand=True)

        # Create a chat display area (a scrolled text widget)
        self.chat_display = tk.Text(chat_frame, state='disabled', wrap='word')
        chat_display = self.chat_display
        chat_display.pack(fill='both', expand=True)

        # Create a message input field
        self.message_input = ttk.Entry(chat_frame)
        message_input = self.message_input
        message_input.pack(fill='x')

        # Create a send button to send messages
        send_button = ttk.Button(self.chat_frame, text="Send", command=self.send_message, bootstyle="primary")
        send_button.pack()

        # Start the Tkinter main loop
        root.mainloop()

    # Function to send a message and display it in the chat display
    def send_message(self):
        message = self.message_input.get()
        if message:
            self.chat_display.configure(state='normal')
            self.chat_display.insert('end', f"You: {message}\n")
            self.chat_display.configure(state='disabled')
            self.message_input.delete(0, 'end')
