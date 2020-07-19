'''

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.


'''
# def say_hello():
# 	print("Hello World")


# say_hello()



'''

Functions can be without Arguments


'''
# def say_my_name():

# 	print("My name is Udemezue John")


# say_my_name()



'''

Functions can be with arguemnts


'''

# def say_my_name(name):

# 	print("my name is " + name)


# say_my_name("John")


# def add_two(x , y):

# 	result  = x + y

# 	print(result)

# add_two(5, 9)

'''

Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, 

add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:

'''


def say_my_name(*name):

	print(name)



say_my_name("john", "david", "Jonah", "sherif")
'''

Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, 

add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:

'''










