"""
table:
product
will index be checked
#product like %%

employee

id designation promotion
10  manager      1st Dec,2022
10  senior manager  1st May,2023

promoted less than 1 year;exceptional

id status
1   Y
2   N
3   Y
4   Y
5   Y
6   Y
7   N
8   Y
9   Y
10  Y

id status

col1 col2 col3
3   4   5
8   9   10

source destination distance
chennai bangalore   300
bangalore   chennai 300
hyd     bangalore   300
bangalore hyd       300
mumbai pune         600
pune   mumbai       600

select least(source),greatest(destination), max(distance)
from location
group by least(source), greatest(destination)


"""