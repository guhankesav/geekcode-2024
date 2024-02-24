class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxVal = nums[0] if nums else 0
        currSum = 0

        for i in nums:
            if currSum < 0:
                currSum = 0 
            currSum += i
            maxVal = max(currSum, maxVal)
        return maxVal 