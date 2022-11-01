sentence = "I live and work in Turkey"
print(sentence.capitalize())
print(sentence.replace("Turkey", "USA"))
print(sentence.swapcase())

string = "        interoperability    "
string2 = "interoperability"
print(string.strip())
print(string.rstrip("ty"))
print(string2.rstrip("ty"))
print(string2.lstrip("in"))

text = 'tyou can learn almost everything in pre-classz'
text = text.lstrip("t").rstrip("z").upper()
print(text)