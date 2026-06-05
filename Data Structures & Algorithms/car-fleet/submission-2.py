class Solution:
    '''
    We may advance in time to identify fleets:

    [4,1,0,7] - [2,2,1,1]
    [6,3,1,8]
    [8,5,2,9]
    [10,7,3,10] -> Two same values, it becomes one fleet.
                -> The values also are the target, we remove the fleet
    [10,7,3]

    We could have a set with all the positions, update the positions
    using the car speeds and count how many final fleets reach the target
    (one per fleet)

    Space complexity - O(n) we store the car positions in a set
    Time Complexity - Building the set is O(n)
                      Each iteration would require to update the set
                      and we would do at most O(target*n)

    A better approach is to identify the time it would take each car
    to reach the target, the formula would be: (target - position) // speed

    With that formula, we could find the cars making fleets by sorting the
    cars by how close they are to the target (descending order).

    If any of the cars behind a given car takes less time to reach the target,
    that means those cars would join the fleet. Because the cars behind
    will catch it at some point. To capture this behavior we could use a
    stack:

    1. Order the cars in descending order.
    2. Initialize an empty stack (monotonic increasing)
    3. Calculate the time of the car to reach the target
    4. If the time is bigger, store it in the stack.
        Otherwise, skip it because it will join the top's fleet
        (the car would catch the one in front)
    5. Return the size of the stack as the answer.
    '''
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_and_speed = [(position[i], speed[i]) for i in range(len(position))]
        position_and_speed = sorted(position_and_speed)[::-1] # By default sorts in ascending order
        stack = [] # Monotonic stack (increasing)

        for current_p, current_s in position_and_speed:
            time = (target - current_p) / current_s

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)

