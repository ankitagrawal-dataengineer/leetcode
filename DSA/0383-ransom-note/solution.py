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

        for ch in ransomNote:
            if have.get(ch, 0) == 0:
                return False
            have[ch] -= 1
        return True