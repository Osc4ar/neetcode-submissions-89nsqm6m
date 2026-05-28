class Solution:
    '''
    Approach with division:
    1. Calculate the product of all the elements
    2. For every position i, divide the total product by current nums[i]
    3. Save it in the array

    This has the limitation of failing with scenarios with a 0 number.

    We can use a similar approach as prefix sums and postfix sums.
    In this case, we would do a prefix product and postfix product
    of the array.

    1. To build a prefix product, we will create an array which contains
    the total product of the current element multiplied by all the previous ones.
    2. The postfix product array would be the same but it would be built from right to left.
    3. We iterate the array to build the result, to get the product of
    the given position, we multiply prefix[i-1] * postfix[i+1] so we can get the
    product of all the elements (pre-computed) without considering the current element.
    
    The time complexity of this solution is O(n) and it has a space complexity of O(n)
    This solution does not need division and does not fail with 0s.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current = 1
        prefix = []
        for n in nums:
            current *= n
            prefix.append(current)

        current = 1
        postfix = []
        for n in reversed(nums):
            current *= n
            postfix.append(current)
        postfix = postfix[::-1]

        result = []
        for i in range(len(nums)):
            current = 1

            if i - 1 >= 0:
                current *= prefix[i - 1]
            if i + 1 < len(nums):
                current *= postfix[i + 1]

            result.append(current)

        return result