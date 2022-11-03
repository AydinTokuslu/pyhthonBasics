# state_capitals = { "Arkansas": "Little Rock", 
#                    "Colorado": "Denver",
#                    "California": "Sacramento",
#                    "Georgia": "Atlanta" }
# #print(state_capitals)
# print(state_capitals["Arkansas"])
# # print(state_capitals["Atlanta"])  # sadece keylere bakar, olmadığı için KeyError verir.
# #print(state_capitals.items())
# state_capitals["Virginia"] = "Richmond"  # yeni bir key-value eklemek
# print(state_capitals)

# mix_values = {"animal" : ("dog", "cat"),  # tuple
#                 "planet" : ["Neptun", "Pluton", "Jupyter"],  # liste
#                 "number" : 40,  # integer
#                 "pi" : 3.14,  # float
#                 "is_good" : False  # boolean
# }

# mix_keys = {22 : "number",
#             3.14 : "float",
#             True : "boolean",
#             "key" : "string"
# }

# my_dictionary = dict(animal = ("dog", "cat"), 
#                     planet = ["Neptun", "Pluton", "Jupyter"],
#                     number = 55)
# print(mix_values.items())
# print(my_dictionary.keys())

school_records={
	'personal_info':
		{'kid':{'tom':{'class':'intermediate', 'age':10},
			'sue':{'class':'elemantary', 'age':8}
			},
		'teen':{'joseph':{'class':'college', 'age':19},
			'marry':{'class':'high school', 'age':16}
			},
		},
}