import tkinter as tk 


class TkinterInheritance(tk.Tk):

	def __init__(self, *args):

		tk.Tk.__init__(self, *args)

		self.container = tk.Frame(self)
		self.container.pack()


App = TkinterInheritance()
print(App.title)
print(App.container)
App.mainloop()