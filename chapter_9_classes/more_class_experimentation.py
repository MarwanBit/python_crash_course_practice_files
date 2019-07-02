import tkinter as tk 

class MainPage(tk.Tk):

	def __init__(self, **kwargs):

		tk.Tk.__init__(self, **kwargs)
		tk.Tk.wm_title(self,"Yeet")

		frame = tk.Frame(tk.Tk, height=300, width=300)



a = MainPage()
a.mainloop()