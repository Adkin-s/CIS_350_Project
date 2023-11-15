import tkinter	#FIXME remove this import if possible. -Eli
import customtkinter
import authHelpers as auth
import text_screen

class window():
	def __init__(self) -> None:
		self.customtkinter.set_appearance_mode("dark")
		self.customtkinter.set_default_color_theme("dark-blue")
		self.root = customtkinter.CTk()
		root = self.root
		root.geometry("500x350")

		self.frame = customtkinter.CTkFrame(master=root)
		frame = self.frame
		frame.pack(pady=20, padx=60, fill="both", expand=True)

		self.label = customtkinter.CTkLabel(master=frame, text="Login System")
		self.label.pack(pady=12, padx=10)

		self.entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
		self.entry1.pack(pady=12, padx=10)

		self.entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
		self.entry2.pack(pady=12, padx=10)

		self.button = customtkinter.CTkButton(master=frame, text="Login", command=self.login)
		self.button.pack(pady=12, padx=10)

		self.checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
		self.checkbox.pack(pady=12, padx=10)

		self.root.mainloop()

	def login(self) -> bool:
		if auth.login(self.entry1, self.entry2):	#FIXME talk with James to try and understand if this will work.
			#Opens the text screen upon sucessful login.
			self.text_screen = text_screen.window()