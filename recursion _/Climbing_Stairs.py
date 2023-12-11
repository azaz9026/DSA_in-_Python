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

