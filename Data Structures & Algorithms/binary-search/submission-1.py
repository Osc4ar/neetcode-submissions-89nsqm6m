class Solution:
    '''
    Standard Binary Search, main considerations:
    Left can be equal to Right, it's ok to have single digit windows
    We move the pointers to middle + 1 or middle - 1, we don't
    need to include middle in the window because we already know
    it's not the result if we are still looking.
    '''
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target: # Look in the right
                left = middle + 1
            else: # look in the left
                right = middle - 1
        
        return -1