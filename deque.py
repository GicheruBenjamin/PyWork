from collections import deque

# Using deque as a stack
print("Using deque as a stack:")

# Creating a deque
stack = deque()

# Appending elements
stack.append(10)
stack.append(20)
stack.append(30)


# Popping elements
popped_value_1 = stack.pop()
popped_value_2 = stack.pop()
popped_value_3 = stack.pop()

print("Popped values:", popped_value_1, popped_value_2, popped_value_3)

# Using deque as a queue
print("\nUsing deque as a queue:")

# Creating a deque
queue = deque()

# Appending elements
queue.append(10)
queue.append(20)
queue.append(30)

 # Popping elements
queued_value_1 = queue.popleft()
queued_value_2 = queue.popleft()
queued_value_3 = queue.popleft()

print("Queued values:", queued_value_1, queued_value_2, queued_value_3)