customer = "Asha Menon" # string can be single or double quotes
attempts = 3 # integer
is_urgent = True # boolean
price = 12.25 # float

print(customer, type(customer))
print(attempts, type(attempts))
print(is_urgent, type(is_urgent))
print(price, type(price))

# String formatting - Comments ignored by Python
summary = f"{customer} has tried {attempts} times. Urgent: {is_urgent}. Price: {price}"
print(summary)

# string in multiple lines
"""Assignment 1:
create a variable like this:
word1 : twinkle
word2 : star

Create a Rhyme like this (using string formatting):
 twinkle twinkle little star
 how i wonder what you are
 up above the world so high
 like a diamond in the sky
 twinkle twinkle little star
 how i wonder what you are
"""

word1 = "twinkle"
word2 = "star"
rhyme = f"{word1} {word1} little {word2} how i wonder what you are, up above the world so high ,like a diamond in the sky, {word1} {word1} little {word2} how i wonder what you are"
print(rhyme)

solution_approach_2 = f"""
 {word1} {word1} little {word2} how i wonder what you are, 
 up above the world so high ,like a diamond in the sky,
 {word1} {word1}little {word2} how i wonder what you are
"""

print(solution_approach_2)

import keyword
print("Keywords in Python:")
print(keyword.kwlist)

True = 10

""" Notes:
Variables:
- Variables are case sensitive, cannot be keywords
- Should not start with a number
- can start with letter or underscore
- should not contain spaces or special characters
"""