higher_status_document = 'higher_status.txt'
success_counter = 0

with open(higher_status_document, 'r', encoding = 'utf-8') as higher_status:
	try:
		higher_status_lines = higher_status.readlines()
		for line in higher_status_lines:
			success_counter +=(line.count('status'))
	except FileNotFoundError:
		print('This file cannot be found')

print(success_counter) 
