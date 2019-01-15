with open ('python_text_files/pi_digits.txt') as pi_file:
	contents = pi_file.read()
	print(contents)
	print(len(contents))

file_name = 'python_text_files/pi_digits.txt'
with open(file_name) as pi_file:
	for line in pi_file:
		print('\n' + str(line.rstrip()))
	print('------------------------------------------------------------------')
	pi_file_lines = pi_file.readlines()
	
pi_file_lines_counter = 0
for line in pi_file_lines:
	pi_file_lines_counter += 1
	print('pi file is..' + str(pi_file_lines_counter)+ ' lines long!')
