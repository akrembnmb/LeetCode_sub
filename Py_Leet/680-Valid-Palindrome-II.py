class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1
        while l<r :
            if s[l] != s[r]:
                delL,delR = s[l+1:r+1] , s[l:r]
                return (delL == delL[::-1] 
                        or delR == delR[::-1])
            l+=1
            r-=1
            
        return True
        #O(n) 