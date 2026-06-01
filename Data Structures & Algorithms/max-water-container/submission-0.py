class Solution:
    '''
    The container could be seen as a rectangle which area is equal to be the product of width and
    height. Where the height of the container is the smallest "bar".

    We could try to first maximize the width of the rectangle by starting with a container
    with a width of the whole array.

    We calculate its area and save it, then we have to choose if we reduce by the left or the right,
    we have to choose the smallest bar and move it one position to the center.

    We repeat that process until the left and right bars are the same.
    '''
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height
            result = max(result, current_area)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return result