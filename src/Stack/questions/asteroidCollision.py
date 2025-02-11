from collections import deque

def asteroidCollision(asteroids):
    stack = deque()  # Initialize a deque to use as a stack
    
    for asteroid in asteroids:
        # If the asteroid is moving to the right or the stack is empty, push it onto the stack
        if asteroid > 0 or not stack:
            stack.append(asteroid)
        else:
            # Handle collisions with asteroids moving to the left
            while stack and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    # The top of the stack asteroid is smaller and gets destroyed
                    stack.pop()
                    continue
                elif stack[-1] == abs(asteroid):
                    # Both asteroids are equal and destroy each other
                    stack.pop()
                break
            else:
                # If no collision occurs, push the current asteroid onto the stack
                stack.append(asteroid)
                       
    return list(stack)  # Convert the deque back to a list and return it

# Test cases
print(asteroidCollision([10, 5, -15]))  # Output: [-15]
print(asteroidCollision([5, 10, -5]))   # Output: [5, 10]
print(asteroidCollision([8, -8]))       # Output: []
print(asteroidCollision([10, 2, -5]))   # Output: [10]
print(asteroidCollision([-2, -1, 1, 2]))# Output: [-2, -1, 1, 2]
print(asteroidCollision([-2, -2, 1, -2]))# Output: [-2, -2, -2]