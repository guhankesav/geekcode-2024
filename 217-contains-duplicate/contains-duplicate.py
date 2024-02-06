class Solution:
    def containsDuplicate(self, nums: [List]) -> bool:

# Solution 1
        hashSet = set()
        for i in nums:
            if i in hashSet:
                return True
            hashSet.add(i)
        return False
        
# Solution 2
        nums.sort()
        i = 0
        while i < len(nums):
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                return True
            i += 1

        return False

# Solution 3
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        
        return False



