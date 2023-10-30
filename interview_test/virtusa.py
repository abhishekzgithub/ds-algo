"""
Year Quatrer sale_amount 
2017 1 2437.98 
2017 2 4467.58 
2017 3 1045.72 
2017 4 5739.6

2018 1 3735.65 
2018 2 2178.91 
2018 3 6754.2 
2018 4 5321.09 

2019 1 4216.63 
2019 2 6425.87 
2019 3 7210.72 
2019 4 8764.72

1. whats the max saleamount quarter in a year?

select * from (
select *,
dense_rank() over (partition by year order by sale_amount desc) as sale_rank
from sales
) rank_sales
where sale_rank=1

select max(sale_amount)
from sales
group by year

2. whats the percentage of improvement in that year, quarter by quarter?

with cte as sale_sum(
select sum(sale_amount) as summ_sales
from sales
group by year
)

select  100*(sale_amount/summ_sales)
from sales join sale_sum on sales.year=sale_sum.year
group by year


Id First_name Last_name Full_name 
1 ABC xyz ABC xyz 
2 Bca LLP.com BCa LLp.com 
3 tuv Pvt.LTD tuv Pvt.LTD 
4 SRS null SRS LLp.com 
5 ABC's null ABC's sample 
6 null Data sam ple Data

--if pvt.com or llp ,no need to replace it, if not, replace it
from pyspark.sql.functions import udf


def func(row):
    fullname=row.full_name
    if row.first_name ==None and row.last_name!=None and ['LLp.com','Pvt.LTD'] not in fullname:
        row.first_name=fullname.replace(row.last_name,"")
    elif row.first_name !=None and row.last_name==None and ['LLp.com','Pvt.LTD'] not in fullname:
        row.last_name=fullname.replace(row.first_name,"")
    return row
        
dataframe=dataframe.map(lambda x: func(x))


Cunningham was, in part, inspired by the Apple HyperCard, which he had used. HyperCard, 
however, was single-user.[16] Apple had designed a system allowing users to create virtual "card stacks" supporting links among the various cards. Cunningham developed Vannevar Bush's ideas by allowing users to "comment on and change one another's text."[2][17] Cunningham says his goals were to link together people's experiences to create a new literature to document programming patterns, and to harness people's natural desire to talk and tell stories with a technology that would feel comfortable to those not used to "authoring

--
single-user ending with fullstop

however

roweveh

"""

strval="""

Cunningham was, in part, inspired by the Apple HyperCard, which he had used. HyperCard, 
however, was single-user.[16] Apple had designed a system allowing users to create virtual "card stacks" supporting links among the various cards. Cunningham developed Vannevar Bush's ideas by allowing users to "comment on and change one another's text."[2][17] Cunningham says his goals were to link together people's experiences to create a new literature to document programming patterns, and to harness people's natural desire to talk and tell stories with a technology that would feel comfortable to those not used to "authoring

"""
strval1="Cunningham was ."

def revert_char(val):
    start=val[0]
    end=val[len(val)-1]
    return end+val[1:len(val)-1]+start

def main(val):
    list_val=val.split(" ")
    full_stop_index=0
    for ele in range(len(list_val)):
        if "." in list_val[ele]:
            full_stop_index=ele
    for indx in range(len(list_val)-full_stop_index):
        list_val[indx]=revert_char(list_val[indx])
        list_val=list_val[::]
    return " ".join(list_val)

#print(revert_char("Cunningham"))
print(main(strval1))