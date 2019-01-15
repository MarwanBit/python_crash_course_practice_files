#This is the prompt used to engage with the guest 
prompt = 'Hello guest... what is your name? :'

#This asks the guest to give their name and stores it in a variable called guest_name
guest_name = input(prompt)

#This line stores a file_name called guest_list.txt in a variable called file
file = 'guest_list.txt'

'''
Line 15 creates a file in write mode and stores it as guest_name_file.
The line under that writes the guest's name in the file guest_name_file.
The last line prints the file guest_name_file
'''
with open(file, 'w') as guest_name_file:
	guest_name_file.write(str(guest_name))
with open(file) as guest_name_file:
	line = guest_name_file.readlines()
	for name in line:
		print(name)
