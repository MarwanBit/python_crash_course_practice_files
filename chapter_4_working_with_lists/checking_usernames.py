current_users = ['Logic', 'Denzel Curry', 'Kendrick Lamar', 'IDK', 
			     'J. Cole', 'Lupe Fiasco', 'Joey Badass', 'Russ']
new_users = ['YBN Cordae', 'BROCKHAMPTON', 'Bas', 'IDK', 'Russ']

for username in new_users:
	if username in current_users:
		print('Sorry' + ' ' + str(username) + ' but that username has been taken, try another one')
	elif username not in current_users:
		print('The username' + ' ' + str(username) + ' is available')
