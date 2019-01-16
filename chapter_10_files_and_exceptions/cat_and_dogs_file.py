cat_document = 'C:/Users/Shadow/Documents/GitHub/python_crash_course_practice_files/chapter_10_files_and_exceptions/python_text_files/cat.txt'
dog_document = 'C:/Users/Shadow/Documents/GitHub/python_crash_course_practice_files/chapter_10_files_and_exceptions/python_text_files/dogs.txt'

with open(cat_document, 'r') as cat_document:
	cat_document_lines = cat_document.readlines()
	for line in cat_document_lines:
		try:
			print(line.strip())
		except FileNotFoundError:
			pass

print('---------------------------------------------')

with open(dog_document, 'r') as dog_document:
	dog_document_lines = dog_document.readlines()
	for line in dog_document_lines:
		try:
			print(line.strip())
		except FileNotFoundError:
			pass