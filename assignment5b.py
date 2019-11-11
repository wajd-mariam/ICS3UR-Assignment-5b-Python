#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: November 2019
# This program calculates the multiplication table 0-10 of the number entered


def main():
    # counter & answer
    counter = 0
    answer = 0

    # input
    number = input("Enter number to show it's multiplication table:")

    # try & process & output
    try:
        number1 = int(number)

        while counter < 11:
            answer = (counter * number)
            print("{} x {} = {}".format(counter, number, answer))
            counter = counter + 1
    except Exception:
        print("Invalid Input")
    finally:
        print("Thank you for using my program!")


if __name__ == "__main__":
    main()
