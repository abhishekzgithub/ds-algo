"""
Find or join two different dataframe with different schemas
You need to create columns in both the dataframe and make it similar and the use unionByName
"""
from pyspark.sql import SparkSession

sparkz=SparkSession.builder.appName("test").getOrCreate()

df1=sparkz.sparkContext.parallelize(range(1,10))
df1=df1.toDF(["A"])

df2=sparkz.sparkContext.parallelize(range(10,20))
df2=df2.toDF(["B"])

df1=df1.unionByName(df2)

