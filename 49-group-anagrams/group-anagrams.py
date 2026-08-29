from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-97]+=1
            key = tuple(count)
            dict[key].append(s)
        return list(dict.values())