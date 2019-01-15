cities = {
	'Charlotte' :{
		'State' : 'North Carolina',
		'Country' : 'The USA',
		'Fact' : 'Known as the banking capital of the USA',
		},
	'Boston' :{
		'State' : 'Massachusetts',
		'Country' : 'The USA',
		'Fact' : 'The first american lighthouse was built in boston',
		},
	'Los Angeles' :{
		'State' : 'California',
		'Country' : 'The USA',
		'Fact' : 'The cities name used to be El Pueblo',
		},	 
	}

for k, v in cities.items():
	print('\nThe city is : ' + str(k))
	print('\t' + v['State'] +
		'\n\tits located in ' +
		str(v['Country'])
		)
	fact_sentence = v['Fact']
	print('Fact' + ' : ' + fact_sentence)
