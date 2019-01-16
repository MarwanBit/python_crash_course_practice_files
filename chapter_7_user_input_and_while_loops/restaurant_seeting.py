seeting_request = raw_input('Hello, how many people will be' +
							'sitting with you? : ')
seeting_request_number = int(seeting_request)

if seeting_request_number > 8:
	print('Wow thats alot of people, sorry for the inconvenience' +
			' But you will have to wait till we can serve you')
elif seeting_request_number < 8:
	print('Great we have a table available for you right now!')
elif seeting_request_number == 8:
	print('Wow the perfect amount, we have a table available for you!')
else:
	print('are you trolling? or is this an error?')
	 
