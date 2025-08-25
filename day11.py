from collections import Counter

def string_permutations(s: str) -> list[str]:
    char_counts = Counter(s)
    results = []
    n = len(s)

    def backtrack(current_permutation):
        if len(current_permutation) == n:
            results.append("".join(current_permutation))
            return

        for char in sorted(char_counts.keys()):
            if char_counts[char] > 0:
                current_permutation.append(char)
                char_counts[char] -= 1
                
                backtrack(current_permutation)
                
                char_counts[char] += 1
                current_permutation.pop()

    backtrack([])
    return results

input_str = "abc"
output = string_permutations(input_str)
print(f"Input: \"{input_str}\"")
print(f"Output: {output}")

input_str_dup = "aab"
output_dup = string_permutations(input_str_dup)
print(f"\nInput: \"{input_str_dup}\"")
print(f"Output: {output_dup}")
