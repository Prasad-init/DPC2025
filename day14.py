def count_substrings_with_exactly_k_distinct_chars(s: str, k: int) -> int:
    return count_at_most_k(s, k) - count_at_most_k(s, k - 1)

def count_at_most_k(s: str, k: int) -> int:
    if k < 0:
        return 0
    
    n = len(s)
    left = 0
    result = 0
    freq = {}
    
    for right in range(n):
        char_right = s[right]
        freq[char_right] = freq.get(char_right, 0) + 1
        
        while len(freq) > k:
            char_left = s[left]
            freq[char_left] -= 1
            if freq[char_left] == 0:
                del freq[char_left]
            left += 1
            
        result += (right - left + 1)
        
    return result

s = "pqpqs"
k = 2
print(f"The number of substrings in '{s}' with exactly {k} distinct characters is: {count_substrings_with_exactly_k_distinct_chars(s, k)}")
