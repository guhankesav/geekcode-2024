class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        # Solution 2
        # using HashMap

        # abba

        hashMap = {}
        left = 0
        res = 0
        for index, val in enumerate(s):
            if val in hashMap:
                newLeft = hashMap[val] + 1
                while left < newLeft:
                    hashMap.pop(s[left])
                    left+=1


            hashMap[val] = index
            res = max(res, index + 1 - left)
        
        return res