class Solution:
    '''
                        *
    [30,38,30,36,35,40,28]
    [ 1, 4, 1, 2, 1, 0, 0]

    [(40, 5)]

    0. Initialize a result array with zeroes
    1. If we have element in the stack, we check the top
        otherwise we just add the value and its index
    2. If the top is smaller than the current number
        we pop it, once popped we update the result array in
        the popped index by doing current_index - stack_index
        Repeat this until the stack is empty or the top is bigger
        than the current number.
    3. If the top is bigger, add the current number and index to
        the stack.
    4. After iterating the input, the result array will have the correct
        values. All the values in the stack did not have a warmer day
        after.
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # monotonic stack, always decreases

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, old_index = stack.pop()
                result[old_index] = i - old_index
            
            stack.append((t, i))

        return result