#two sum leet code

class Solution:
    def two_sum(self, nums, target):
        for i in range(len(nums)):
            remaining_target = target - nums[i]
            remaining_set = set(nums) - set({nums[i]})
            print(remaining_set, nums)
            for j in remaining_set:
                if j==remaining_target:
                    return j, nums[i]

    def two_sum_dict(self, nums, target):
        dict_with_index = {i: k for i, k in enumerate(nums) }
        seen_dict={i:False for i in dict_with_index.keys() }
        for j in dict_with_index.keys():
            seen_dict[j]=True
            remaining_target = target - dict_with_index[j]
            for k in dict_with_index.keys():
                if not seen_dict[k] and dict_with_index[k]==remaining_target:
                    return j,k

            #remaining_index = [i for i in dict_with_index.keys() if dict_with_index[i]==remaining_target ]
            #return j, remaining_index[0] if len(remaining_index)>0 else None
        #return dict_with_index
        

nums=[3,2,4]#[2,7,5,11]
target=6
print(Solution().two_sum_dict(nums, target))