
## Sum of Adding Digits ----------------------------------------------------------------------------------------------------------------------------


def add_digits(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

# Example usage:
number_to_add = 12345
result = add_digits(number_to_add)
print(f"The single-digit result of adding the digits of {number_to_add} is: {result}")

## Ans -> The single-digit result of adding the digits of 12345 is: 6


## Another Method----------------------------------------------------------------------------------------------------------------------------------------


def add_digits_math(n):
    if n == 0:
        return 0
    elif n % 9 == 0:
        return 9
    else:
        return n % 9

# Example usage:
number_to_add = 12345
result = add_digits_math(number_to_add)
print(f"The single-digit result of adding the digits of {number_to_add} is: {result}")

## Ans -> The single-digit result of adding the digits of 12345 is: 6


## Another Method----------------------------------------------------------------------------------------------------------------------------------------


def add_digits_recursive(n):
    if n < 10:
        return n
    else:
        return add_digits_recursive(sum(int(digit) for digit in str(n)))

# Example usage:
number_to_add = 12345
result = add_digits_recursive(number_to_add)
print(f"The single-digit result of adding the digits of {number_to_add} is: {result}")

## Ans -> The single-digit result of adding the digits of 12345 is: 6
