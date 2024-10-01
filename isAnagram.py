def isAnagram(s:str,t:str) ->bool:
    return sorted(s) == sorted(t)


# Time Complexity: O(n log n) due to the sorting step.
# Space Complexity: O(n) for storing the sorted strings.

def isAnagram(s: str, t: str) -> bool:
    # If lengths differ, they cannot be anagrams
    if len(s) != len(t):
        return False

    # Create a frequency array for 26 letters
    count = [0] * 26

    # Increment for s and decrement for t
    for char in s:
        count[ord(char) - ord('a')] += 1

    for char in t:
        count[ord(char) - ord('a')] -= 1

    # Check if all counts are zero
    for c in count:
        if c != 0:
            return False

    return True

# Time Complexity: O(n), where n is the length of the strings.
# This is because we iterate over both strings once.

# Space Complexity: O(1), as we only use a fixed-size array (size 26) regardless of the input size.
