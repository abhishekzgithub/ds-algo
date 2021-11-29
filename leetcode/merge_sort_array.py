class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=j=k=0;
        temp=nums1[:]
        temp=temp[:n]
        while i<len(temp) and j<len(nums2):
            print(i,j, nums1,nums2)
            if temp[i]<nums2[j]:
                nums1[k]=temp[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        while i<len(temp):
            print(i,j, nums1,nums2)
            nums1[k]=temp[i]
            i+=1
            k+=1
        while j<len(nums2):
            print(i,j, nums1,nums2)
            nums1[k]=nums2[j]
            j+=1
            k+=1
        return nums1
        
    def merge1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i=j=k=0;
        temp=nums1[:]
        while i<len(temp) and j<len(nums2):
            print(i,j, nums1)
            if temp[i]<nums2[j]:
                if temp[i]==0:
                    nums1[k]=nums2[j]
                    j+=1
                else:
                    nums1[k]=temp[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            k+=1
        return nums1

    def merge_1(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1=self.merge_sort(nums1[:m]+nums2)
        return nums1

    def merge_sort(self, num_array):
        if len(num_array)>1:
            mid=len(num_array)//2
            L=num_array[:mid]
            R=num_array[mid:]
            self.merge_sort(L)
            self.merge_sort(R)
            i=j=k=0
            while i< len(L) and j<len(R):
                if L[i]<R[j]:
                    num_array[k]=L[i]
                    i+=1
                else:
                    num_array[k]=R[j]
                    j+=1
                k+=1
            while i<len(L):
                num_array[k]=L[i]
                i+=1
                k+=1
            while j<len(R):
                num_array[k]=R[j]
                j+=1
                k+=1
        return num_array

    def merge_v2(self,n1,m,n2,n):
        end=len(n1)-1
        m=m-1
        n=n-1
        while (m>=0 and n>=0):
            if n1[m]>n2[n]:
                n1[end]=n1[m]
                m-=1
            else:
                n1[end]=n2[n]
                n-=1    
            end-=1
        return n1
nums1=[1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

# nums1=[2,0]
# m=1
# nums2=[1]
# n=1

# nums1=[-1,0,0,3,3,3,0,0,0]
# m=6
# nums2=[1,2,2]
# n=3
# expected=[-1,0,0,1,2,2,3,3,3]

#nums1=[-50,-48,-47,-47,-46,-44,-43,-43,-41,-39,-38,-37,-37,-37,-33,-33,-32,-31,-29,-29,-27,-26,-26,-26,-25,-25,-24,
#-24,-23,-22,-22,-22,-18,-17,-17,-14,-14,-11,-11,-11,-6,-5,-5,-5,-5,-4,-1,0,2,2,2,2,5,6,7,7,9,10,13,13,14,14,18,21,
#21,21,22,24,24,24,25,26,26,29,29,29,30,30,31,31,32,33,34,34,34,35,38,40,41,42,43,44,44,46,46,47,47,48,49,49]
#m=100
#nums2=[]
#n=0
print(Solution().merge_v2(nums1, m, nums2, n))