class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return sorted(s) == sorted(t)



        # if len(s) != len(t):
        #     return False

        # counterS, counterT = {}, {}

        # for i in range(len(s)):
        #     counterS[s[i]] = 1 + counterS.get(s[i], 0)
        #     counterT[t[i]] = 1 + counterT.get(t[i], 0)
        # for i in counterS:
        #     if counterS[i] != counterT.get(i,0):
        #         return False
        # return True
        