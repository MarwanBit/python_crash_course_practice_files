def read_favorite_number_json():
	try:
		with open(json_file, 'r') as json_file:
			json_file_var = json_file.readlines()
			for line in json_file_var:
				print('/n' + str(line))
	except Exception:
		print('try again:')
		continue

def write_favorite_number_json():
	try:
		with open(json_file, 'w') as json_file:
			try:
				'''placeholder'''
				user_input = input('Type your favorite_number:')
				user_input = float(user_input)
			except ValueError:
				'''placeholder'''
				print("That's not a number, try again")
				continue
			else:
				json.dump(user_input, json_file)
				print('Your favorite number has been stored')
				
