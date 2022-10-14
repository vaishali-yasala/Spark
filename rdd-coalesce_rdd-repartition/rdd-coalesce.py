#!/usr/bin/env python
# coding: utf-8

# # coalesce( ) Transformation
# 

# In[1]:


from pyspark.sql import SparkSession
import pyspark

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("coalesce Transformation") \
        .enableHiveSupport() \
        .getOrCreate()


# In[2]:


def debug_a_partition(iterator):
    print("==begin-partition=")
    for x in iterator:
        print(x)
    #end-for
    print("==end-partition=")

    
names_list =["ABC - 1", "DEF - 1","GHI-1", "ABC - 2", "DEF - 2","GHI -2", \
             "ABC - 3", "DEF - 3","GHI -3","ABC - 4", "DEF - 4","GHI -4"]

names_rdd = spark.sparkContext.parallelize(names_list,4)

print("From local[4] =",names_rdd.getNumPartitions())
print("Repartition elements : ", names_rdd.foreachPartition(debug_a_partition))



# In[3]:


#reparition shuffles the data completely
repartition_rdd = names_rdd.repartition(3)
print("coalesce elements : ", repartition_rdd.foreachPartition(debug_a_partition))


# In[4]:


#coalesce combines the partition close to it
coalesce_rdd = names_rdd.coalesce(3)
print("Repartition size : ", coalesce_rdd.foreachPartition(debug_a_partition))


# In[5]:


#Reading data from a file on the local machine
data_file_path = "/Users/vaishaliyasala/Desktop/Github/Spark/Exercise_Dependencies/SalesJan2009.csv"

df = spark.read.csv(data_file_path, header = True )

df1 = df.select(df["Name"],df["Country"]).repartition(4)

print("Count in the original data=", df1.count())

#Filter the names only from country United States
filtered_rdd = df1.rdd.filter(lambda x: (x[1] == "United States"))


filtered_rdd.toDF(["Name", "Country"]).show(5)


print("Filtered data Count =", filtered_rdd.count())
print("Number of Partitions =", filtered_rdd.getNumPartitions())



# In[6]:


#As the filtered data count increased significantly, we can reduce the number of partitions from 4 to 2
#It doesn't change the resultant RDD as seen from the outputs of both before and after coalesce transformation
#Only data changes in each partition


names_coalesce_rdd = filtered_rdd.coalesce(2)

names_coalesce_rdd.toDF(["Name", "Country"]).show(5)

print("Number of Partitions =", names_coalesce_rdd.getNumPartitions())

