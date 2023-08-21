class Solution:
    def isPalindrome(self, s: str) -> bool:
         """ check = ""
        for e in s:
            if e.isalnum():
                check += e.lower()
        return check==check[::-1]
        #Extra memory O(n)
        #O(n)
        
        """
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not self.isalnm(s[l]):
                l+=1
            while l<r and not self.isalnm(s[r]):
                r-=1
            if s[r].lower() != s[l].lower():
                return False
            
            r-=1
            l+=1
        return True

    def isalnm(self,c):
        return (ord('A')<=ord(c) <=ord('Z') or
            ord('a')<= ord(c)<=ord('z') or
            ord('0')<= ord(c)<=ord('9'))
    #O(n) Time
    #O(1) memory
            