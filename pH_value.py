#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Get pH value condition | ----\n", fg("red")))

# user interaction
pH_value = float(input("Enter pH value (0 <= value <= 14): "))

# function
def get_condition(value):
    if value < 0 or value > 14:
        exit("\nInvalid Input\n")
    elif value == 7:
        return stylize("neutral", fg("green_3b"))
    elif value < 7:
        return stylize("acidic", fg("red"))
    elif value > 7:
        return stylize("alkaline", fg("purple_4a"))

# output
condition = get_condition(pH_value)
print(f"\nThe pH value {pH_value} is {condition}.\n")
