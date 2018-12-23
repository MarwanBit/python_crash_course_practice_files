Hedwig = {
	'Animal Type' : 'Owl',
	'Owner' : 'Harry Potter',
	'Name' : 'Hedwig',
	}
Crookshanks = {
	'Animal Type' : 'Cat',
	'Owner' : 'Hermione',
	'Name' : 'Crookshanks',
	}
Nagini = {
	'Animal Type' : 'Snake',
	'Owner' : 'Lord Voldemort',
	'Name' : 'Nagini',
	}
BuckBeak = {
	'Animal Type' : 'Hypogriff',
	'Owner' : 'Hagrid',
	'Name' : 'BuckBeak',
	}

pets = [
	Hedwig, 
	Crookshanks, 
	Nagini, 
	BuckBeak,
	]

for pet in pets:
	print('\n\t' + str(pet['Name']))
	print('\n' + str(pet['Animal Type']))
	print(str(pet['Owner']))
