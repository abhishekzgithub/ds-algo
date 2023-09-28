# from pyspark.sql import SparkSession

# spark=SparkSession.builder.appName("test").getOrCreate()
# word="abcdefa"
# word_dict={}
# spark_df=spark.sparkContext.paralleize(word).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b)

abc=[1,2,3,4,3]
df=set()

for ele in abc:
    if ele not in df:
        df.add(ele)

print(df)

"""
select *, rank() over(partition by empid)
from emp

"""
