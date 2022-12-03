import math

fruits = {'fruit': 'apple', 'colour': 'green'}


def divide_or_square(number):
    if number % 5 == 0:
        print(math.sqrt(number))
    else:
        print(number % 5)


def longest_value(dictionary):
    longest_word = ""
    for item in dictionary:
        if len(dictionary[item]) > len(longest_word):
            longest_word = dictionary[item]
    print(longest_word)


longest_value(fruits)
