#!/usr/bin/env python
# coding: utf-8

# # coalesce( ) Transformation
# 

# In[1]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("pipe Transformation") \
        .enableHiveSupport() \
        .getOrCreate()


# In[2]:


#Reading data from a file on the local machine
data_file_path = "/Users/vaishaliyasala/Desktop/Github/Spark/Exercise_Dependencies/SalesJan2009.csv"

df = spark.read.csv(data_file_path, header = True )

df1 = df.select(df["Name"],df["Country"]).repartition(4)

print("Count in the original data=", df1.count())


#Filter the names only from country United States
names_rdd = df1.rdd.filter(lambda x: (x[1] == "United States"))

filtered_data = spark.createDataFrame (data = names_rdd, schema = df1.printSchema())
filtered_data.show(5)

print("Filtered data Count =", names_rdd.count())
print("Number of Partitions =", names_rdd.getNumPartitions())



# In[3]:


#As the filtered data count increased significantly, we can reduce the number of partitions from 4 to 2
#This doesn't change the results as seen from the outputs of both before and after coalesce transformation

names_coalesce_rdd = names_rdd.coalesce(2)

coalesced_data = spark.createDataFrame (data = names_coalesce_rdd, schema = df1.printSchema())
coalesced_data.show(5)

print("Number of Partitions =", names_coalesce_rdd.getNumPartitions())

