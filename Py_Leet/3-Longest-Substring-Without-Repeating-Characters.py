class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hashset = set()
        l = 0
        for r in range (len(s)):
            if s[r] not in hashset :
                hashset.add(s[r])
                res = max(res , len(hashset))
            else :
                while s[l] != s[r]:
                    hashset.remove(s[l])
                    l += 1
                l += 1  
        return res
        
        """ res = 0
        hashset = set()
        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            res = max(res, len(hashset))
        return res"""
        #O(n) Time
    
        #O(n) Space