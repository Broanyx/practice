def is_armstrong(n):
    """
    An Armstrong number is an n-digit number that equals the sum of each digit raised to the power n.
    """
    if n < 0:
        return False  
    
    digits = [int(d) for d in str(n)]  
    num_digits = len(digits)           
    total = sum(d ** num_digits for d in digits)  
    
    return total == n 

# Test Cases
print(is_armstrong(153))   # True (1^3 + 5^3 + 3^3 = 153)
print(is_armstrong(370))   # True (3^3 + 7^3 + 0^3 = 370)
print(is_armstrong(123))   # False (1^3 + 2^3 + 3^3 = 36 ≠ 123)
print(is_armstrong(9474))  # True (9^4 + 4^4 + 7^4 + 4^4 = 9474)
print(is_armstrong(0))     # True (0^1 = 0)