import json
import write_and_read_json as custom_json_functions

json_file = 'python_text_files/favorite_number.json'

prompt = 'If you want to write a new file type "r"'
prompt +='/nIf you want to read a previous file type "w":'
prompt += '/nIf you want to quit type "q"'

starting_user_input = input(prompt)

main_loop_one_way_flag = True

while main_loop_one_way_flag == True:
	if starting_user_input == 'r':
		custom_json_functions.read_favorite_number_json()
	elif starting_user_input == 'w':
		custom_json_functions.write_favorite_number_json()
	elif starting_user_input == 'q':
		break 
		









