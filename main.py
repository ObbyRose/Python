# import random
# print("hello world")
# #python is awesome

# if True:
#     print("Python is awesome")
#     print("Hello World")
# """ 
# lorem

# """
# # This function will print my name

# print(" my name is Tal ")

# """ 
# My final project is a spotify clone 
# I will be using the spotipy api to get the data
# I will be using the tkinter library to create the GUI
# I will be using the pygame library to play the music
# I will be using the requests library to get the data

# """

# # DATA TYPES

# message = "Hello World"

# print(message)

# """

# # Integer
# integer_example = 42
# print(integer_example)

# # You can perform arithmetic operations
# print(integer_example + 10)
# print(integer_example - 10)
# print(integer_example * 2)
# print(integer_example / 2)

# # Float
# float_example = 3.14
# print(float_example)

# # You can perform arithmetic operations
# print(float_example + 1.86)
# print(float_example - 1.14)
# print(float_example * 2)
# print(float_example / 2)

# # String
# string_example = "Hello, Python!"
# print(string_example)

# # You can concatenate strings
# print(string_example + " How are you?")

# # You can repeat strings
# print(string_example * 2)

# # Boolean
# boolean_example = True
# print(boolean_example)

# # You can use booleans in logical operations
# print(boolean_example and False)
# print(boolean_example or False)
# print(not boolean_example)

# # List
# list_example = [1, 2, 3, 4, 5]
# print(list_example)

# # You can access elements by index
# print(list_example[0])

# # You can append elements
# list_example.append(6)
# print(list_example)

# # You can remove elements
# list_example.remove(3)
# print(list_example)

# # Tuple
# tuple_example = (1, 2, 3, 4, 5)
# print(tuple_example)

# # You can access elements by index
# print(tuple_example[0])

# # Tuples are immutable, so you cannot change them

# # Dictionary
# dictionary_example = {"name": "Alice", "age": 30}
# print(dictionary_example)

# # You can access values by key
# print(dictionary_example["name"])

# # You can add new key-value pairs
# dictionary_example["city"] = "Wonderland"
# print(dictionary_example)

# # You can remove key-value pairs
# del dictionary_example["age"]
# print(dictionary_example)

# # Set
# set_example = {1, 2, 3, 4, 5}
# print(set_example)

# # You can add elements
# set_example.add(6)
# print(set_example)

# # You can remove elements
# set_example.remove(3)
# print(set_example)

# # Sets do not allow duplicate elements
# set_example.add(1)
# print(set_example)

# # NoneType
# none_example = None
# print(none_example)

# # None is used to represent the absence of a value
# integer_example = 42
# print(integer_example)

# """
# shampoo = 5
# conditioner = 4
# soap = 6
# total = shampoo + conditioner + soap
# print(total)

# x = 54

# if x > 1 and x < 100:
#     print("x is between 1 and 100") 
# user = ''
# user_name = input("Please enter your name: ")
# user_age = input("Please enter your age: ")
# user = user_name + " " + user_age

# print(f"Hello {user}")

# for i in range(5):
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     summary = number + number
# print(summary)

#Q1
# number1 = 10
# number2 = 321
# summary = number1 + number2
# differnece = number1 - number2
# product = number1 * number2
# quotient = number1 / number2

# print("Summary: ", summary, "Difference: ", differnece, "Product: ", product, "Quotient: ", quotient)

#Q2

# number3 = int(input("Please enter a number: "))
# squared_number = number3 ** 2

# print(f"Squared number of {number3}: ", squared_number)

#Q4
# celsius_temparture = 32
# convert_to_farenheit = (celsius_temparture * 9/5) + 32
# print(f"{celsius_temparture} degrees celsius is equal to {convert_to_farenheit} degrees farenheit")

#Q5
# radius_of_circle = 5
# area_of_circle = 3.14159 * (radius_of_circle ** 2)
# print(f"Area of circle with radius {radius_of_circle} is {area_of_circle}")

