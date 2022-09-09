import json

#json = dictionary yapısı

person_string = '{"name":"ali", "languages":["python","c#"]}'
person_dict = {"name":"ali", "languages":["python","c#"]}

# result=person["name"]
# result=person["languages"]
# result=person["languages"][0]

#JSON string to Dict
# result=json.loads(person_string) #json a çeviririz
# print(type(result))
#result=result["name"]
# result=result["languages"]
# result=result["languages"][0]

# with open("person.json") as f:
#     data=json.load(f)
#     print(data["name"])

# print(result)

# person_dict = {
#     "name":"ali", 
#     "languages":["python","c#"]
# }
#Dict to JSON string
# result=json.dumps(person_dict) #json dan stringe çeviririz.
# print(result)
# print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

person_dict=json.loads(person_string)

result=json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)
