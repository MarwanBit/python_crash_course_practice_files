import random

#/////////////////////////////////////////////////////////
#https://www.datacamp.com/community/tutorials/decorators-python 

#Part one: Assigning Functions to Variables

def plus_one(number):
	'''add's one to the inputed variable'''
	return number + 1


#The function above (and all other functions) can be
#assigned to variables and then those variables can 
#be called with params
add_one = plus_one
#add_one which is assigned to the func. plus_one which takes
#in the param number and runs the plus_one function
print('\nadd_one is a var which is set equal to a function,' + 
		' functions should be treated as objects:')
print('add_one(5): ' + str(add_one(5)))

#//////////////////////////////////////////////////////// 

#Part Two: Defining Functions inside Functions

def plus_two(number):
	'''plus_two passes number to add_one'''
	def add_one(number):
		return number + 1
	#add_one is defined and then used inside plus_two
	#twice, getting the effect of adding twice
	result = add_one(add_one(number))
	#this result is then returned when plus_two is called
	return result 

print('\nplus_two(4): ' + str(plus_two(4)))

#//////////////////////////////////////////////////////// 

#Part Three: Passing Functions as Arguments to other Functions

def square_number(number):
	'''squares the number inputed'''
	return number * number 

def subtract_1_then_other(num,func):
	'''subtracts one from num and then executes func'''
	num = num - 1
	num = func(num)
	return num 

print('\nexample of using a func as a param:' + 
		str(subtract_1_then_other(12, square_number)))


#///////////////////////////////////////////////////////// 

#Part Four: Functions returning functions

def function_returns_function():
	'''this function returns another func which is input'''
	def return_string():
		'''returns the string of str(string)'''
		return "string"
	'''returns the return_string function as an object'''
	return return_string

func_var = function_returns_function()
print('\n' + str(func_var))
print(func_var())
print('\n')

#//////////////////////////////////////////////////////////// 

#Part 5:Nested Functions have access to the enclosing function's
#Variable scope

def print_message(message):
	'''print's message'''
	#This is the enclosing function 
	def message_sender():
		#This is the nested function
		#this func has access to message
		print(message)

	message_sender()

print_message("Some random message")
print('\n')

#//////////////////////////////////////////////////////////// 

#Part 6: Creating Decorators

def say_hi():
	'''returns the string hello there'''
	return 'hello there'

def uppercase_decorator(function):
	'''Take a function and then returns wrapper (the nested function)'''
	def wrapper():
		'''
		wrapper takes the inputed function and calls it and stores it.
		It then uppercases that string and returns the result 
		'''
		func = function()
		make_uppercase = func.upper()
		return make_uppercase

	return wrapper

#Here's the way that decorators work,
#You pass the original function into the decorator function,
#The ouput is then printed, we just use special syntax for 
#Decorators with the @ sign
decorate = uppercase_decorator(say_hi)
print(decorate() + '\n')

#These lines can just be simplified using @name_of_decorator,
#Which sort of passes the function below as an input into the decorator
#Example: 

@uppercase_decorator
def say_hello():
	'''returns the string 'yeet'''
	return "yeet"

print('\n' + say_hello() + '\n')

#///////////////////////////////////////////////////////////// 

#Part 7: Applying Multiple Decorators to a Single Function

def decorator_1(function):
	def wrapper():
		func = function()
		func = func.upper()
		return func 
	return wrapper


@decorator_1
def say_yaga():
	'''returns the string yaga'''
	return 'yaga' 

wrapper_func = decorator_1(say_yaga)
print(wrapper_func())