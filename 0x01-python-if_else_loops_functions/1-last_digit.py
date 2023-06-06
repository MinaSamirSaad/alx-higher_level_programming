#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number%10 if number >=0 else number % -10
message = ""
if last_digit == 0:
    message ="and is zero"
elif last_digit >= 6:
    message= "and is greater than 5"
else:
    message ="and is less than 6 and not 0"
print(f"Last digit of {number:d} is {last_digit:d} {message:s}")