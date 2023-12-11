## Fibonacci series----------------------------------------------------------------------------------------------------------------------------


def fibonacci(number_of_terms):
    if number_of_terms == 0 or number_of_terms == 1:
        return number_of_terms
    else:
        return fibonacci(number_of_terms-1) + fibonacci(number_of_terms-2)

# Example usage:
number_of_terms = 10
result = fibonacci(number_of_terms)
print(f"The Fibonacci series up to {number_of_terms} terms is: {result}")


## Ans -> The Fibonacci series up to 10 terms is: 55