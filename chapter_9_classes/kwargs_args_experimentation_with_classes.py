import tkinter as tk 

class GyraLoginPage(tk.Tk):

	def __init__(self, *args, **keyargs):
		
		self.arg_list = []

		for arg in args:
			self.arg_list.append(str(arg))
			
		print(self.arg_list)

		self.keyarg_dict = {}

		for key, value in keyargs.items():
			self.keyarg_dict[str(key)] = str(value)

		print(self.keyarg_dict)

			

app = GyraLoginPage('arg1','arg2','arg3','arg4', apple = 'red', orange = 'orange', blueberry = 'blue' )
print(app)