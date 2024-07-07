    

try:
    answer = 5 / 0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError:
    print("You can't divide by zero!")

except ValueError:
    print("You can't divide by a string")

finally:
    print("This will run no matter what")

print("This will run no matter what")

for i in range(5):
    print(i)