class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            timeToReach = (target-p) / s
            stack.append(timeToReach)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


# stack[-1] <= stack[-2] this check at line 10 is important
# it tells that whether the next(reverse order) takes less or equal time
# less time means the car is faster than the next car and they become a fleet
# equal means they gonna meet at the target position 
