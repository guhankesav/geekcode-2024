class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        """
        Solution 1

        using count in an array
        Tiem complexity
        Space complecity
        """
        countMap = {}

        for val in nums:
            countMap[val] = countMap.get(val, 0) + 1
        
        countArr = [[] for i in range(len(nums) + 1)]
        
        for key, count in countMap.items():
            countArr[count].append(key)

        result = []
        for i in range(len(countArr)-1, 0, -1):
            for val in countArr[i]:
                result.append(val)
                if len(result) == k:
                    return result




        #Solution 2
        result = []
        countMap = {}
        for value in nums:
            countMap[value] = countMap.get(value, 0) + 1
        
        # print(sorted(countMap.items(), key=lambda kv:(kv[1], kv[0])))
        for i, j in (sorted(countMap.items(), key=lambda kv:(kv[1], kv[0]), reverse = True)):
            # print(i, j)
            if k == 0:
                return result
            k -= 1
            result.append(i)
        
        return result



