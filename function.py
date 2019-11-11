#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: November 2019
# This program converts temperature in degrees Celsius
#  to temperature degrees Fahrenheit


def celsius_to_fahrenheit():
    # This program converts temperature in degrees Celsius
    #  to temperature degrees Fahrenheit

    # Input
    celsius_degree = input("Please enter the temperature in degrees Celsius: ")

    # Process
    try:
        # The numbers need to be float because we cannot
        #  multiply float by an int
        celsius_degree = float(celsius_degree)
        fahrenheit_degree = 1.8 * celsius_degree + 32.0

        # Output
        print("\nThe temperature in degrees fahrenheit is", fahrenheit_degree)
    except(Exception):
        print("Wrong input!!!")


def main():
    # This function calls other functions
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
