import json

file_name = 'username.json'

try:
	with open(file_name) as file_obj:
		username = json.load(file_obj)
		print(username)
except FileNotFoundError:
	username = input("What is your name?")
	with open(file_name, 'w') as f_obj:
		json.dump(username, f_obj)
		print('We will remember you when you come back,' + username + '!')
else:
	print("welcome back" + username + "!")
