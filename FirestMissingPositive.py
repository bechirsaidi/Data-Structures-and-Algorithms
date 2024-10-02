def firstMissingPositive(nums):
    n = len(nums)
    
    # Step 1: Place each number in its correct position if possible
    for i in range(n):
        # Only place numbers in their correct position if they are in the range [1, n]
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Swap the current number to its correct position
            correct_idx = nums[i] - 1
            nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
    
    # Step 2: Find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1  # The first missing positive integer
    
    # If all numbers from 1 to n are present, return n + 1
    return n + 1
# Time Complexity: O(n), because each element is swapped at most once.

# Space Complexity: O(1), since we are modifying the input array in place and not using any extra space.
