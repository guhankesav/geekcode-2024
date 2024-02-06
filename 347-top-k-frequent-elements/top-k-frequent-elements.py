class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
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



