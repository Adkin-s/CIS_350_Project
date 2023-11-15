import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style

# Create the main application window
root = tk.Tk()
root.title("SNRK")
style = Style(theme="darkly")

# Create a chat frame
chat_frame = ttk.Frame(root)
chat_frame.pack(fill='both', expand=True)

# Create a chat display area (a scrolled text widget)
chat_display = tk.Text(chat_frame, state='disabled', wrap='word')
chat_display.pack(fill='both', expand=True)

# Create a message input field
message_input = ttk.Entry(chat_frame)
message_input.pack(fill='x')

# Function to send a message and display it in the chat display
def send_message():
    message = message_input.get()
    if message:
        chat_display.configure(state='normal')
        chat_display.insert('end', f"You: {message}\n")
        chat_display.configure(state='disabled')
        message_input.delete(0, 'end')

# Create a send button to send messages
send_button = ttk.Button(chat_frame, text="Send", command=send_message, bootstyle="primary")
send_button.pack()

# Start the Tkinter main loop
root.mainloop()
