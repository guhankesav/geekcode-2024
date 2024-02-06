class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Solution 1
        hashSet = set(nums)
        maxLength = 0
        for i in nums:
            if i - 1 not in hashSet:
                length = 0 
                while i + length in hashSet:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength




        # Solution 2
        if not nums:
            return 0

        nums.sort()


        res = 1
        temp = 1
        for index in range(len(nums)):
            if index + 1 < len(nums) and nums[index + 1] == nums[index] + 1:
                temp += 1
                res = max(temp, res)
            elif index + 1 < len(nums) and nums[index + 1] == nums[index]:
                continue
            else:
                temp = 1
        return res
        