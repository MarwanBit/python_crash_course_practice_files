
class ClassWithoutParameters:

	def __init__(self):

		self.descriptions = "I'm a class w/o parameters"

	def description(self):

		print(str(self.descriptions))


obj = ClassWithoutParameters()
obj.description()