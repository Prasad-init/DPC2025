from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first_str = strs[0]
        for i, char in enumerate(first_str):
            for other_str in strs[1:]:
                if i >= len(other_str) or other_str[i] != char:
                    return first_str[:i]

        return first_str

solver = Solution()

strs1 = ["flower", "flow", "flight"]
print(f"Input: {strs1}")
print(f"Longest Common Prefix: '{solver.longestCommonPrefix(strs1)}'")
# Expected Output: Longest Common Prefix: 'fl'


  
