import pyspark
from pyspark.sql import SparkSession
import findspark
findspark.init()
findspark.find()

JAR_LOCATION=r"C:\Users\abhi3\Documents\work\ds-algo\pyspark_practice\postgresql-42.5.2.jar"
URL = "jdbc:postgresql://localhost:5432/postgres"
PROPERTIES = {
    "user": "postgres",
    "password": "123",
    "driver": "org.postgresql.Driver"
}

spark = (SparkSession.builder.master("local[*]")
        .config("spark.driver.maxResultSize",  "0")
        .config("spark.executor.memory", "4g")
         #.config("spark.jars", jar_location) # never use this
        #.config("spark.driver.extraClassPath", JAR_LOCATION)
        #.config("spark.driver.maxResultSize",  "0")
        .getOrCreate())


def create_rdd(spark):
    employee = [("Radhika",10), 
        ("Kaavya",20), 
        ("Varnika",30), 
        ("Akshay",40) 
      ]
    rdd = spark.sparkContext.parallelize(employee)
    dataframee = rdd.toDF()
    dataframee.printSchema()
    dataframee.show()

def read_postgres_connection(spark,table_name="orders"):
    df = spark.read.jdbc(URL, table_name, properties=PROPERTIES)
    return df.show()
#read_postgres_connection(spark)
create_rdd(spark)