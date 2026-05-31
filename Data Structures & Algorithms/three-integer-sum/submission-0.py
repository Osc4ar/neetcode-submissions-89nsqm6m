class Solution:
    '''
    We may use a similar approach to Two-Sum to solve this problem.

    1. We iterate the array, for every element we calculate a target = 0 - num
    2. For the rest of the array, we use a solution like two sum with the target we
       calculated. If there are solutions, we save the triplet as a tuple in a set to avoid duplicates.
    3. The Two sum solution which we can use is using a HashMap/Dictionary to store the
       the complement of a given number: complement = target - num. To quickly check if two numbers
       sum the target.
    4. At the end, we iterate the set of tuples and convert them to a list of lists without duplicates

    The time complexity of this algorithm is O(n^2), because for every item we do the Two Sum algorithm O(n)
    The space complexity of this algorithm is O(n) because we store the array in a HashMap 
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_triplets = set()

        def twoSum(sub_array: List[int], current_num: int):
            target = 0 - current_num
            complements = {}

            for n in sub_array:
                if n in complements:
                    # Sorting triplet to avoid permutations in Set
                    sorted_triplet = sorted([current_num, complements[n], n])
                    unique_triplets.add(tuple(sorted_triplet))
                else:
                    complements[target - n] = n

        for i, n in enumerate(nums):
            if i + 1 < len(nums):
                twoSum(nums[i+1:], n)
        
        return [list(triplet) for triplet in unique_triplets]
