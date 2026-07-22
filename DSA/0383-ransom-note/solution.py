class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        have={}
        for ch in magazine:
            have[ch]=have.get(ch,0)+1
        need={}
        for ch in ransomNote:
            need[ch]=need.get(ch,0)+1
        flag=False
        for ch in need:
            if have.get(ch,0)<need.get(ch,0):
                return False
        return True
        