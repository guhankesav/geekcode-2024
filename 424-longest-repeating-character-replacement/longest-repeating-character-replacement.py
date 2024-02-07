class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        l = 0
        maxx = 0
        charMap = {}

        for r in range(len(s)):

            charMap[s[r]] = charMap.get(s[r], 0) + 1

            while ( r - l + 1 ) - max(charMap.values()) > k:
                charMap[s[l]] -= 1
                l += 1


            maxx = max(maxx, r - l + 1)
        return maxx           
        