import tkinter as tk
from tkinter import messagebox
from webapp import WebApp

class LoginScreen:
	def __init__(self, master):
		self.master = master
		self.master.title("Global Chat Service")
		self.webapp = WebApp()

		self.label_email = tk.Label(self.master, text="Email")
		self.label_password = tk.Label(self.master, text="Password")

		self.entry_email = tk.Entry(self.master)
		self.entry_password = tk.Entry(self.master, show="*")

		self.label_email.grid(row=0, sticky="E")
		self.label_password.grid(row=1, sticky="E")

		self.entry_email.grid(row=0, column=1)
		self.entry_password.grid(row=1, column=1)

		self.login_button = tk.Button(self.master, text="Login", command=self.login)
		self.login_button.grid(columnspan=2)

	def login(self):
		email = self.entry_email.get()
		password = self.entry_password.get()

		user = self.webapp.login_user(email, password)
		if user:
			messagebox.showinfo("Login info", "Login Successful")
			self.master.destroy()
			self.open_chat_screen(user)
		else:
			messagebox.showinfo("Login info", "Login Failed")

	def open_chat_screen(self, user):
		# Open the chat screen
		pass

if __name__ == "__main__":
	root = tk.Tk()
	app = LoginScreen(root)
	root.mainloop()
