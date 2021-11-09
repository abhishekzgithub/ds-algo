#https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1, nums2):
        result=[]
        for ele in nums1:
            for ele1 in nums2:
                if ele ==ele1:
                    result.append(ele)
                break
        return result
if __name__=="__main__":
    nums1=""
    nums2=""
    nums1=[4,9,5]
    nums2=[9,4,9,8,4]
    expected=[4,9]
    #nums1 = [1,2,2,1]; nums2 = [2,2]
    #expected=[2,2]
    print(Solution().intersect(nums1, nums2))