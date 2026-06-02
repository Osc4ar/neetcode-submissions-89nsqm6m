class Solution:
    '''
    The amount of water a given cell can hold depends on the walls to the left or the right.
    If the current height is smaller than any wall in the left and right, it will trap water.

    Therefore the amount of water if the cell i could be calculated with water[i] = min(left[i], right[i]) - height[i]
    The left and right arrays refer to some precomputed arrays with the maximum height registered
    until that point, either starting from the left or from the right.

    With the pre-computed arrays which have a time and space complexities of O(n), we can solve
    the problem with a time complexity of O(n).

    1. Calculate the max_left and max_right arrays.
    2. Iterate the array again, this time use the formula to get the water
        water[i] = min(left[i], right[i]) - height[i]
    3. If the current height does not trap water, it will result in 0 in the previous formula
    4. Accumulate the result in a variable and return it
    '''
    def trap(self, height: List[int]) -> int:
        current_max = 0
        max_left = []
        for h in height:
            if h > current_max:
                current_max = h
            max_left.append(current_max)

        current_max = 0
        max_right = []
        for h in reversed(height):
            if h > current_max:
                current_max = h
            max_right.append(current_max)
        max_right = max_right[::-1] # We built it in reverse

        result = 0
        for i, h in enumerate(height):
            min_wall_height = min(max_left[i], max_right[i])
            result += min_wall_height - h

        return result