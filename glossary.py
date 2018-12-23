python_glossary = {
	'variable' : 'an item that stores a value',
	'list comprehension' : 'a single line of code used to create a list',
	'loop' : 'a mechanic which repeats instructions under certain conditions',
	'dictionary' : 'a list which attaches values to keys',
	'string' : 'a collection of alphanumerical characters',
	'method' : 'an abstraction of directions that can be applied to data',
	'if statement' : 'a method to define instructions under certain conditions',
	'else statement' : 'a method to define instructions when certain conditions are not met',
	}

for term, definition in python_glossary.items():
	print('the term' +
	 ' ' + 
	 str(term) + 
	 ' means ' + 
	 ': ' +
	str(definition))

