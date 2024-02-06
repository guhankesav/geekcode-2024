class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Solution 1
        - 2 pointer approach
        - Time complexity - O(n)
        - Space complexity - O(1)
        """
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(area, maxArea)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
            

        """
        Solution 2 
        - Brute Force 
        - Time complexity - O(n^2)
        - Space complexity - O(1)
        """
        maxArea = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                maxArea = max(area, maxArea)
        
        return maxArea
        