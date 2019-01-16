ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in ordinal_numbers:
	if number == 1:
		print(str(number) + 'st')
	elif number == 2:
		print(str(number) + 'nd')
	elif number == 3:
		print(str(number) + 'rd')
	elif number >= 4:
		print(str(number) + 'th')
