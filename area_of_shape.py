#Add the ability to calculate the area of parallelograms, rhombus, triangles and trapezoids

import math

def get_area(shape):

    Shape = shape.lower()

    if shape == "parallelogram":
        parallelogram_area()
    elif shape == "rhombus":
        rhombus_area()
    elif shape == "triangle":
        triangle_area()
    elif shape == "trapezoid":
        trapezoid_area()
    else:
        print("Please, enter parallelograms, rhombus, triangles or trapezoids ")

def parallelogram_area():
    #formular is breath * height
    breadth = float(input("Enter breadth: "))
    height = float(input("Enter height: "))
    area = breadth * height

    print("The area of the parallelogram is: ", area)

def rhombus_area():
    #formular is (p * q) / 2

    length1 = float(input("Enter value of length: "))
    length2 = float(input("Enter value of the second length: "))
    area = (length1 * length2) / 2

    print("Area of the rhombus is: ", area)


def triangle_area():
    # formular is (base * height) / 2
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = (base * height) / 2

    print("The area of the triangle is: ", area)


def trapezoid_area():
    #formular for trapezoid is (a*b) * 2(h)

    base1 = float(input("Enter value for one base: "))
    base2 = float(input("Enter value for the second base: "))
    height = float(input("Enter value for the height: "))
    area = (base1 * base2) / 2 * height

    print("The area pf the trapezoid is : ", area)


def main():
    shape_type = input("Area of what shape? ")

    get_area(shape_type) #writing a function for shape

main()