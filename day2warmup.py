import math
#printing a string in reverse
x = 'hello world'
print(x[:5])
#sliced1 = slice(0,6,1)
#sliced2 = slice(5,11,1)
#print(x[sliced2] + x[sliced1])

#printing a user input in reverse
a = input("What is your name? ")
sliced3 = a[::-1]
#sliced3 = slice(len(a), 0, -1)
print("Hello " + sliced3)

#finding the types of some objects
print(type(print))
print(type(len))
print(type(slice))

#finding square roots using math function
x = 33
y = 7
print(x+y)
print(math.sqrt(25))
print(math.sqrt(1))
print(math.sqrt(4))
print(math.sqrt(144))
print(math.sqrt(16))
print(16**1/2)
print(x//y)

#conjoining lists and arrays with two different methods
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(list1 + list2)
print(list1, list2)
array1 = ('hi', 'hello', 'good morning')
array2 = ('how are you', "what's up", 'nothing much')
print(array1 + array2)

#typecasting section where we change data types using a function
number = 55
letter =  '5'
string = '66'
string2 = 'yes sir'
str_number = str(number)
int_letter = int(letter)
float_string = float(string)
upperstr = string2.upper()
print(upperstr)
print(str_number)
print(int_letter)
print(float_string)

#printing out a string one letter at a time
newstring = 'Python'

for letter in newstring:
    print(letter)

#printing an item from a list of objects
print(list1[3])

#checking the python version installed
import sys
print("Python version")
print(sys.version)
print("Version Info.")
print(sys.version_info)