s = "name"
print(s[::-1])

print(s.index("a"))

def email_gen(name):
	"""FLow of code:
	input = "harshal dev"
	therefore, first_letter = 'h'
	and reverse_str = 'dev harshal'
	first_space = gives the index of the first space in the reveresed name , ie here = 3 
	reversed surname = ved ,
	surname = reversed_surname ko seedha karna hai , ie dev ho gaya 
	now then we put our "first_letter" + "surname" + @company.com
	and then return the email
	"""
	first_letter = name[:1].lower()

	reverse_str = name[::-1] #name ko ulta kr dia poora

	first_space = reverse_str.index(" ") #ulte naam me pehla space dhooondh raha hu

	reversed_surname = reverse_str[:first_space] #ulta surname bana dia

	surname = reversed_surname[::-1].lower() #ulte surname ko seedhe kar rahe hai

	email = first_letter+surname+"@company.com" #email ka format genreate kr rahe hai 

	return email #email ko return kra rahe hai
	


print(email_gen("HARSHAL DEV"))


