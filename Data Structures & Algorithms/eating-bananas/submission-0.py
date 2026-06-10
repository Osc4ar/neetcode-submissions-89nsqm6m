class Solution:
    '''
    We need a way to know if a given speed k is fast enough.

    To quickly know which speed is the minimum we can use binary search, the search
    space is not the array directly. The max value in the array (biggest pile) is the
    max k we have to use. For the min value we may use 1 or Sum of Math.ceil(bananas / h).

    1. Define the left and right pointers (linear complexity)
    2. Calculate the middle point of the search space
    3. Check if the speed is fast enough.
        a. If it is, store the speed as the current minimum. Move right pointer to middle - 1
        b. If it is not, Move left pointer to middle + 1
    4. Return the current minimum when the loop ends, the loop ends when left > right

    To check if a given speed is fast enough, we can do a for loop checking how
    many hours we would take to finish all bananas. If the time is bigger than h,
    the speed is not enough

    To calculate the time we can do something like: Match.ceil(piles[i] / k) to know
    how many hours we would take in each pile. We accumulate the time of each pile.
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right = max(piles)
        left = math.ceil(sum(piles) / h)
        result = right

        while left <= right:
            middle = (right + left) // 2
            if self.isValidSpeed(piles, h, middle):
                result = min(result, middle)
                right = middle - 1
            else:
                left = middle + 1

        return result

    def isValidSpeed(self, piles: List[int], h: int, k: int) -> bool:
        current_time = 0

        for pile in piles:
            current_time += math.ceil(pile / k)

            if current_time > h:
                return False
        
        return True