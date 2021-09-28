#!/usr/bin/env python3

message = 'You are flying simulated '

# wrap connection in a float() to accept decimals as numbers
speed = float(input("What is your speed in MPH?"))

# if input value was higher or equal to 900
if speed >= 900:
    message = message + 'Apollo rocket.'
elif speed >= 500:
    message = message + 'SR71.'
elif speed >= 300:
    message = message + 'F14.'
else:
    message = message + 'Kite.'
print(message)
