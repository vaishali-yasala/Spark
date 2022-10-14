#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("aggregrate Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#path of the data file on the local machine
data_file = '/Users/vaishaliyasala/Desktop/Github/Spark/Exercise_Dependencies/sales_data.csv'

#Read the csv into a dataframe
df = spark.read.csv(data_file, header = True, )

df1 = df.select(df["InvoiceNo"],df["Quantity"]).repartition(4)

print(df1.printSchema())

#Creating view of the dataframe of with 3 required columns and sample of 3% of data
sample_df = df1.sample(0.01,25)

sample_df.show()


# In[2]:


# apply a map() transformation to rdd to create (K, V) pairs

#In this key-value pair, key is the InvoiceN and Quantity is the value

rdd1 = df1.rdd.map(lambda x : (x[0],int(x[1])))
print("Number of elements =",len(rdd1.collect()))
print("Number of Partitions =",rdd1.getNumPartitions())


# In[3]:


# apply a reduceByKey() transformation on rdd1 to create a (key, value) pair

#  where key is the InvoiceNo and value is sum of prices for each key 

#we can create more partitions than its parent RDD.

rdd2 = rdd1.reduceByKey(lambda a, b: a+b)

print("Number of elements =",len(rdd2.collect()))
print("Number of Partitions =",rdd2.getNumPartitions())
print(rdd2.take(10))


# In[4]:


#Sort by key ascending

sort_key = rdd2.sortByKey(ascending = True)
print("Number of elements =",sort_key.take(10))


# In[5]:


#Sort by key descending

sort_key = rdd2.sortByKey(ascending = False)
print("Number of elements =",sort_key.take(10))

