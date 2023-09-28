# import pyspark
# from pyspark.sql import SparkSession

# spark=SparkSession.builder.appName("test").options({"jar":"<postgres.jar>"}).getOrCreate()

# sc=spark.read.options({"host":"postgres",
#                        "user":"postgres",
#                        "password":"postgres",
#                        "url":"<url>",
#                        "database":"dbname",
#                        "table":"employee"})#.collect()

"""
emp:
id
name
managerid
salary
cityid
deptid

dept:
id
name

city:
id
name
stateid

state:
id
name

1. get the number of employees in  all the city

select c.id, count(e.id) as employee_count
from emp e1 left join city c on emp.cityid=c.id join state s on s.id=c.stateid 

group by c.id,e.id

2. total salary of each department

select e.deptid as department_id, d.name as department_name, sum(e.salary) as department_salary
from emp e join dept d on e.deptid=d.id
group by e.deptid,d.name

emp
id salary departmentid
1   2000    1
2   3000    2
3   4000    1

department
id  name
1   a
2   b

output:
department_id  department_name department_salary
1               a                  6000
2                b               3000


3. cross join
select e.deptid as department_id, d.name as department_name, sum(e.salary) as department_salary
from emp e cross join dept d 

4. right join

t1          t2
id name     id name
1   t1      1   t21
2           3   t23
3           4
4           6
5           7
            8

            
t1 left join t2 on t1.id=t2.id            
t1.id t2.id
1,1
2, null
3,3
4,4
5,null

t1 right join t2 on t2.id=t1.id
t2.id   t1.id
1       1
3       3
4       4
6       null
7       null
8       null
            
"""

def fib(num,f0=5,f1=9):
    if not num:
        return f0
    return fib(num-1,f0=f1,f1=f0+f1)

print(fib(0))
print(fib(4))
    

def func(num):
    f0=5
    f1=9
    temp=0
    while num:
        f0,f1=f1,f0+f1
        num-=1
    return f0

# print(func(4))
# print(func(3))
# print(func(1))
# print(func(0))
#series=5,9,14,23,37,60
#series=100