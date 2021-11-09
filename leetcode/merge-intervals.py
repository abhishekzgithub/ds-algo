#https://leetcode.com/problems/merge-intervals/submissions/
"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

"""
import copy

class Solution:
    def merge(self, intervals):
        intervals=sorted(intervals)
        merged_list=[]

        if len(intervals)<2:
            return intervals
        l,h=0,len(intervals)
        while l<h:
            if merged_list==[]:
                merged_list.append(intervals[l][:])
                l+=1
                continue
            #l+=1
            print(l)
            print(merged_list)
            prev_start=merged_list[-1][0]#intervals[l][0]
            prev_end=merged_list[-1][1] #intervals[l][1]
            next_start=intervals[l][0]
            next_end=intervals[l][1]
            if prev_end-next_start>=0:
                if prev_end-next_end<=0:
                    merged_list[-1][1]=copy.deepcopy(next_end)
                    l+=1
                    continue
                else:
                    merged_list[-1][1]=copy.deepcopy(prev_end)
                    l+=1
                    continue
            merged_list.append(intervals[l])
            l+=1
        return merged_list

intervals = [[1,3],[2,6],[8,10],[15,18]]
#intervals=[[1,4],[4,5]]
#intervals=[[1,4],[5,6]]
intervals = [[1,2],[3,5],[4,6],[8,10],[15,18]]
intervals=[[1,4],[2,3]]

print(Solution().merge(intervals))