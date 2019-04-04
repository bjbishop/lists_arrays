#!/usr/bin/env python3

#########
# lists #
#########

# Build a list of string elements.  Make them names of some sort.  --
# ensure your list has at least 6 elements
# Suggestions:  Team Members, Superheros, Pets, etc.
# Requirement:  Must include “Wolverine”
# Requirement:  Cannot include “Hamburglar”
# Print out all list items

my_list = ["Bryan", "Amanda", "JiSeob", "YeongHo", "Lillian", "Wolverine"]

for name in my_list:
    print(name)


# How are list elements defined/numbered?
# Print out a specific element in the list.

# indexed by starting with 0
print(my_list[0])  # => Bryan
print(my_list[-1])  # => Wolverine, -1 is the last entry in the list


# Add to the list
# Append to the end
# Replace the 4th value in the list with “Hamburglar”

my_list.append("Geddy")
my_list[3] = "Hamburglar"
print(my_list[3])  # => Hamburglar

# Remove an element by index value
# Remove the third element
# What index was used.
# 2, since the array starts at 0
del my_list[2]  # => Removes JiSeob

# Remove an element by element content
my_list.remove("Geddy")


# Challenge:  How can you count the number of elements in a list?
# Show an example
# What do you notice about the count?  Is it different from the index values?
# Print the content of the last element in the list, using the count you found in your print statement.

print(len(my_list))  # => 5
# returns 5 items, one more than the index of the last item, since the array starts at 0
last = len(my_list)
print(my_list[last-1])
# or
print(my_list[-1])
# Additional Challenge:  Pop an element (Wolverine), to reuse this element for another task.
# Print the original list to show that the pop was successful.
# Print a sentence using the popped element.

print("Original my_list contained these items: " + str(my_list))
var1 = my_list.index("Wolverine")
print("Saving the index of Wolverine: " + str(var1))
var2 = my_list.pop(var1)
print("New my_list now contains these items: " + str(my_list))
print("Popped element number " + str(var1) +
      " contained the name " + str(var2))


##########
# tuples #
##########


# Explain the conceptual difference between a list and a tuple

# Tuples are immutable, so items inside can't be changed
# Constructed with ( )

# Show how a tuple is created, and discuss the difference from a list

my_other_list = [1, 2, 3]
my_other_list[0] = "banana"
my_tuple = (1, 2, 3)
# can't update items in the tuple but can contain mutable items
# >>> a = (1, ['a', 'b', 'c'], 2)
# >>> a[1]
# ['a', 'b', 'c']
# >>> a[1].append('d')
# >>> a[1]
# ['a', 'b', 'c', 'd']
# >>> a
# (1, ['a', 'b', 'c', 'd'], 2)

# Challenge:
# What happens when you try to add to a tuple?
# no append method on tuples
# What happens when you try to replace a tuple member?
# TypeError: 'tuple' object does not support item assignment


#########
# loops #
#########


# Nest a for loop inside your for loop.
# Create an additional list, which has the same number of elements as your original name list.  For this list, put random astrological signs (aries, gemini, leo, etc) as the list elements.

import random
signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
         "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
signs_shuffled = random.sample(signs, len(signs))


for name in my_list:
    for sign in signs:
        print(f"{name} is a {sign}, doncha know.")

# Do not print anything for the outer (name) for loop, do the following for the nested (astrological) for loop:
# Print the following statement for each iteration of the astrological list:  “{name} is a {astrological sign}, doncha know.”
# What do you notice about this approach?

# It prints each name next to each sign:
# Example:
# Wolverine is a Aries, doncha know.
# Wolverine is a Taurus, doncha know.
# Wolverine is a Gemini, doncha know.
# Wolverine is a Cancer, doncha know.
# Wolverine is a Leo, doncha know.
# Wolverine is a Virgo, doncha know.
# Wolverine is a Libra, doncha know.
# Wolverine is a Scorpio, doncha know.
# Wolverine is a Sagittarius, doncha know.
# Wolverine is a Capricorn, doncha know.
# Wolverine is a Aquarius, doncha know.
# Wolverine is a Pisces, doncha know.


