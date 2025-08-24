from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for s in strs:
        sorted_s = "".join(sorted(s))
        anagram_map[sorted_s].append(s)

    return list(anagram_map.values())

input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupAnagrams(input_strs)
print(output)
