
def largestRectangle(h):
    # Write your code here
    max_area = 0
    index = 0
    stack: list[int] = []
    
    while index < len(h):
        if not stack or h[index] >= h[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = h[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
            max_area = max(max_area, area)
    
    while stack:
        top_of_stack = stack.pop()
        area = h[top_of_stack] * ((index - stack[-1] - 1) if stack else index)
        max_area = max(max_area, area)
    
    return max_area
