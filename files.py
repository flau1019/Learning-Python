try:
    file = open("textfile.txt", "r")
    s = file.read()
    print(s)

except FileNotFoundError:
    print("Where da file at")


finally:
    file.close()