# [11:21 AM] Ekta Rajkumar Panjwani

 

# city	serial3
# Delhi	5
# Banglore	6
# Chennai	7

 

# [11:22 AM] Ekta Rajkumar Panjwani

 

# state
# Delhi
# KA
# TN

import pandas as pd
from pyspark.sql.function import *
df=df.withColumn("state",when((col("city") =='Delhi' & col("serial3")==5),"Delhi").otherwise("null")
                 )
"""
city	state	code	serial2
Delhi	Delhi	0	(0, 1)
Banglore KA	    1	(1, 1)
Chennai	TN	    2	(2, 1)
"""
df["serial2"]=df["code"].apply(lambda x:(x,1) )
#df=df.withColumn("serial2",case())

""" emp
city	    state	code	visit_date	id
Delhi	    Delhi	0	    01-01-2023	ashu    1
Banglore	KA	    1	    18-01-2023	ashu    1
Chennai	    TN	    2	    01-02-2023	ashu    1
Chennai	    TN	    2	    01-02-2023	ashu    2

>16

select * 
        from (select * ,lag(visit_date,1) as prev_day from emp) 
        where datediff(visit_date,prev_day)>16
        

update emp set id='ashu'
where id is null;

select city, state, code, visit_date
from emp
where id is null
or city is null
or state is null
or code is null
or visit_date is null
"""