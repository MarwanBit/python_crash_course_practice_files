learning_python_file = 'python_text_files/learning_python.txt'
with open(learning_python_file) as python_file:
	lines = python_file.readlines()

for line in lines:
	print(line)
	print(line)
	print(line)
	print('----------------------------')

print('\n' + '-------------------------------------------------')

with open(learning_python_file) as python_file_replaced:
	lines = python_file_replaced.readlines()

for line in lines:
	line = line.replace('I have learned', 'I HAVE NOT LEARNED')
	print(line)
	print('-------------------')