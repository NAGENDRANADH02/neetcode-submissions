class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        def solve(interval):
            interval.sort()
            res=[]
            for start,end in interval:
                if not res or start>res[-1][1]:
                    res.append([start,end])
                else:
                    res[-1][1]=max(res[-1][1],end)
            return res
        return solve(intervals)                

        