#Q6
number = 32
if number % 2 == 0:
    print("Number is even")
else: 
    print("Number is odd")

#Q7
# vowels = ['a', 'e', 'i', 'o', 'u']
# letter = input("Please enter a letter: ")
# if letter in vowels:
#     print("Letter is a vowel")
# else:
#     print("Letter is a consonant")

#Q8
# number = int(input("Please enter a number: "))
# if number > 0:
#     print("Number is positive")
# elif number > 0:
#     print("Number is negative")
# else:
#     print("Number is zero")

# #Q9
# year = int(input("Please enter a year: "))
# if year % 4 == 0:
#     print("Year is a leap year")

# #Q10
# grade = int(input("Please enter your grade: "))
# if grade >= 90:
#     print("A")
# elif grade >= 80:
#     print("B")
# elif grade >= 70:
#     print("C")
# elif grade >= 60:
#     print("D")
# else:
#     print("F")

#Q11
# for number in range(1, 11):
#     print(number)

#Q12
# sum = 0
# number = int(input("Please enter a number: "))
# for i in range(1, number):
#     sum += i
# print(sum)

#Q13
# factorial = int(input("please enter a number: "))
# result = 1
# while factorial > 0:
#     result *= factorial
#     factorial -= 1
# print(f"The factorial is {result}")

#Q14
Countdown = 10
while Countdown > 0:
    print(Countdown)
    Countdown -= 1
    if Countdown == 0:
        print("Blast off!")

#Q15
# numbers1 = int(input("Please enter the 1st number: "))
# numbers2 = int(input("Please enter the 2nd: "))
# numbers3 = int(input("Please enter the 3rd number: "))

# if numbers1 > numbers2 and numbers1 > numbers3:
#     print(f"{numbers1} is the largest number")
# elif numbers2 > numbers1 and numbers2 > numbers3:
#     print(f"{numbers2} is the largest number")
# else:
#     print(f"{numbers3} is the largest number")

# #Q16
# is_palindrome = input("Please enter a word: ")
# if is_palindrome == is_palindrome[::-1]:
#     print("Word is a palindrome")


# #Q17
# n = int(input("Please enter a number: "))
# a, b = 0, 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b

#Q18
# for i in range(1,51):
#     if i%3 == 0 and i%5 == 0:
#         print(f"{i} is divisble by 3 and 5")

#Q19
# is_prime = int(input("Please enter a number: "))
# if is_prime > 1:
#     for i in range(2, is_prime):
#         if is_prime % i == 0:
#             print("Number is not prime")
#         else:
#             print("Number is prime")

# import random
# random_number = random.randint(1, 100)
# guess_number = int(input("Please enter a number between 1 and 100: "))
# while guess_number != random_number:
#     if guess_number < random_number:
#         print("Number is too low")
#     else:
#         print("Number is too high")
#     guess_number = int(input("Please enter a number between 1 and 100: "))

# user_pin = 1234
# user_balance = 1000
# user_name = "Maman"
# input_pin = int(input("Please enter your pin: "))

# if input_pin == user_pin:
#     withraw_or_deposit = input(f" Hello {user_name} Would you like to withdraw or deposit? ")
#     if withraw_or_deposit == "withdraw":
#         withdraw_amount = int(input("How much would you like to withdraw? "))
#         if withdraw_amount <= user_balance:
#             user_balance -= withdraw_amount
#             print(f"Money Withdrawn, your new balance is {user_balance}$")
#         else:
#             print("Insufficient funds")
#     else:
#         deposit_amount = int(input("How much would you like to deposit?"))
#         user_balance += deposit_amount
#         print(f"Money Deposited, your new balance is {user_balance}$")
# else:
#     print("Invalid pin")

number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
operator = input("Please enter the operation you would like to perform +, -, *, /: ")
if operator != "+" and operator != "-" and operator != "*" and operator != "/":
    print("Invalid operation")
elif operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Invalid operation")