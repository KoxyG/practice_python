#a function checks is a value is float or not

num_3 = "3.13"
def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False

print("is pi a float :", isfloat(num_3))