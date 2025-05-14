#1. script to calculate the area and perimeter of a rectangle using variables. 
# Defining the length and width of the rectangle
length = 10
width = 5
# Calculating the area and perimeter
area = length * width
perimeter = 2 * (length + width)
# Displaying the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)




#2.  script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
# Take two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Comparing the numbers
if num1 > num2:
    print("First number is greater than the second.")
elif num1 < num2:
    print("First number is less than the second.")
else:
    print("Both numbers are equal.")





#3. script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400). 
# Take a year as input
year = int(input("Enter a year: "))
# Checking that year is leap year or not 
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")





#5. script that concatenates two strings and prints the result.
# Defining  two strings
first_name = "Sai"
last_name = "Thanmaisri"
# Concatenation of 2 strings
full_name = first_name + " " + last_name
# Displaying the result
print("Full name is:", full_name)
 