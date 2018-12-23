prompt = "\nTell me something, and I will repeat it back to you :"
prompt += "\nEnter 'Quit' to end the program."

active = True
while active:
	message = input(prompt)
	
	if message == 'Quit':
		active = False
	else:
		print(message)
