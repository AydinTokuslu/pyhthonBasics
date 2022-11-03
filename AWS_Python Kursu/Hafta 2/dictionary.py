state_capitals = { "Arkansas": "Little Rock", 
                   "Colorado": "Denver",
                   "California": "Sacramento",
                   "Georgia": "Atlanta" }
#print(state_capitals)
print(state_capitals["Arkansas"])
# print(state_capitals["Atlanta"])  # sadece keylere bakar, olmadığı için KeyError verir.
#print(state_capitals.items())
state_capitals["Virginia"] = "Richmond"  # yeni bir key-value eklemek
print(state_capitals)

mix_values = {"animal" : ("dog", "cat"),  # tuple
                "planet" : ["Neptun", "Pluton", "Jupyter"],  # liste
                "number" : 40,  # integer
                "pi" : 3.14,  # float
                "is_good" : False  # boolean
}

mix_keys = {22 : "number",
            3.14 : "float",
            True : "boolean",
            "key" : "string"
}


