arr = [6, 8, 0, 1, 3]
n = len(arr)
nge = [-1] * n  # Initialize the result array with -1
stack = []

# Iterate over each element in the array
for i in range(n):
    # While stack is not empty and the current element is greater than the element at the top of the stack
    while stack and arr[stack[-1]] < arr[i]:
        index = stack.pop()
        nge[index] = arr[i]
    # Push the current index onto the stack
    stack.append(i)

print("Array:", arr)
print("Next Greater Elements:", nge)
