#a program that converts a list to a tuple

lst = [1, 2, 3, 4] #declare and store a variable
print(type(lst)) #prints the data type called list

tpl = tuple(lst)
print(type(tpl))

#note a tuple cannot be converted to a list or cannot be changed too


#nesting lists within tuples
tpl = (['a', 'b', 'c'], ['d', 'e', 'f'])
print(tpl)

tpl[0].append('z') #adding new list character in the tuple
print(tpl)
tpl[1].remove('f') #removing an element in a list
print(tpl)
