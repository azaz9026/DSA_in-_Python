## Sum of Digit ----------------------------------------------------------------------------------------------------------------------------------


def sum_of_digits(number):
    # Convert the number to a string to iterate through its digits
    str_number = str(number)

    # Initialize a variable to store the sum
    digit_sum = 0

    # Iterate through each digit and add it to the sum
    for digit in str_number:
        digit_sum += int(digit)

    return digit_sum

# Example usage:
number_to_sum = 12345
result = sum_of_digits(number_to_sum)
print(f"The sum of the digits of {number_to_sum} is: {result}")


# Ans -> The sum of the digits of 12345 is: 15


## Another Method----------------------------------------------------------------------------------------------------------------------------------------


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

# Example usage:
number_to_sum = 12345
result = sum_of_digits(number_to_sum)
print(f"The sum of the digits of {number_to_sum} is: {result}")


# Ans -> The sum of the digits of 12345 is: 15