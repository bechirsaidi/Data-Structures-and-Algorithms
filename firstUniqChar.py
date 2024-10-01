def firstUniqChar(s: str) -> int:
    # First pass: Count the occurrences of each character
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Second pass: Find the first unique character
    for index, char in enumerate(s):
        if char_count[char] == 1:
            return index
    
    return -1

# Time Complexity: O(n), where n is the length of the string.
# We iterate over the string twice (once for building the frequency map and once for finding the first unique character).

# Space Complexity: O(1) in terms of auxiliary space, as the character count dictionary will have at most 26 entries (for lowercase English letters).


def test_firstUniqChar():
    # Test case 1: Single unique character at the start
    assert firstUniqChar("leetcode") == 0, "Test case 1 failed"
    
    # Test case 2: Unique character in the middle
    assert firstUniqChar("loveleetcode") == 2, "Test case 2 failed"
    
    # Test case 3: No unique character
    assert firstUniqChar("aabb") == -1, "Test case 3 failed"
    
    # Test case 4: Single character string
    assert firstUniqChar("z") == 0, "Test case 4 failed"
    
    # Test case 5: Empty string
    assert firstUniqChar("") == -1, "Test case 5 failed"
    
    # Test case 6: All characters unique
    assert firstUniqChar("abcdef") == 0, "Test case 6 failed"
    
    print("All test cases passed!")

# Run the tests
test_firstUniqChar()
