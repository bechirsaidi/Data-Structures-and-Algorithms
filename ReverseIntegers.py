def reverse(x: int) -> int:
    # Define the 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Determine if x is negative
    sign = -1 if x < 0 else 1
    x *= sign
    
    # Reverse the integer
    reversed_x = 0
    while x != 0:
        digit = x % 10
        reversed_x = reversed_x * 10 + digit
        x //= 10
        
        # Check for overflow
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
    
    return sign * reversed_x
# Time Complexity: O(log(x)), where x is the input integer.
# This is because the number of digits in x is proportional to log10(x).

# Space Complexity: O(1), as we're using only a few additional variables.