# Does this seem to fit a normal usage pattern of nesting loops?
# ??

# If you answered Yes, quantify your answer publicly to the closest wall, then profess your love for Windows ME, arguing that Pearson should adopt this OS as their corporate standard.

# If you said No, consider working on the following Stretch:
# Find a way to assign a birth date (Month/day) to each of the
# characters in your name list. In your nested loop, build conditional
# logic which assigns the proper Zodiac based on the character’s birth
# date.

import datetime


def get_day_of_year(y, m, d):
    return(datetime.datetime(y, m, d).timetuple().tm_yday)


def range_between_dates(y1, m1, d1, y2, m2, d2):
    from_day = get_day_of_year(y1, m1, d1)
    to_day = get_day_of_year(y2, m2, d2) + 1
    if y2 > y1:
        first_part = range(get_day_of_year(y1, m1, d1),
                           get_day_of_year(y1, 12, 31) + 1)
        second_part = range(get_day_of_year(y2, m2, d2) + 1)
        return([first_part, second_part])
    else:
        return([(range(from_day, to_day))])


my_new_list = [
    ["Bryan", get_day_of_year(2019, 11, 29)],
    ["Amanda", get_day_of_year(2019, 11, 21)],
    ["JiSeob", get_day_of_year(2019, 6, 4)],
    ["YeongHo", get_day_of_year(2019, 11, 8)],
    ["Lillian", get_day_of_year(2019, 4, 16)],
    ["Wolverine", get_day_of_year(2020, 1, 1)]
]


my_new_signs = [
    ["Aries", range_between_dates(2019, 3, 21, 2019, 4, 19)],
    ["Taurus", range_between_dates(2019, 4, 20, 2019, 5, 20)],
    ["Gemini", range_between_dates(2019, 5, 21, 2019, 6, 21)],
    ["Cancer", range_between_dates(2019, 6, 21, 2019, 7, 22)],
    ["Leo", range_between_dates(2019, 7, 23, 2019, 8, 22)],
    ["Virgo", range_between_dates(2019, 8, 23, 2019, 9, 22)],
    ["Libra", range_between_dates(2019, 9, 23, 2019, 10, 22)],
    ["Scorpio", range_between_dates(2019, 10, 23, 2019, 11, 21)],
    ["Sagittarius", range_between_dates(2019, 11, 22, 2019, 12, 21)],
    ["Capricorn", range_between_dates(2019, 12, 22, 2020, 1, 19)],
    ["Aquarius", range_between_dates(2020, 1, 20, 2020, 2, 18)],
    ["Pisces", range_between_dates(2020, 2, 19, 2020, 3, 20)],
]


for name in my_new_list:
    for sign in my_new_signs:
        for r in sign[1]:
            if name[1] in r:
                print(
                    f"The astrogical sign for {name[0]} in 2019-2020 is: {sign[0]}")


# The astrogical sign for Bryan in 2019-2020 is: Sagittarius
# The astrogical sign for Amanda in 2019-2020 is: Scorpio
# The astrogical sign for JiSeob in 2019-2020 is: Gemini
# The astrogical sign for YeongHo in 2019-2020 is: Scorpio
# The astrogical sign for Lillian in 2019-2020 is: Aries
# The astrogical sign for Wolverine in 2019-2020 is: Capricorn


# Stretch “for loop” Challenge:  Research how to create a local directory on your computer, using Python.
# Choose, and define, your starting path:  c:\temp,  %userprofile%, HOME, , /tmp, etc
# Create a directory for each element in your list

import os

my_dirs = ["alpha", "bravo", "charle", "delta", "echo", "foxtrot"]

for dir in my_dirs:
    try:
        os.mkdir("one" + "/" + dir)
    except FileExistsError:
        pass
