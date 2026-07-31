class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for num in asteroids:
            is_alive = True
            while is_alive and stack and stack[-1] > 0 and num < 0:
                if stack[-1] == abs(num):
                    stack.pop()
                    is_alive = False
                elif stack[-1] < abs(num):
                    stack.pop()
                elif stack[-1] > abs(num):
                    is_alive = False
            if is_alive == True:
                stack.append(num)

        return stack
