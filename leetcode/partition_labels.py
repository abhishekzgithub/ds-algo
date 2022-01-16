"""
https://leetcode.com/problems/partition-labels/

763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

"""

class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        The idea is to keep track of index and compare if the index has reached its max end. If yes, then
        switch/ propagate the index to next and then move on.
        """
        hash_max={}
        for ix, ele in enumerate(s):
            hash_max[ele]=ix
        print(hash_max)
        partition_index=[]
        j=i=0
        max_indexval=0
        while j<len(s):
            max_indexval=max(max_indexval, hash_max[s[j]])
            if j==max_indexval: #once j reach the max index value 's index, switch
                partition_index.append(j-i+1)
                print(s[i:j])
                i=j+1
            j+=1
        return partition_index
        

s="ababcbacadefegdehijhklij"
output=[9,7,8]
obj=Solution()
print(obj.partitionLabels(s))