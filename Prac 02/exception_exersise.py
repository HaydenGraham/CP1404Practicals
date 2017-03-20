try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


print("Finished.")

# Q1: When the entered value is not a number
# Q2 When the fraction is impossible IE when the denominator is 0
# Q3 Check of the denominator is =0 then prompt the user to pick again if its true or add it in the detection






# #Zero Denominator Detector
#  while denominator==0:
#      print("Non valid input")
#      denominator = int(input("Enter a valid denominator: "))
#
