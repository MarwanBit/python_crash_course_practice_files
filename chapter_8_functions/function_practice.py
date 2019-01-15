def greet_user(username):
	# Creates a function that displays a given username
	print('Hello ' + str(username.title()) + ' !')
	
def debriefing_message_chapter_8():
	print('\ntoday we are learning how to call and create functions!')
	
def favorite_book(title):
	print('\nOne of my favorite books is ' +
			str(title.title()) +
			'!')

def make_shirt(size = 'large', message = 'I love Python'):
	print('Your shirt size is ' + str(size.title()))
	print('The message printed on your shirt: ' +
			str(message.title()))

def describe_city(cityname = 'Reykajavik', country = 'Iceland'):
	print(str(cityname.title()) + ' is in ' + str(country.title()))
	
#Below shows how to make functions with optional inputs
#To do this you set a Variable to an empty list
def get_formatted_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name     
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
	



