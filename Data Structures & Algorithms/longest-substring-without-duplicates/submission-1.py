class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        left=0
        seen=set()
        for i in range(len(s)):
            while s[i]  in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            maxi=max(maxi,i-left+1)
        return maxi        
