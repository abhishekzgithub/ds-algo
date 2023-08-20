# abc={1,2,3,4,5}
# dbc=set()
# l,r=0,len(abc)-1
# while len(abc)>0:
#     ele = abc.pop()
#     dbc.add(ele)
#     # abc[l],abc[r]=abc[r],abc[l]
#     # l+=1
#     # r-=1
# print(dbc)

# # for ele in range(len(abc)-1,-1,-1):
# #     dbc.append(abc[ele])
# # print(dbc)

# lambda x,y,z : if x>y and x>z elif y>x and y>z else z

class Test(object):
    counter=0
    def __new__(cls):
        cls.counter+=1
        print(cls.counter)

    def __init__(self):
        self.counter+=1
        print(self.counter)


test=Test()

test=Test()

test=Test()


"""
Order:
customername

orderdate:

abc 18-08-2023
abc 19-08-2023
abc1 18-08-2023
abc1 19-08-2023

with cte as (
select *, lag() over(order by orderdate desc) as prev_date

)

select * from cte
where datediff(orderdate,prevdate)>2
group by customername


"""