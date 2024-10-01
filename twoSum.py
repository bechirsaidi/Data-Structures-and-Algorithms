def twoSum(nums,target):
    left ,right= 0 , len(nums) -1

    while left<right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left+1, right+1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Time Complexity: O(n), where n is the number of elements in the input array.
# We traverse the array at most once with the two pointers.

# Space Complexity: O(1), as we are using a constant amount of extra space for pointers.
