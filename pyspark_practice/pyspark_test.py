import os,sys
#os.environ['PYSPARK_PYTHON'] = r'C:\Users\abhi3\Documents\work\ds-algo\pyspark_practice\spark-3.5.3-bin-hadoop3\spark-3.5.3-bin-hadoop3\python'
os.environ["SPARK_HOME"]=r"C:\Users\abhi3\Documents\work\ds-algo\pyspark_practice\spark-3.5.3-bin-hadoop3\spark-3.5.3-bin-hadoop3"
#os.environ["PYTHONPATH"]=r'$(ZIPS=("$SPARK_HOME"/python/lib/.zip); IFS=:; echo "${ZIPS[]}"):$PYTHONPATH'
os.environ["JAVA_HOME"]=r'C:\Program Files\Java\jre1.8.0_431'
os.environ["HADOOP_HOME"]=r'C:\Users\abhi3\Documents\work\ds-algo\pyspark_practice\spark-3.5.3-bin-hadoop3\spark-3.5.3-bin-hadoop3\hadoop'
#os.environ["PYSPARK_DRIVER_PYTHON"]="jupyter"
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable
#os.environ["PYSPARK_PYTHON"]="python"
#r'C:\Users\abhi3\anaconda3\Lib\site-packages\pyspark'
#import findspark
#findspark.init()#spark_home=r"C:\Users\abhi3\Documents\work\ds-algo\pyspark_practice\spark-3.5.3-bin-hadoop3\spark-3.5.3-bin-hadoop3")
# print(findspark.find())

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MyApp")\
    .master("local[*]")\
    .config("spark.ui.port", "4041")\
    .getOrCreate()
sc = spark.sparkContext

sc.setLogLevel("DEBUG")
from datetime import datetime, date
#import pandas as pd
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(a=1, b=2., c='string1', d=date(2000, 1, 1), e=datetime(2000, 1, 1, 12, 0)),
    Row(a=2, b=3., c='string2', d=date(2000, 2, 1), e=datetime(2000, 1, 2, 12, 0)),
    Row(a=4, b=5., c='string3', d=date(2000, 3, 1), e=datetime(2000, 1, 3, 12, 0))
])
df.show()
input("Press to exit")