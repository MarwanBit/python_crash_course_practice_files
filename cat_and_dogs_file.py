cat_document = 'cat.txt'
dog_document = 'dogs.txt'

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