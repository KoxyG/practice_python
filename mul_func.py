def solv_eq(equation):
    x, mul, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int (num2)
    return "x = ", str(num2 / num1) #dividing both side by 3
print(solv_eq("x * 3 = 9"))



def mult_divide(num1, num2):
    return (num1 * num2), (num2 / num1)
mult, divide = mult_divide(5, 4)

print("5 * 2 =", mult)
print("5 / 2 =", divide)

