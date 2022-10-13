#!/usr/bin/env python
# coding: utf-8

# # groupByKey( ) Transformation 
# 
# By definition, When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable<V>) pairs. 
# 
# To group the values for each key in the RDD into a single sequence. 

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("groupByKey Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#path of the data file on the local machine
data_file = '/Users/vaishaliyasala/Desktop/Github/Spark/Exercise_Dependencies/sales_data.csv'

#Read the csv into a dataframe
df = spark.read.csv(data_file, header = True, )

df1 = df.select(df["InvoiceNo"],df["UnitPrice"],df["Quantity"]).repartition(4)

print(df1.printSchema())

#Creating view of the dataframe of with 3 required columns and sample of 3% of data
sample_df = df1.sample(0.03,25)

sample_df.show()


# In[2]:


# apply a map() transformation to rdd to create (K, V) pairs

#In this key-value pair, key is the InvoiceN0 and the tuple (UnitPrice, Quantity) is the value

rdd1 = sample_df.rdd.map(lambda x : (x[0],(x[1],x[2])))
print("Number of elements =",len(rdd1.collect()))
print("Number of Partitions =",rdd1.getNumPartitions())


# In[3]:


# apply groupByKey() transformation to rdd2 to return a dataset of (K, Iterable<V>) pairs.

rdd2 =rdd1.groupByKey()
print("Number of elements =",len(rdd2.collect()))
print("Number of Partitions =",rdd2.getNumPartitions())
print("----------")

print(rdd2.collect())


# ### From result of Input block 2 and 3, we can see the number of elements decreased because they are grouped together when they have the same key. 

# In[4]:


# RDD.mapValues - Pass each value in the key-value pair RDD through a map function without changing the keys
# mapValues operates on the values only
# this also changes the original RDD's partitioning.

print("rdd2.mapValues().collect() = ", rdd2.mapValues(lambda values: list(values)).collect())


# ### groupByKey() Transformation cannot be used on large datasets.
# Because all the elements from each partition will be sent over the network to the Task performing the reduce operation. Since the data is not combined or reduced on the map side, we transferred all the elements over the network during shuffle. 
# Since all elements are sent to the task performing the aggregate operation, the number of elements to be handled by the task will be more and could possibly result in an Out of Memory exception.
# 
# 
