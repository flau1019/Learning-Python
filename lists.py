import random

mylist = [1, 2, 3, 4, 5]
my2ndlist = ["asdf", "sdfg", "dfhg", 3]

print(mylist)
print(mylist[3])
number = mylist[3] + my2ndlist[3] + my2ndlist[-1]
print(number)
print(my2ndlist[1:3])
mylist.append(number)
print(mylist)
random.shuffle(mylist)
print(mylist)
my2ndlist.insert(1, 3)
my2ndlist.extend(mylist)
print(my2ndlist)
print(my2ndlist.index(3))
copy = my2ndlist.copy()
print(copy)

