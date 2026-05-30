class Solution:
    '''
    We can use the property of the array being sorted to find the target using two pointers.

    One pointer in the left and another one in the right, because the array is sorted we now the
    smallest item is the leftmost one and the greatest one is the rightmost one.

    1. Start iterating with left = 0 and right = len(numbers) - 1
    2. Calculate the current sum
    3. If the current sum is smaller than the target, increase it by moving left to the right
    4. If the current sum is greater than the target, decrease it by moving right one position to the left
    5. Repeate until the target is found, by definition it should happen before left == right
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [left+1, right+1] # Adding one to make them 1-indexed
        
        # Impossible to reach if preconditions are true
        return [-1, -1]