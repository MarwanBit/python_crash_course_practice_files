#Asks user what rental car they want
wanted_car = input('Hello, what type of rental car would you like?'+
	' : ')
print('Ohh so would you like a(n)' + ' ' + str(wanted_car) + '?')
yes_or_no = input('Is that your final decision?' +
	'type yes or no : ')

if yes_or_no:
	yes_or_no.lower()
	if 'yes' in yes_or_no:
		print('Ok well get that request processed!')
	else:
		print('Well look around and see if we can interest you' +
			'in a different car')



		
