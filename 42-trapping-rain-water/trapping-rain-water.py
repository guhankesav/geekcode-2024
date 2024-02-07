class Solution:
    def trap(self, height: List[int]) -> int:
        

        # Solution 2
        left = []
        right = []
        
        h = 0
        for i in range(len(height)):
            left.append(h)
            h = max(height[i], h)

        h = 0
        for i in range(len(height)-1, -1 , -1):
            right.append(h)
            h = max(height[i], h)
        right  = right[::-1]


        trappedWater = 0
        for i in range(len(height)):
            if (min(left[i], right[i]) - height[i]) > 0:
                trappedWater += min(left[i], right[i]) - height[i]
        
        return trappedWater

        