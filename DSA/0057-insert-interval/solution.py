class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        inserted=False
        res=[]
        for interval in intervals:
            if not inserted and newInterval[0]<interval[0]:
                res.append(newInterval)
                inserted=True
            res.append(interval)
        if not inserted:
            res.append(newInterval)
        ans=[]
        start1=res[0][0]
        end1=res[0][1]
        for i in range(1,len(res)):
            start2=res[i][0]
            end2=res[i][1]
            if end1>=start2:
                end1=max(end1,end2)
            else:
                ans.append([start1,end1])
                start1=start2
                end1=end2
        ans.append([start1,end1])
        return ans