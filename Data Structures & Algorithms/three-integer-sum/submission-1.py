class Solution:
    '''
    To optimize the solution in memory complexity, we can use a sorted array.
    Because sorting is O(n*logn) it will not impact our target time complexity of O(n^2).
    Once the array is sorted, we can do the following:

    1. Iterate every element of the array.
    2. For every element, calculate which value is needed to add to it to get 0
    3. With the new target value, use the two pointers approach in the rest of the array,
        to find two numbers which sum the target.
    4. Store the result if there is any result.
    5. Move the pointer to the next position, if there are any duplicate, skip it to avoid
        duplicate results.
    6. Return the list of arrays with the triplets
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        i = 0
        nums = sorted(nums)

        while i < len(nums):
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[left] + nums[right]
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left-1] == nums[left]: # To avoid duplicates
                        left += 1
            
            i += 1
            while i < len(nums) and nums[i-1] == nums[i]: # To avoid duplicates
                i += 1

        return result