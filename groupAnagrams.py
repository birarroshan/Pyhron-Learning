from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        ana = dict()
        for s in strs:
            key = [0] *26
            for ch in s:
                key[ ord(ch) - ord('a')] +=1
            k = tuple(key)
            ana[k] = ana.get(k,[])
            ana[k].append(s)
        return list(ana.values())
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))