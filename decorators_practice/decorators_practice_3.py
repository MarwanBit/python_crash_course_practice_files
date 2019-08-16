import functools

'''
#Note: Find a way to input each element in a list automatically.
Example: gen_test_list_data(range_var)
		 print_args(X1,X2,X3,....XN)
		 #Find some code which generates the lines inside of the print_args input
'''

def gen_test_list_data(range_var):
	test_data_list = []
	base_letter = "X"
	for i in range(0,int(range_var)):
		temp_data = ""
		i = str(i)
		temp_data = base_letter + i 
		test_data_list.append(temp_data)
	return test_data_list


def simple_decorator(function):
	return function

@simple_decorator
def print_args(*args):
	args_list = []
	for i in args:
		args_list.append(i)
	print(str(args_list))
	return args_list

test_list = print_args
test_list("1","2","3")




