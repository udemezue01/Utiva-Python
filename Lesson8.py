'''
A dictionary is a collection which is unordered, changeable and indexed. 

In Python dictionaries are written with curly brackets, and they have keys and values.

'''

clubs = {
		
	"Arsenal":"The Gunners",

	"Man U"	: "The Reds",

	"Chelsea": "The Blues",

	"Liverpool":"Chicken",

}

'''
Indexing Dictionaries

'''

# print(clubs["Arsenal"])
# print(clubs["Chelsea"])


'''

Adding Items to a dictionary
'''

# clubs["Man city"] = "The killers"

# clubs["Leicerst"] = "The Murderers"

# print (clubs)


'''
Removing an Item In a dictionary

'''


clubs.pop("Chelsea")
print(clubs)

