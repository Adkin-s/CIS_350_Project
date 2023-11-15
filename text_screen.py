import tkinter as tk    #What is going on with these import statements? -Eli
from tkinter import ttk
from ttkbootstrap import Style
import chatbot as cb

class Window():
    def __init__(self):
        # Creates a few predetermined chatbot personas. Currently hardcoded to just one persona, as there's no way to switch personas via the GUI yet.
        #I'd prefer to run the chatbot commands first, so the API has time to load before the GUI is created. -Eli
        self.personas = {
            "Snarky" : cb.Persona("Mr. Snarky", "Your name is 'Mr. Snarky'. You are a mean, snarky, and passive-agressive assistant.", [{}]),
            #"Kind" : cb.Persona("Mr. Kind", "Your name is 'Mr. Kind'. You are a nice, friendly, and helpful assistant.", [{}]),
            #"Silly" : cb.Persona("Mr. Silly", "Your name is 'Mr. Silly'. You are a silly, funny, and playful assistant.", [{}]),
            #"Serious" : cb.Persona("Mr. Serious", "Your name is 'Mr. Serious'. You are a professional, serious, and formal assistant.", [{}])
            }
        self.currentPersona = self.personas["Snarky"] #Defaults to Snarky

        # Create the main application window
        self.root = tk.Tk()
        root = self.root
        root.title("SNRK")
        Style(theme="darkly")

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

    #TODO TEST TEST TEST
    # Function to send a message and display it in the chat display
    def send_message(self): #TODO fill with last session's user and chatbot messages. Requires full DB implementation.
        message = self.message_input.get()
        chatbotMessage = self.currentPersona.prompt(message)

        if message:
            self.chat_display.configure(state='normal')
            self.chat_display.insert('end', f"User: {message}\n")
            self.chat_display.configure(state='disabled')
            self.message_input.delete(0, 'end')

        if chatbotMessage:
            self.chat_display.configure(state='normal')
            self.chat_display.insert('end', f"{self.currentPersona.name}: {message}\n")
            self.chat_display.configure(state='disabled')
            self.message_input.delete(0, 'end')
        
        chatbotMessage = None