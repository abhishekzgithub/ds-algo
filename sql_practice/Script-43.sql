/*
 * https://leetcode.com/problems/tree-node/
 * +-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id is the column with unique values for this table.
Each row of this table contains information about the id of a node and the id of its parent node in a tree.
The given structure is always a valid tree.
LEV1 LEV2 LEV3 M2
 */
--with cte as (
--select 
--*
--from tree t1
--where not exists (
--select * from tree t2 where t1.parent_id=t2.id
--)
--)
--select cte.parent_id as level1
--,cte.id as level2
--,tree.id as level3
--from cte 
--join tree on cte.id=tree.parent_id

-----------------
--find parent leaf and child node
select * from tree;









;