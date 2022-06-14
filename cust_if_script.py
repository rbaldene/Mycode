#!/usr/bin/env python3

score = float(input("Enter your score: "))
message = ' Your final grade is '

if score >= 90:
    message = message + 'an A, great job!'

elif score >= 80:
    message = message + 'a B, nice work.'

elif score >= 70:
    message = message + 'a C, you passed.'

elif score >= 60:
    message = message + 'a D, you need to attend summer school.'

elif score <= 59:
    message = message + 'a F, you SUCK!!'

print(message)
