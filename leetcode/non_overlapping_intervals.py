"""
https://leetcode.com/problems/non-overlapping-intervals/
Given an array of intervals, intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals=sorted(intervals, key=lambda x:x[1])
        #print(intervals)
        compatible=set()
        ix=0
        prev=ix
        next=ix+1
        compatible.add((intervals[0][0],intervals[0][1]))
        while next<=len(intervals)-1:
            i=intervals[prev][0]
            j=intervals[prev][1]
            m=intervals[next][0]
            n=intervals[next][1]
            if j<=m:
                #compatible.add((i,j))
                compatible.add((m,n))
                prev=next
                next+=1
            else:
                next+=1

        return(abs(len(compatible) - len(intervals)))

intervals=[[1,2],[2,3],[3,4],[1,3]]
#intervals=[[1,2],[1,2],[1,2]]
#intervals=[[0,2],[1,3],[2,4],[3,5],[4,6]]
output=1
print(Solution().eraseOverlapIntervals(intervals))