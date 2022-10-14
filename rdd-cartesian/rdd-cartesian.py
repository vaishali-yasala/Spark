#!/usr/bin/env python
# coding: utf-8

# # cartesian( ) Transformation
# 
# Return the cartesian product of this RDD and another one, that is, the RDD of all pairs of elements (a,b) where a is in the first RDD and b is in the second RDD.

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("cartesian Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#First RDD
a = [('a', 2.5), ('b', 4.0), ('c', 5.5) ]

rdd1 = spark.sparkContext.parallelize(a)
print(rdd1.collect())

#Second RDD
b = [('u', 3.5), ('v', 4.0), ('x', 2.5), ('y', 3.5), ('z', 10.0) ]

rdd2 = spark.sparkContext.parallelize(b)
print(rdd2.collect())



# In[2]:


cartesianValue = rdd1.cartesian(rdd2)
print("count = ", cartesianValue.count())
print("resultant RDD =", cartesianValue.take(5))

