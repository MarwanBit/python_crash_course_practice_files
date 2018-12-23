website_usernames = ['Admin', 'Eric', 'Johnathan', 'Flamie', 'Simple']

if website_usernames:
	for username in website_usernames:
		if username == 'Admin':
			print('Hello Admin, welcome back to your administration duties')
		else:
			print('Hello' + ' ' + str(username) + ', welcome to the site')
else:
	print('There are no users on this website')
