## alternating digit sum ------------------------------------------------------------------------------------------------------


def alternating_digit_sum(number):
    str_number = str(number)
    even_sum = sum(int(digit) for digit in str_number[::2])  # Even-positioned digits
    odd_sum = sum(int(digit) for digit in str_number[1::2])  # Odd-positioned digits
    return even_sum - odd_sum

# Example usage:
number_to_sum = 12345
result = alternating_digit_sum(number_to_sum)
print(f"The alternating digit sum of {number_to_sum} is: {result}")

## Ans-> The alternating digit sum of 12345 is: 3


## another method ---------------------------------------------------------------------------------------------------------------



def alternating_digit_sum(n):
    str_number = str(n)
    even = 0
    odd = 0

    for i in range(len(str_number)):
        digit = int(str_number[i])
        if i % 2 == 0:
            even += digit
        else:
            odd += digit
    
    return even - odd



# Example usage:
number_to_sum = 12345
result = alternating_digit_sum(number_to_sum)
print(f"The alternating digit sum of {number_to_sum} is: {result}")


## Ans-> The alternating digit sum of 12345 is: 3