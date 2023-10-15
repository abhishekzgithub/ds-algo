# nest_dict = {'key1': {'a': 7, 'b': 9, 'c': 12},
# 'key2': {'a': 15, 'b': 19, 'c': 20},
# 'key3': {'a': 5, 'b': 10, 'c': 2}}
# total_sum=0
# for key,val in nest_dict.items():
#     if val.get("b",None):
#         total_sum+=val["b"]

# print(total_sum) #38

from pyspark.sql.functions import udf

@udf
def change_lower_to_upper_case(dataframe):
    dataframe=dataframe.map(lambda x: x[0].upper())
    return dataframe
#psycopg2,psycopg
"""
pl/sql
begin transaction;

end transaction;


"""