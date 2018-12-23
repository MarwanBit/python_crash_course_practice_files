favorite_languages_poll = {
	'Daniel' : 'CSS',
	'Angela' : 'HTML',
	'Aphrodite' : 'C#',
	'Anida' : 'Python',
	'Sasuke' : 'C++',
	'Askarala' : 'Java',
	'Sami' : 'Javascript',
	'Marwan' : 'Python',
	}

people_who_should_take_poll = [
	'Tami',
	'Sami',
	'Askarala',
	'Daniel',
	'Janson',
	'Bryan',
	'Sahada',
	'Samson',
	]

for person in people_who_should_take_poll:
	if person in favorite_languages_poll:
		print('\nThank you ' + 
			str(person) +
			' for taking the poll')
	else:
		print('\nHello ' +
		str(person) +
		' please take the poll')
