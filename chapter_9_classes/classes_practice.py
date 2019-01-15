class User():
	
	def __init__(self, first_name, last_name, age, gender):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.gender = gender
		self.user_dictionary = {}
		self.login_attempts = 0
		
	def describe_user(self):
		self.user_dictionary = {
					'first name' : str(self.first_name),
					'last name' : str(self.last_name),
					'age' : str(self.age),
					'gender' : str(self.gender)
						}
		print("\n" + str(user_dictionary))
		
	def increment_login_attempts(self):
		self.login_attempts += 1 
	
	def reset_login_attempts(self):
		self.login_attempts = 0

class Privileges():
	'''
	This class is a subclass of User which gives specific methods
	and objects dealing with admin privileges
	'''
	def __init__(self):
		self.privileges =  [
							'editing',
							'kicking',
							'can delete posts',
							'launching an investigation'
							]

	def show_privileges(self):
		print(self.privileges)
		
class Admin(User):
	
	def __init__(self, first_name, last_name, age, gender):
		super().__init__(first_name, last_name, age, gender)
		self.admin_privileges = Privileges()



user_1 = Admin("marwan", "bit", 16, "Male")
user_1_privileges = Privileges()
user_1.admin_privileges.show_privileges()
		
	
		    


		
		
		
