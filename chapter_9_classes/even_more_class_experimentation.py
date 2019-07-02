import tkinter as tk 


class TkinterInheritance(tk.Tk):

	def __init__(self, *args):

		tk.Tk.__init__(self, *args)

		self.container = tk.Frame(self, height=300, width=300)
		self.container.pack(side='top', fill='both',expand='true')

		self.frames= {}


		


App = TkinterInheritance()
App.mainloop()