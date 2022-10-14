#!/usr/bin/env python
# coding: utf-8

# # cogroup( ) Transformation

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("cogroup Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#key-value pairs from dataset 1
kvPair = [(1, 2.5), (2, 4.0), (3, 5.5) ]

kvPairRdd = spark.sparkContext.parallelize(kvPair)
print(kvPairRdd.collect())

#key-value pairs from dataset 2
otherKvPair = [(1, 3.5), (1, 4.0), (2, 2.5), (2, 3.5), (4, 10.0), (3, 4.5) ]

otherKvPairRdd = spark.sparkContext.parallelize(otherKvPair)
print(otherKvPairRdd.collect())


# In[2]:


#kvPairRdd has (K,V)
#otherKvPairRdd has (K,W)
#cogroup returns a dataset of (K, (Iterable<V>, Iterable<W>)) tuples. 
#That means for kvPairRDD, there are a list of values for each key in Iterable<V>
#That means for otherKvPairRDD, there are a list of values for each key in Iterable<W>

cogroupKvRdd = kvPairRdd.cogroup(otherKvPairRdd)
print(cogroupKvRdd.collect())


# In[3]:


#Let us look at the actual values

print([(x,tuple(map(list,y)))for x,y in sorted(list(cogroupKvRdd.collect()))])

