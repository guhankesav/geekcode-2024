class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Solution 1
        Using defaultdict
        Time complexity - O(n * klog(k)), where n is number of strings and k is number of characters in each string
        Space Complexity - O(n)
        """
        
        anagramMap = defaultdict(list) 

        for string in strs:
            charactercount = [0] * 26
            for character in string:
                charactercount[ord(character) - ord('a')] += 1
            anagramMap[tuple(charactercount)].append(string)

        return anagramMap.values()

        """
        Solution 2
        Using defaultdict
        Time complexity - O(n * klog(k)), where n is number of strings and k is number of characters in each string
        Space Complexity - O(n)
        """
        
        anagramMap = defaultdict(list) 

        for string in strs:
            sortedString = sorted(string)
            anagramMap[tuple(sortedString)].append(string)

        return anagramMap.values()