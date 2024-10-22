import os
os.environ['PYSPARK_PYTHON'] = r'C:\Users\abhi3\anaconda3\python.exe'
os.environ["SPARK_HOME"]=r'C:\Users\abhi3\anaconda3\Lib\site-packages\pyspark'
import findspark
findspark.init()
# print(findspark.find())

# from pyspark import SparkConf, SparkContext

# # Configure Spark
# conf = SparkConf().setAppName("WordCount")
# sc = SparkContext(conf=conf)

# # Read input file
# text_file = sc.textFile("input.txt")

# # Perform word count
# word_counts = text_file.flatMap(lambda line: line.split(" ")) \
#              .map(lambda word: (word, 1)) \
#              .reduceByKey(lambda a, b: a + b)

# # Save results to a file
# word_counts.saveAsTextFile("output")

# # Stop Spark context
# sc.stop()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp").getOrCreate()
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
print(df)