#BMI calculator ro determine if one is overweight or not

name1 = "Koxy"
height_m1 = 2
mass_kg1 = 90

name2 = "Joy"
height_m2 = 1.8
mass_kg2 = 70

name3 = "Steven"
height_m3 = 2.8
mass_kg3 = 100

def bmi_cal(name, height, mass):
    bmi = mass / (height ** 2) #** means square, i.e raise to the power
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " " + "is not overweight" #using + to concatenate two strings
    else:
        return name + "is overweight"
result1 = bmi_cal(name1, height_m1, mass_kg1)
result2 = bmi_cal(name2, height_m2, mass_kg2)
result3 = bmi_cal(name3, height_m3, mass_kg3)

print(result1)
print(result2)
print(result3)