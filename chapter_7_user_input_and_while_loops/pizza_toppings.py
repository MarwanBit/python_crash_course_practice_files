#Creates the pizza store ordering/ topping selecting message
prompt = '\nHello welcome to our pizza shop, what toppings would you..'
prompt += 'Like on your pizza, type the topping in!'
prompt += '\ntype "quit" to cancel the order'
prompt += '\ntype "done" to finish the pizza order : '

#Prompt for second time applications of the while loop and so on
second_time_prompt = 'Please type in your next topping'
second_time_prompt += '\ntype "quit" to cancel the order'
second_time_prompt += '\ntype "done" to finish the pizza order : '

#One way flag indicating the store is open
#Also list of toppings that is user generated is initialized
pizza_store_open = True
user_generated_pizza_toppings = []

#While loop containing the whole ordering program
while pizza_store_open == True:
	message = input(prompt)
	message.lower()
	if message == 'quit':
		print('\n\tWell have a good day, bye bye!')
		pizza_store_open = False
	elif message == 'done':
		print('\nWell that will be all, your pizza will have' +
			'\t' +
			str(user_generated_pizza_toppings))
		while pizza_store_open == True:
			message = input('\n' + second_time_prompt)
			message.lower()
			if message == 'quit':
				print('\n\tWell have a good day, bye bye!')
				pizza_store_open = False
			elif message == 'done':
				print('\nWell that will be all,' + 
					'your pizza will have' +
					'\t' +
					str(user_generated_pizza_toppings))
			else:
				print('\tOk ' + str(message) +
						' will be added to your pizza!')
				user_generated_pizza_toppings.append(message)
				
	else:
		print('\tOk ' + str(message) + ' will be added to your pizza!')
		user_generated_pizza_toppings.append(message)
		while pizza_store_open == True:
			message = input('\n' + second_time_prompt)
			message.lower()
			if message == 'quit':
				print('\n\tWell have a good day, bye bye!')
				pizza_store_open = False
			elif message == 'done':
				print('\nWell that will be all,' +
					'your pizza will have' +
					'\t' +
					str(user_generated_pizza_toppings))
			else:
				print('\tOk ' + str(message) + 
					' will be added to your pizza!')
				user_generated_pizza_toppings.append(message)
				
