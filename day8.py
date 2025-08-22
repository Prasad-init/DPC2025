def reverse_words(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

input_str1 = "the sky is blue"
print(f'Input: "{input_str1}"')
print(f'Output: "{reverse_words(input_str1)}"') # Expected: "blue is sky the"

input_str2 = "  hello world  "
print(f'\nInput: "{input_str2}"')
print(f'Output: "{reverse_words(input_str2)}"') # Expected: "world hello"

input_str3 = "a good   example"
print(f'\nInput: "{input_str3}"')
print(f'Output: "{reverse_words(input_str3)}"') # Expected: "example good a"
