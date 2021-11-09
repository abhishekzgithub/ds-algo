"""
https://leetcode.com/problems/contains-duplicate-ii/
"""
class Solution:
    def containsNearbyDuplicate(self, nums ,k):
        dict_store=dict()
        count=1
        for index, ele in enumerate(nums):
            #print(dict_store)
            if ele not in dict_store.keys():
                count=1
                loc=[index]
                dict_store[ele]=[count,loc]
            else:
                #print(dict_store)
                count=dict_store[ele][0]+1
                dict_store[ele][1].append(index)
                #print(count,loc)
                dict_store[ele][0]=count
        #print(dict_store)
        for key, val in dict_store.items():
            if val[0]>1:
                for i in range(len(val[1])-1):
                    if abs(val[1][i]-val[1][i+1])<=k:
                        return True
        else:
            return False
                    
                    
                
nums=[1,2,3,1]
k=3
print(Solution().containsNearbyDuplicate(nums,k))     
                