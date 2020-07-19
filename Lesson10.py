
'''

Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

'''
# class Church:

# 	pastor = 1

# 	ushers = 10

# 	choir  = 15


# Rccg = Church()


# Mfm  = Church()

# cac = Church()





# print(Rccg.pastor)

# print(Rccg.choir)

# print(Mfm.pastor)









'''
All classes have a function called __init__(), 


which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, 

or other operations that are necessary to do when the object is being created:


'''

# class Church:

# 	def __init__(self, pastor, ushers, choir):

# 		self.pastor = pastor

# 		self.ushers = ushers

# 		self.choir = choir



# Rccg =  Church(40, 4000, 90000)

# Mfm = Church(5000, 20, 50)

# print(Rccg.pastor)

# print(Rccg.ushers)

# print(Mfm.pastor)















'''

Objects can also contain methods. 


Methods in objects are functions that belong to the object.


'''
class Church:

	def __init__(self, pastor, ushers, choir):

		self.pastor = pastor

		self.ushers = ushers

		self.choir = choir

	def add_all(self):

		result = self.pastor + self.ushers + self.choir

		print(result)



Rccg =  Church(40, 4000, 90000)

Mfm = Church(5000, 20, 50)

print(Rccg.pastor)

print(Rccg.add_all())

print(Mfm.add_all())

'''

Inheritance allows us to define a class that inherits 

all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

'''


class Mosque(Church):

	pass 




Anwarul = Mosque(4000, 3 , 6)

print(Anwarul.pastor)










