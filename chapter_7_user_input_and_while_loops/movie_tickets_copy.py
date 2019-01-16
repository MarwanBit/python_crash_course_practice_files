#One way flag that operates the loop
movie_open = True

#Message shown to user when they ask for the price of there ticket
prompt = '\nHello welcome to AMC theaters, please enter your age below.'
prompt += '\ntype "quit" to leave the theater price finder'
prompt += '\n(please enter your age to the right) : '

#Message for second time applications of the program
second_time_prompt = '\nType another age to see the price associated..'
second_time_prompt += '\nwith that age'
second_time_prompt += '\n(please enter your age to the right) : '

#While loop that encapsulates the entire program
while movie_open == True:
	message = raw_input(prompt)
	if message < 3:
		print('\n your ticket price is $0.00')
	elif message > 3 and message < 12:
		print('\n your ticket price is $10')
	elif message > 12:
		print('\n your ticket price is $15')
	elif message == 'quit':
		print('\n hope you had a good time at AMC theaters!')

	
