class Solution(object):
    def isValid(self, s):
        stack=[] 
        for i in range(len(s)): 
            if s[i]=='(' or s[i]=='{' or s[i]=='[': 
                stack.append(s[i]) 
            elif s[i]==')': 
                if stack and stack[-1]=='(': 
                    stack.pop()
                else:
                    return False 
            elif s[i]=='}': 
                if stack and stack[-1]=='{': 
                    stack.pop()
                else:
                    return False  
            elif s[i]==']': 
                if stack and stack[-1]=='[': 
                    stack.pop()
                else:
                    return False  
        if stack: 
            return False 
        else: 
            return True