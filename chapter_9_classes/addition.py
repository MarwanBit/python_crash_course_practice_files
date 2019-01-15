def add_two_numbers():
	one_way_flag = True
	one_iteration_list = [1]
	prompt = '\nWelcome to the addition calculator'
	prompt += '\nType "q" to quit, "begin" to begin:'
	int1_prompt = '\nEnter your first number:'
	int2_prompt = '\nEnter your second number:'
	while one_way_flag == True:
		starting_input = input(prompt)
		try:
			if int(starting_input) >= 0  or float(starting_input) >= 0:
				print('\nYour value could not be read, try again')
				add_two_numbers()
		except ValueError:
			starting_input = str(starting_input)
			if str(starting_input) == "q":
				break
			elif str(starting_input) == "begin":
				int1 = input(int1_prompt)
				int2 = input(int2_prompt)
				anwser = float(int1) + float(int2)
				print(
					"your anwser is..." +
					str(anwser) + "!"
					)
			else:
				print('Try again')

add_two_numbers()
				
		
			
	
