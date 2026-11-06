class Solution:
    '''
    Pythonic solution using list addition: nums + nums
    '''
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(2):
            for n in nums:
                result.append(n)

        return result
