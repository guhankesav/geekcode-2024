class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda pair : pair[0])
        res = [intervals[0]]
        print(res[-1][0])
        print(res[-1][1])
        for interval in intervals[1:]:
            lastVal = res[-1]
            if lastVal[1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res

        