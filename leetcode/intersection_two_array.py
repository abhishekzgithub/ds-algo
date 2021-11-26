"""
Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]


"""

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        big_array,short_array =(nums1,nums2) if len(nums1)>len(nums2) else (nums2,nums1)
        print(big_array,short_array)
        window=len(short_array)
        for i in range(len(big_array)-window):
            if big_array[i:i+window]==short_array:
                print(i,i+window-1)
    def intersect(self, nums1, nums2):
        hash_table={}
        result=[]
        big_array,short_array =(nums1,nums2) if len(nums1)>len(nums2) else (nums2,nums1)
        for idx, ele in enumerate(big_array):
            if ele not in hash_table:
                hash_table[ele]=[idx]
            else:
                hash_table[ele].append(idx)
        for elej in short_array:
            if elej in hash_table:
                if len(hash_table[elej])==1:
                    result.append(elej)
                    del hash_table[elej]
                else:
                    if len(hash_table[elej])>1:
                        result.append(elej)
                        hash_table[elej].pop(0)
        return result
            
nums1=[1,2,1,2,2,1]
nums2=[2,2]

#nums1 = [4,9,5]
#nums2 = [9,4,9,8,4]

#nums1=[3,1,2]
#nums2=[1,1]

obj=Solution()

print(obj.intersect(nums1, nums2))