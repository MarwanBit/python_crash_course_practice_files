#Decorators practice to understand the concept

def decorator_func(function):
	'''prints the *args and **kwargs of the inputed function'''
	def wrapper(*args):
		args_list = []
		for arg in args:
			args_list.append(str(arg))
		args_string = 'The args are : ' + str(args_list)
		func_string = str(function(*args))
		return args_string + '\n\n' + func_string
	return wrapper 


@decorator_func
def adding_function(func_1, func_2):
	'''print's the string of two functions being added'''
	str_func_1 = str(func_1)
	str_func_2 = str(func_2)
	return str_func_1 + " + " + str_func_2


print(adding_function('g(x)','f(x)'))


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

def square_function(function):
	'''decorator which squares a function which is inputed''' 
	def wrapper_func(num_1,num_2):
		'''the resulting returned_function'''
		func_output = function(num_1,num_2)
		func_output = func_output ** 2 
		return func_output 
	return wrapper_func 

@square_function
def get_sum(num_1,num_2):
	'''add's two numbers''' 
	return float(num_1 + num_2)

print('\n' + str(get_sum(1,2)) + '\n') 

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 

def dec_1(function):
	'''returns the cube after the operation of an inputed function''' 
	def wrapper_func(num_1,num_2):
		'''returns func with the square'''
		func_output = function(num_1,num_2)
		func_output = func_output ** 2
		return func_output 
	return wrapper_func

def dec_2(function):
	'''returns the val of inputed function divided by 2''' 
	def wrapper_func_2(num_1,num_2):
		'''returns the output/2'''
		output = function(num_1,num_2)
		output = output / 2
		return output 
	return wrapper_func_2

@dec_2
@dec_1
def find_difference(num_1,num_2):
	'''finds the difference of num_1 and num_2'''
	return float(float(num_1)-float(num_2))

print(find_difference(14,12))

#Note: Decorators take in a function and return a modified function which you can then call 
#Note: Decorators are applied from a bottom up way, for example above, find_difference is put into
# dec_1, and then the function returned is put into dec_2