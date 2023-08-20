""""
abc=[5,2,7,9,11,20,3]
"""
# abc=[5,2,7,9,11,20,3]
# target=12
# dict_b={}
# for ele in range(len(abc)):
#     diff=target-abc[ele]
#     if diff not in dict_b:
#         dict_b[abc[ele]]=diff
#     else:
#         print(diff,dict_b[diff])

#################
arr1=[1,None,2,3,None]
arr2=[1,7,2,3,5]

#         1
#     None    2
#         3       None


# [None,1,2,3,None]

# [1,7,2] [3,5]
# [1,7] [2]

# [1,2,7] [3,5]

# [1,2,3,5,7]

# def merge(arr):
#     pass

# def merge_sort(arr):
#     if len(arr)==0:
#         return
#     l,r=0,len(arr)-1
#     mid = l+r/2
#     left_array,right_array=arr[:mid],arr[mid+1:r]
    
#     return merge_sort(left_array), merge_sort(right_array)

"""
insert into table tbl values (

--select * from tbl2
id 1

)


EMP:
id:
name:
salary:
managerid:

1 gaurav 1000 null
2 abhishek 2000 1
3 abhishek2 3000 1

1 gaurav 1000 null
2 abhishek 2000 1
3 abhishek2 3000 1

select e1.managerid, e1.name as managername, avg(e2.salary)
from emp e1 left join emp e2
on e2.managerid=e1.id
group by e2.managerid

"""
