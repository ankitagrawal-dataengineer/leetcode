class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            elif stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)