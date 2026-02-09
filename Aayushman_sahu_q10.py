def second_largest(nums):
    """
    Return the second largest unique number in the list.
    If there's no second largest (all elements same or list too small), return None.
    """
    unique_nums = list(set(nums))  # Remove duplicates
    unique_nums.sort()             # Sort in ascending order
    
    if len(unique_nums) < 2:
        return None
    else:
        return unique_nums[-2]    # Return second last element

# Test Cases
print(second_largest([2, 5, 1, 4, 5]))  # 4
print(second_largest([7, 7, 7]))         # None
print(second_largest([10, 9, 8]))       # 9
print(second_largest([5]))               # None
print(second_largest([-3, -1, -2]))      # -2
print(second_largest([1, 2, 2, 3]))      # 2