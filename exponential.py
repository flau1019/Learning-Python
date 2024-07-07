
x = float(input("Enter a base number: "))
y = int(input("Enter an exponent: "))


def exponential(x, y):
    temp = 1
    for i in range(y):
        temp = temp*x
    return temp

print(exponential(x, y))