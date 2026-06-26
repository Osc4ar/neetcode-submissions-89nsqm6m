class Solution:
    '''
    We can use a sliding window and a sliding window and
    a set to quickly check if we have a substring with
    unique characters.

    1. We start with two pointers left and right in position zero
    2. We add the first character to the set.
    3. We move the right pointer one position.
    4. We check if we the new character is in the set
      a. If it is not in the set, add it and keep moving right (save the max size of the set)
      b. If the character is in the set, move left and remove its character in the set until
         the set does not have duplicates or it is empty.
    5. Keep repeating this until right iterates the whole array.
    6. Our result is the longest set size
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        maxSize = 1
        left = 0
        unique_chars = {s[0]}
        for right in range(1, len(s)):
            while s[right] in unique_chars:
                unique_chars.remove(s[left])
                left += 1
            unique_chars.add(s[right])
            maxSize = max(maxSize, len(unique_chars))

        return maxSize
        