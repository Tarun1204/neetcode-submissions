class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        o = {}
        b = {}
        aa = 1
        for i, value in enumerate(s):
            if value in o:
                o[value] = o[value] +1
            else:
                o[value] = aa

        for i, value in enumerate(t):
            if value in b:
                b[value] = b[value] +1
            else:
                b[value] = aa

        return o == b
          
        