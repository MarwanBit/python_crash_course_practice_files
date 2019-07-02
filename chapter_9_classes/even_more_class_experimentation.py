import tkinter as tk 


class TkinterInheritance(tk.Tk):

	def __init__(self, *args):

		tk.Tk.__init__(self, *args)


App = TkinterInheritance()
print(App.title)