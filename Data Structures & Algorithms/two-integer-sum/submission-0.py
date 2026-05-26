class Solution:
    '''
    We need a way to quickly lookup if a previous number plus the current number sum the target.

    We could do quick lookups with a Dictionary/HashMap. Building the the dictionary plus the lookups
    will have a time complexity of O(n) and a memory complexity of O(n) since we are iterating
    the array once and storing it again.

    1. For every number in the array, calculate its "complement": target - num
    2. Store the complement in the dictionary, the value its the index.
    3. Whenever the dictionary is not empty, check if the current value exists in the dictionary
    4. If the value exists as a key in the dictionary, it means that it's a complement
    5. Return the index in the dictionary with the current index
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for i, n in enumerate(nums):
            if n in complements:
                return [complements[n], i]

            complement = target - n
            complements[complement] = i

        return [] # We should never reach here given the assumption
