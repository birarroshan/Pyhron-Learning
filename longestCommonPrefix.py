from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for k in range(len(strs[0])):
            #ix+=1
            pre = strs[0][:k+1]
            ch = strs[0][k]
            for i in range(1,len(strs)):
                if k >= len(strs[i]) or strs[i][k]!=ch:
                    return strs[0][:k]
        return pre