class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i,j=0,0
        n,m=len(firstList),len(secondList)
        res=[]
        while i<n and j<m:
            start1=firstList[i][0]
            end1=firstList[i][1]
            start2=secondList[j][0]
            end2=secondList[j][1]

            if start1<=start2:
                if end1>=start2:
                    start=max(start1,start2)
                    end=min(end1,end2)
                    res.append([start,end])
            else:
                if end2>=start1:
                    start=max(start1,start2)
                    end=min(end1,end2)
                    res.append([start,end])
            if end1<=end2:
                i+=1
            else:
                j+=1
        return res