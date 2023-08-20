# Amt	TRNID	TRNDT
# 1245000	1	09-Aug
# 1245000	2	09-Aug
# 500000	3	09-Aug
# 955000	4	10-Aug
# 955000	5	10-Aug
# 1500000	6	10-Aug
"""
with rank_cte as (
select amt, trndt, dense_rank() over(order by amt desc) as amt_rank
from transaction
)
select amt,trndt
from rank_cte
where amt_rank=1
group by 1,2

"""
import pandas as pd
dataframe=pd.read_csv("transaction.csv")
df1=dataframe.groupby("trndt").max("amt")["amt","trndt"]
df1.head()

