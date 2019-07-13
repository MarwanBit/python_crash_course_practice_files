#Decorators practice to understand the concept

@decorator
def adding_functions(func_1, func_2):
	'''print's the string of two functions being added'''
	str_func_1 = str(func_1)
	str_func_2 = str(func_2)
	return str_func_1 + " + " + str_func_2

def decorator(function):
	'''prints the *args and **kwargs of the inputed function'''
	def wrapper(*args):
		args_list = []
		for arg in args:
			args_list.append(str(arg))
		args_string = 'The args are : ' + str(args_list)
		func_string = str(function(*args))
		return args_string 
	return wrapper 

adding_function('g(x)','f(x)')