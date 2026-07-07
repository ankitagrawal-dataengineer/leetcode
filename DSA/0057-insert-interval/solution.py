class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        arr = []
        inserted = False
        for interval in intervals:
            if not inserted and newInterval[0] < interval[0]:
                arr.append(newInterval)
                inserted = True
            arr.append(interval)
        if not inserted:
            arr.append(newInterval)
        res = []
        start1 = arr[0][0]
        end1 = arr[0][1]
        for i in range(1, len(arr)):
            start2 = arr[i][0]
            end2 = arr[i][1]
            if end1 >= start2:
                end1 = max(end1, end2)
            else:
                res.append([start1, end1])
                start1 = start2
                end1 = end2
        res.append([start1, end1])
        return res
        
