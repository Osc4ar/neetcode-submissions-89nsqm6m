'''
[1, 2, 3]

[1]
[1,2] [1,3]
[1,2,3][1,3,2]

1. Iterate the nums
2. For each num append the num to the current arr
3. Call the recursive function with the remaining values in nums
4. Once we are done with the recursive call, remove the value
5. If we do not have remaining nums, add the current array to the results list

Duplicates? It seems we will not have duplicates since we
are going over every value once and we remove it afterwards.
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        self.recursive([], nums, results)

        return results

    def recursive(self, current: List[int], nums: List[int], results: List[List[int]]):
        if len(nums) == 0:
            results.append(current[:])
            return

        for index, val in enumerate(nums):
            current.append(val)
            nums_without_value = nums[:index] + nums[index+1:]
            self.recursive(current, nums_without_value, results)
            current.remove(val)
