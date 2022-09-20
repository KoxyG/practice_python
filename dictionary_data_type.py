#syntax:    variable_name ={key1: value1, key2: value 2,...}
#creating dictionaries

d1 = {}
print(d1)
print(type(d1)) #prints type as dict

d2 = {1:"Welcome", 2:"to",3:"Python",4:"tutorials"}
print(d2)

d3 = {"name":"Sam", "age":22, "profession":"student"} #putting the keys in double quote because its a string
print(d3)

d4 = dict({"name":"Sam", "age":22, "profession":"student"})

#nesting dictionaries
d5 = {"name":{"first":"Sam","last":"king"}, "age":22, "profession":"student"}
print(d5)

#adding element
d = {}
d[0] = "welcome"
d[1] = ("How", "are you")
print(d)
d["name"] = {"first":"Sam", "last":"Crew"} #the will be added to the dictionaries
print(d)