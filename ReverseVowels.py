def reverseVowels(s: str) -> str:
    # Time Complexity: O(n), where n is the length of the string
    # Space Complexity: O(n), due to storing the list s_list
    
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s) - 1
    
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
            
    return ''.join(s_list)

# Test cases
def test_reverseVowels():
    # Test case 1: Basic test with some vowels
    assert reverseVowels("hello") == "holle", "Test case 1 failed"

    # Test case 2: All vowels, should be reversed completely
    assert reverseVowels("leetcode") == "leotcede", "Test case 2 failed"
    
    # Test case 3: No vowels, should return the original string
    assert reverseVowels("bcdfg") == "bcdfg", "Test case 3 failed"
    
    # Test case 4: Single character (vowel)
    assert reverseVowels("a") == "a", "Test case 4 failed"
    
    # Test case 5: Single character (consonant)
    assert reverseVowels("z") == "z", "Test case 5 failed"
    
    # Test case 6: Multiple identical vowels
    assert reverseVowels("aAaAa") == "aAaAa", "Test case 6 failed"
    
    # Test case 7: Uppercase and lowercase mix
    assert reverseVowels("hEllo") == "hollE", "Test case 7 failed"
    
    # Test case 8: Empty string
    assert reverseVowels("") == "", "Test case 8 failed"
    
    # Test case 9: Long string with vowels at the start and end
    assert reverseVowels("abcdefghi") == "ibcdefgha", "Test case 9 failed"
    print("All test cases passed!")

# Run the tests
test_reverseVowels()
