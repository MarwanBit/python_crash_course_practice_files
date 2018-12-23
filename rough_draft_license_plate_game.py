#This one way flag manages the off/on properties of the game
plate_game_on = True

#This is the list with all of the states that are in this game
list_of_states = [
				'alabama', 'alaska', 'arizona','arkansas',
				'california', 'colorado', 'conneticut', 'delaware',
				'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
				'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
				'maine', 'maryland', 'massachusetts', 'michigan', 
				'minnesota', 'mississipi', 'missouri', 'montana',
				 'nebraska', 'nevada', 'new hampshire', 'new jersey',
				 'new mexico', 'new york', 'north carolina', 'north dakota',
				 'ohio', 'oklahoma', 'oregon', 'pennyslvania', 
				 'rhode island', 'south carolina', 'south dakota',
				 'tennesse', 'texas', 'utah', 'vermont', 'virginia',
				 'washington', 'west virginia', 'wisconsin', 'wyoming',
				 ]

#This is the first prompt you see while launching the game
prompt = '\nHi welcome to the license plate finding game!!'
prompt += '\n(type "quit" to quit the game)'
prompt += '\n(type "reset" to reset the states)'
prompt += '\n(type "show" to show the current list of states)'
prompt += '\nnow enter your input here : '

#This is the second prompt which occurs after the second iteration of the loop
second_prompt = '\nTry again'
second_prompt += '\n(type "quit" to quit the game)'
second_prompt += '\n(type "reset" to reset the states)'
second_prompt += '\n(type "show" to show the current list of states)'
second_prompt += '\nnow enter your input here : '

#The game is located inside this while loop
while plate_game_on == True:
	message = raw_input(str(prompt))
	message.lower()
	if message in list_of_states:
		list_of_states.remove(message)
		print('\n' + message + ' has been removed from the list of states')
		while plate_game_on == True:
			message = raw_input(str(second_prompt))
			message.lower()
			if message in list_of_states:
				list_of_states.remove(message)
				print('\n' + message + 
					' has been removed from the list of states')
			elif message == 'quit':
				print('\nThanks for playing!')
				plate_game_on = False
				break
			elif message == 'reset':
				list_of_states = [
				'alabama', 'alaska', 'arizona','arkansas',
				'california', 'colorado', 'conneticut', 'delaware',
				'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
				'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
				'maine', 'maryland', 'massachusetts', 'michigan', 
				'minnesota', 'mississipi', 'missouri', 'montana',
				 'nebraska', 'nevada', 'new hampshire', 'new jersey',
				 'new mexico', 'new york', 'north carolina', 'north dakota',
				 'ohio', 'oklahoma', 'oregon', 'pennyslvania', 
				 'rhode island', 'south carolina', 'south dakota',
				 'tennesse', 'texas', 'utah', 'vermont', 'virginia',
				 'washington', 'west virginia', 'wisconsin', 'wyoming',
				 ]
				print('\nthe list of states has been reseted')
			elif message == 'show':
				for state in list_of_states:
					print(state)
				print(len(int(list_of_states +
					' is the number of states left'))				
	elif message == 'quit':
		print('\nThanks for playing!')
		plate_game_on = False
		break
	elif message == 'reset':
		list_of_states = [
				'alabama', 'alaska', 'arizona','arkansas',
				'california', 'colorado', 'conneticut', 'delaware',
				'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
				'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
				'maine', 'maryland', 'massachusetts', 'michigan', 
				'minnesota', 'mississipi', 'missouri', 'montana',
				 'nebraska', 'nevada', 'new hampshire', 'new jersey',
				 'new mexico', 'new york', 'north carolina', 'north dakota',
				 'ohio', 'oklahoma', 'oregon', 'pennyslvania', 
				 'rhode island', 'south carolina', 'south dakota',
				 'tennesse', 'texas', 'utah', 'vermont', 'virginia',
				 'washington', 'west virginia', 'wisconsin', 'wyoming',
				 ]
		print('\nthe list of states has been reseted')
		while plate_game_on == True:
			message = raw_input(str(second_prompt))
			message.lower()
			if message in list_of_states:
				list_of_states.remove(message)
				print('\n' + message + 
					' has been removed from the list of states')
			elif message == 'quit':
				print('\nThanks for playing!')
				plate_game_on = False
				break
			elif message == 'reset':
				list_of_states = [
				'alabama', 'alaska', 'arizona','arkansas',
				'california', 'colorado', 'conneticut', 'delaware',
				'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
				'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
				'maine', 'maryland', 'massachusetts', 'michigan', 
				'minnesota', 'mississipi', 'missouri', 'montana',
				 'nebraska', 'nevada', 'new hampshire', 'new jersey',
				 'new mexico', 'new york', 'north carolina', 'north dakota',
				 'ohio', 'oklahoma', 'oregon', 'pennyslvania', 
				 'rhode island', 'south carolina', 'south dakota',
				 'tennesse', 'texas', 'utah', 'vermont', 'virginia',
				 'washington', 'west virginia', 'wisconsin', 'wyoming',
				 ]
				print('\nthe list of states has been reseted')
			elif message == 'show':
				for state in list_of_states:
					print(state)
				print(len(int(list_of_states +
					' is the number of states left'))
	elif message == 'show':
		for state in list_of_states:
			print(state)
		print(len(int(list_of_states +
					' is the number of states left'))
			while plate_game_on == True:
				message = raw_input(str(second_prompt))
				message.lower()
				if message in list_of_states:
					list_of_states.remove(message)
					print('\n' + message + 
						' has been removed from the list of states')
				elif message == 'quit':
					print('\nThanks for playing!')
					plate_game_on = False
					break
				elif message == 'reset':
					list_of_states = [
					'alabama', 'alaska', 'arizona','arkansas',
					'california', 'colorado', 'conneticut', 'delaware',
					'florida', 'georgia', 'hawaii', 'idaho', 'illinois',
					'indiana', 'iowa', 'kansas', 'kentucky', 'louisiana',
					'maine', 'maryland', 'massachusetts', 'michigan', 
					'minnesota', 'mississipi', 'missouri', 'montana',
					 'nebraska', 'nevada', 'new hampshire', 'new jersey',
					 'new mexico', 'new york', 'north carolina', 'north dakota',
					 'ohio', 'oklahoma', 'oregon', 'pennyslvania', 
					 'rhode island', 'south carolina', 'south dakota',
					 'tennesse', 'texas', 'utah', 'vermont', 'virginia',
					 'washington', 'west virginia', 'wisconsin', 'wyoming',
					 ]
					print('\nthe list of states has been reseted')
				elif message == 'show':
					for state in list_of_states:
						print(state)
					print(len(int(list_of_states +
					' is the number of states left'))		
	
