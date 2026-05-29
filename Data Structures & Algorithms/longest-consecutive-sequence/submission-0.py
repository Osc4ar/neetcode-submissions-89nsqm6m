class Solution:
    '''
    We cannot sort the array because sorting is O(n*logn)

    We may use a Set to remove all the duplicates and quickly lookup for values.
    To quickly identify the beginning of the sequence, I can check if
    the current number has a predecessor in the Set. If it does not have
    a predecessor we count it as the beginning of the sequence.

    For numbers which are the start of the sequence, we check for the next
    values until we lose the sequence. We have to do this check for 
    every number in the array. If we lose the sequence, we save the longest
    sequence so far.
    '''
    def longestConsecutive(self, nums: List[int]) -> int:
        lookup = set(nums)

        max_sequence = 0
        for n in nums:
            if n - 1 in lookup:
                continue

            # We start counting the sequence
            current_sequence = 1
            current_n = n + 1
            while current_n in lookup:
                current_sequence += 1
                current_n += 1
            max_sequence = max(current_sequence, max_sequence)

        return max_sequence