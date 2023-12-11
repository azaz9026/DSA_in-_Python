## Climbing Stairs problem-----------------------------------------------------------------------------------------------------------------------------


def climbStairs(n):
    if n <= 3:
        return n
    else:
        return climbStairs(n-1) + climbStairs(n-2)

# Example usage:
number_of_stairs = 5
result = climbStairs(number_of_stairs)
print(f"There are {result} distinct ways to climb {number_of_stairs} stairs.")


## Ans -> There are 8 distinct ways to climb 5 stairs.



## Another Method----------------------------------------------------------------------------------------------------------------------------------------


def climbStairs(n):
    if n == 1:
        return 1
    
    num1 = 1
    num2 = 2

    for i in range(3, n + 1):
        num3 = num1 + num2

        num1 = num2
        num2 = num3
        
    return num2

# Example usage:
number_of_stairs = 5
result = climbStairs(number_of_stairs)
print(f"There are {result} distinct ways to climb {number_of_stairs} stairs.")

## Ans -> There are 8 distinct ways to climb 5 stairs.