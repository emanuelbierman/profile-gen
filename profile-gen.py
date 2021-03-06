

class Profile:
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.dob = []
		# create a dob dict with keys date, month, yeat
		self.age = 0
		self.email_pri = 'primary email'
		self.email_sec = 'No secondary email entered'

	def age_calc(self):
		self.dob = input("Enter your date of birth (MM/DD/YYYY): ").split('/')
		new_age = (2018 - int(self.dob[2]))
		self.age = new_age

	def legal(self):
		return self.age >= 18

	def email_gen(self):
		new_email = input("Enter your primary email address: ")
		if '@' in new_email:
			self.email_pri = new_email
		else:
			new_email = input("Please enter a valid email address: ")
		
		new_email = input("Enter a secondary email address, or type n to continue: ")
		if '@' in new_email:
			self.email_sec = new_email
		elif new_email == 'n':
			pass
		else: 
			new_email = input("Please enter a valid email address: ")

	def prof_disp(self):
		f"""	Here is the information you entered:
				Name: {self.first_name} {self.last_name}
				DOB: {self.dob} Age: {self.age}
				Email: {self.email_pri} {self.email_sec}
				Thank you for creating your profile.

				"""

	def prof_mod(self):
		modify = int(input("To modify your date of birth, enter 1. To modify your email addresses, enter 2. "))
		if modify == 1:
			self.age_calc()
		elif modify == 2:
			self.email_gen()
		else:
			self.prof_disp()
			# I'm having trouble calling these methods from within the class def.

def new_profile():
	begin = input("Do you want to create a new profile? y/n: ")
	if begin.strip() != 'y':
		print("why, I never!")
		#  how do I get this to end the function?

	new_name = input("Enter your name (you will not be able to mofidy this once it is entered): ").split()
	
	new_profile = Profile(new_name[0], new_name[1])

	new_profile.age_calc()

	if new_profile.legal() == False:
		print("""
		You should be 18 or older to create a profile.
		Go ask your parents for permission to continue.
		""")
		return
	
	new_profile.email_gen()

	print("Welcome, {}. ".format(new_profile.first_name))

	new_profile.prof_disp()

	new_profile.prof_mod()

new_profile()