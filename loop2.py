#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
# This program uses a while loop


def main():

    # input
    positive_integer = print("  Enter how many times to repeat ")
    positive_string = input("Enter Here plz : ")
    loop_counter = 0
    number_factorial = 1

    # process & output
    try:
        positive_integer = int(positive_string)

        while loop_counter < positive_integer:
            loop_counter = loop_counter + 1
            number_factorial = number_factorial * loop_counter
        print("The factorial of {0} is {1}".format(num, number_factorial))

    except Exception:
        print("This was an invalid number ")


if __name__ == "__main__":
    main()
