def is_valid_parentheses(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

input_string = "[{()}]"
output = is_valid_parentheses(input_string)
print(f"Input: s = \"{input_string}\"")
print(f"Output: {str(output).lower()}")
