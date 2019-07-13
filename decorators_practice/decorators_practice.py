#/////////////////////////////////////////////////////////

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
	def add_one(number):
		return number + 1
	result = add_one(add_one(number))
	return result 

print('\nplus_two(4): ' + str(plus_two(4)))