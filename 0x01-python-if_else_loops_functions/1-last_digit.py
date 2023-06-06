#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number%10 if number >= 0 else number % -10
message = ""
if lastDigit == 0:
   message ="and is 0"
elif lastDigit < 6:
    message = "and is less than 6 and not 0"
else:
    message = "and is greater than 5"
print(f"Last digit of {number:d} is {lastDigit:d} {message:s}")