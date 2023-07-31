class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        check="([{"
        
        for e in s:
            if e in check:
                stack.append(e)
            elif  e == ")" and stack and stack[-1] =="(" :
                stack.pop()
            elif  e == "]" and stack and stack[-1] =="[" :
                stack.pop()
            elif  e == "}" and stack and stack[-1] =="{" :
                stack.pop()
            else : return False
            
            
        return len(stack) == 0


#O(n)