import tkinter as tk 


class TkinterInheritance(tk.Tk):

	def __init__(self, *args):

		tk.Tk.__init__(self, *args)

		self.container = tk.Frame(self, height=300, width=300)
		self.container.pack()

		


App = TkinterInheritance()
canvas = tk.Entry(App.container)
canvas.place(relx=0.5,rely=0.5, relheight=0.1, relwidth=0.4, anchor='n')
App.mainloop()