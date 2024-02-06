class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        Solution 1
        Using hashMap
        TimeComplexity - O(n)
        spaceComplexity - O(n)
        """
        countMap = {}

        for index, value in enumerate(nums):

            if (target - value) in countMap:
                return [index, countMap[target - value]]

            countMap[value] = index
            



        """
        Solution 2
        Brute Force  
        Time Complexity  - O(n^2)
        Space Complecity - O(1)
        """

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]