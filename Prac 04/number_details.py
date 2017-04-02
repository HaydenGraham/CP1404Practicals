import math
NUMBERS_ASKED = int(5)
numbers_recieved=[]
for x in range (0,NUMBERS_ASKED):
    numbers_recieved += input("What is your number?")
print (numbers_recieved)
print("The first number is " + numbers_recieved[0])
print("The last number is " + numbers_recieved[-1])
print("The smallest number is " + min(numbers_recieved))
print("The largest number is " + max(numbers_recieved))
print("The average of the numbers is " + sum(numbers_recieved)/NUMBERS_ASKED)
