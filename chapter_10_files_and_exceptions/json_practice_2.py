import json

json_practice = 'python_text_files/favorite_number.json'

try:
	with open(json_practice) as file_obj:
		favorite_number = json.load(file_obj)
except FileNotFoundError:
	user_input = input('Enter your favorite number:')
	with open(json_practice, 'w') as file_obj:
		json.dump(user_input, file_obj)
		print('your favorite number..' + favorite_number + ' has been dumped into a file for storage!!')
else:
	print('your favorite number is..' + favorite_number + '!' )
