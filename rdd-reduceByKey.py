#!/usr/bin/env python
# coding: utf-8

# # reduceByKey( ) Transformation
# 
# <i>groupByKey() Transformation cannot be used on large datasets. To solve this problem, let us look us at reduceByKey() Transformation. reduceByKey is optimized with a map side combine. This means it performs the merging locally on each mapper for each key before sending results to a reducer operation. After that, the values are combined for each key using an associative and commutative reduce function.
# By this, less elements are sent over the network.

# In[1]:


from pyspark.sql import SparkSession
import pyspark

spark = SparkSession \
        .builder \
        .master("local[4]") \
        .appName("Sample Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#path of the data file on the local machine
data_file = '/Users/vaishaliyasala/Desktop/Github/Spark/Exercise_Dependencies/sales_data.csv'

#Read the csv into a dataframe
df = spark.read.csv(data_file, header = True )

df1 = df.select(df["InvoiceNo"],df["UnitPrice"],df["Quantity"]).repartition(4)

print(df1.printSchema())

#Creating view of the dataframe of with 3 required columns and sample of 2% of data
sample_df = df1.sample(0.02,134)

sample_df.show()


# In[2]:


# apply a map() transformation to rdd to create (K, V) pairs

#In this key-value pair, key is the InvoiceNo and the number is the value

#whereas the number is obtained from UnitPrice*Qunatity


import decimal


def get_price(x3):
    try:
        UnitPrice = decimal.Decimal(x3[2])
        convert = UnitPrice * decimal.Decimal(x3[1])
    except decimal.InvalidOperation:
           print("Invalid input")
    key = x3[0]
    number = convert
    return (key, number)


rdd1 = df1.rdd.map(lambda x : get_price(x))
print("Number of elements =",len(rdd1.collect()))
print("Number of Partitions =",rdd1.getNumPartitions())


#Showing the Result for the dataframe sample sample_df
sample_df_rdd = sample_df.rdd.map(lambda x : get_price(x))

print(sample_df_rdd.collect())


# In[3]:


# apply a reduceByKey() transformation to rdd1 to create a (key, value) pair

#  where key is the InvoiceNo and value is number

#we can create more partitions than its parent RDD.

rdd2 = rdd1.reduceByKey(lambda a, b: (a,b),10)


print(len(rdd2.collect()),rdd2.getNumPartitions())
print("Number of elements =",len(rdd2.collect()))
print("Number of Partitions =",rdd2.getNumPartitions())


# ### From result of Input block 2 and 3, we can see the number of elements decreased because they are merged together when they have the same key. Additionally, it is optimized with a map side combine.

# In[4]:


#Below we can the result of reduceByKey() applied on sample_df_rdd

print(sample_df_rdd.reduceByKey(lambda a, b: (a,b),10).collect())

