class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for i in range(len(s)):
            freq[s[i]]=freq.get(s[i],0)+1
        for i,ch in enumerate(s):
            if freq[ch]==1:
                return i
        return -1