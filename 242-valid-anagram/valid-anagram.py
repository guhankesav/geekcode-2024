class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

#####################################################################

        #Solution 1
        count = [0] * 26
        
        # Count the frequency of characters in string s
        for x in s:
            count[ord(x) - ord('a')] += 1
        
        # Decrement the frequency of characters in string t
        for x in t:
            count[ord(x) - ord('a')] -= 1
        
        # Check if any character has non-zero frequency
        for val in count:
            if val != 0:
                return False
        
        return True

#####################################################################

        #Solution 2
        counterS, counterT = {}, {}

        for char in s:
            counterS[char] = counterS.get(char, 0) + 1
        
        for char in t:
            counterT[char] = counterT.get(char, 0) + 1

        if len(counterS) != len(counterT):
            return False

        for char in counterT:
            if counterT.get(char, -1) != counterS.get(char, -1):
                return False
        
        return True

#####################################################################

        # Solution 3
        if len(s) != len(t):
            return False

        counterS, counterT = {}, {}

        for i in range(len(s)):
            counterS[s[i]] = 1 + counterS.get(s[i], 0)
            counterT[t[i]] = 1 + counterT.get(t[i], 0)
        for i in counterS:
            if counterS[i] != counterT.get(i,0):
                return False
        return True

#####################################################################

        # Solution 4
        return Counter(s) == Counter(t)


#####################################################################

        #Solution 5
        return sorted(s) == sorted(t)