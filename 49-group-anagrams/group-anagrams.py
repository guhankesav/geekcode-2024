class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Solution 1
        Using defaultdict
        """
        
        anagramMap = defaultdict(list) 

        for string in strs:
            sortedString = sorted(string)
            anagramMap[tuple(sortedString)].append(string)

        return anagramMap.values()

        