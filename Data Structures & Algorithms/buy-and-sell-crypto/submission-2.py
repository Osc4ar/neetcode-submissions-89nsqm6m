class Solution:
    '''
    We may use two pointers to have a window of days

    If the left pointer is bigger than right, there is no profit. Move left one position
    If the left pointer is less or equal than right, there is profit. Move right one position

    Calculate the profit, start with zero and update it with profit = max(profit, current)

    * Pointers have to start in 0 and 1 positions
    '''
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        left = 0

        for right in range(1, len(prices)):
            profit = prices[right] - prices[left]
            result = max(result, profit)

            if profit < 0:
                # Move the left pointer to the smaller value
                left = right

        return result