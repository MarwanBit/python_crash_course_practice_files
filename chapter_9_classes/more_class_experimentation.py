import tkinter as tk 

class MainPage(tk.Tk):

	def __init__(self, **kwargs):

		tk.Tk.__init__(self, **kwargs)
		tk.Tk.wm_title(self,"Yeet")

		self.frame = tk.Frame(self, height=300, width=300)
		self.frame.pack(side = "top", fill="both",expand=True)
		self.frame.grid_rowconfigure(0, weight=1)
		self.frame.grid_columnconfigure(0, weight=1)

		self.button = tk.Button(self.frame,width=10, height=1, text="ohhh")
		self.button.pack(side="top")



a = MainPage()
a.mainloop()