major_rivers = {
	'nile' : 'egypt',
	'yellow' : 'china',
	'missisipi' : 'the united states of america',
	}

for river, location in major_rivers.items():
	print("The" +
		" " +
		str(river) +
		" flows through " +
		str(location))
		
river_names = []
for river in major_rivers.keys():
	river_names.append(river)
	print('\nThe ' + str(river) + ' river')

print('\n' + str(river_names))
river_names_index = 0

for location in major_rivers.values():
	print('\nThe ' + str(river_names[int(river_names_index)]) + 
		' River is located in ' + str(location))
	print('\t' + str(location))
	river_names_index = river_names_index + 1
