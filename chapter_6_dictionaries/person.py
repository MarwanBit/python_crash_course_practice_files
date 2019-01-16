person_marwan = {'firstname' : 'Marwan', 'lastname' : 'Bit', 
	'birthday' : 'April 8th 2003', 'city' : 'Charlotte',
	'state' : 'North Carolina', 'race' : 'Arab',
	}
	
person_amine = {'firstname' : 'Amine', 'lastname' : 'Bit',
	'birthday' : 'April 8th 2003', 'city': 'Charlotte',
	'state' : 'North Carolina', 'race' : 'Arab',
	}
	
person_anwar = {'firstname' : 'Anwar', 'lastname' : 'Bit',
	'birthday' : 'April 8th 2009', 'city' : 'Charlotte',
	'state' : 'North Carolina', 'race' : 'Arab',
	}

list_of_people = [person_amine, person_marwan, person_anwar,]


for person in list_of_people:
	print('\n' + str(person['firstname']))
	print(person['lastname'])
	print(person['birthday'])
	print(person['city'])
	print(person['state'])
	print(person['race'])
	
peoples_favorite_numbers = {
	'George' : [
		4, 
		1,
		],
	'Happy': [
		12,
		4,
		],
	'Ashley' : [
		33,
		],
	'Felicity' : [
		31,
		],
	'Apple' : [
		14,
		69,
		82,
		],
	}
for name, numbers in peoples_favorite_numbers.items():
	print('\n' + str(name) + "'s favorite number(s) are/is " +
		str(numbers))
