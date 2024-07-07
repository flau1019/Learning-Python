Number = input("Enter a number: ")
Number2 = input("Enter another number: ")

if int(Number) > 5 and int(Number2) < 5:
    print("Number is greater than 5 and second number less than 5")

elif int(Number) < 5 and int(Number2) > 5:
    print("Number is less  than 5 and second number greater than 5")

elif int(Number) < 5 and int(Number2) < 5:
    print("Both numbers less than 5") 

else:
    print("Both numbers greater than 5") 