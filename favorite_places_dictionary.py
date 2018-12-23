peoples_favorite_places = {
	'Kanye' : [
		'Paris',
		'Hawaii',
		'Wisconsin',
		],
	'Logic' : [
		'Maryland',
		'Chicago',
		'Madison Square Garden',
		],
	'Kendrick Lamar' : [
		'Compton',
		'Africa',
		'Robins Island',
		],
		}

for people, places  in peoples_favorite_places.items():
	print('\n' + str(people) + 
	"'s favorite places are " + 
	str(places))
