#checking if certain things are true about a string using is_alpha() and is_digit() by printing true or false
#checking if a user put in the correct type of a data string

birth_year = "1980"
state = "VA"

print(birth_year.isdigit()) #prints true
print(state.isalpha()) #prints true

born_year = "july 1980"
state = "10 Delta"

print(born_year.isdigit()) #returns false
print(state.isalpha()) #returns/prints false