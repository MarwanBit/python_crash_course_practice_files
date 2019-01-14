#this prompt is used to ask for someones reason for their affinty of programming
prompt = 'Why do you like programming?:'

#This one-way flag variable is used to create an infinite while loop
one_way_flag = True

#This variable is used to store a file name which holds all responses to the poll
poll_responses = 'poll_responses.txt'

while one_way_flag == True:
	user_input = input(prompt)
	with open(poll_responses, 'a') as poll_responses_file:
		poll_responses_file.write('\n' + user_input)
