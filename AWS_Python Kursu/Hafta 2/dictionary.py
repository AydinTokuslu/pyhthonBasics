state_capitals = {"Arkansas": "Little Rock", 
                  "Colorado": "Denver",
                  "California": "Sacramento",
                  "Georgia": "Atlanta"}
#print(state_capitals)
print(state_capitals["Arkansas"])
# print(state_capitals["Atlanta"]) #sadece keylere bakar, olmadığı için KeyError verir.
#print(state_capitals.items())
state_capitals["Virginia"] = "Richmond"
print(state_capitals)
