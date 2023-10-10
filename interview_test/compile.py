"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

[-1,-2,-3,-4]
"""
nums = [-2,1,-3,4,-1,2,1,-5,4] #6
nums=[-1,-2,-3,-4]
max_summ=nums[1]
summ=0
for ele in range(len(nums)):
    if summ<0:
        summ=0
    summ=summ+nums[ele]
    max_summ=max(max_summ,summ)
print(max_summ)


"""

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | None      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+

101 john A None 
102 Dan  A 101

select m1.id as managerId,m1.name as manager_name 
from employee e1, employee m1
where 1=1
and m1.managerId=e1.id
group by m1.managerId

having count(e1.name)>=5

"""
