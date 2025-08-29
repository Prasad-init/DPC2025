def lengthOfLongestSubstring(s: str) -> int:
    char_index_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        char = s[right]
        
        if char in char_index_map and char_index_map[char] >= left:
            left = char_index_map[char] + 1
            
        char_index_map[char] = right
        
        current_length = right - left + 1
        max_length = max(max_length, current_length)
        
    return max_length

S = "abcabcbb"
print(f"Input: S = \"{S}\"")
print(f"Output: {lengthOfLongestSubstring(S)}")
