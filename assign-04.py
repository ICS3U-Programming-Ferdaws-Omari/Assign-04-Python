#!/usr/bin/env python3
# Created By: Ferdaws
# Date: May 2022
# This program displays the time table of number entered from 0 to 10


def main():
    count = -1
    # Get the user number and convert it to an int.
    try:
        user_number = int(input("Enter a positive number: "))
        # While statement
        while count < 10:
            # Check if the number is negative
            if user_number < 0:
                print("Your number cannot be negative!")
                break
            else:
                # Calculate and display the time table
                count = count + 1
                product = user_number * count
                print(user_number, "x", count, "=", product)
    # Catch invalid input
    except Exception:
        print("Invalid input")


if __name__ == "__main__":
    main()
