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

#Game while loop
while plate_game_on == True:
    message = input(prompt)
    if message == 'quit':
        print('\nthanks for playing the license plate game' +
	    ' have a good day!')
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
        print('\n\tThe list of states has been reset!, you are starting' +
	    ' from zero!!')
		
    elif message == 'show':
        list_of_states_for_show = []
        for state in list_of_states:
            list_of_states_for_show.append(state)
        print(list_of_states_for_show)
    elif message in list_of_states:
        list_of_states.remove(message)
        print('\n ' + message + ' has been removed from the list of' + ' states')
	

while plate_game_on == True:
    message = input(str(second_prompt))
    message.lower()
    if message == 'quit':
        print('\nthanks for playing the license plate game' +
	    ' have a good day!')
        plate_game_on = False
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
        print('\n\tThe list of states has been reset!, you are starting' +
	    ' from zero!!')
    elif message == 'show':
        list_of_states_for_show = []
        for state in list_of_states:
            list_of_states_for_show.append(state)
            if len(list_of_states_for_show) == 5:     
                print(list_of_states_for_show)
                list_of_states_for_show = []               
    elif message in list_of_states:
		list_of_states.remove(message)
		print('\n ' + message + ' has been removed from the list of' +
			' states')
		
