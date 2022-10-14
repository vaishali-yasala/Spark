#!/usr/bin/env python
# coding: utf-8

# # Sample Transformation
# 
# Sample() Transformation is get random sample records from the dataset. This can be helpful when there is a larger dataset and wanted to test a subset of the data.
# 
# 
# Syntax of the Sample() Transformation:
# 
# sample(WithReplacement, fraction, seed=None)
# 
# fraction - Fraction of rows to generate, range[0.0,1.0]. Note that it doesn't guarantee to provide the exact number the exact number of the fraction of records.
# 
# seed - Seed for sampling (default a random seed). Used to reproduce the same random sampling.
# 
# withReplacement - Sample with replacement or not (default False).

# In[7]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Sample Transformation") \
        .getOrCreate()

#DataFrame created with 100 records and getting a 5% sample of records
rdd = spark.range(100)
print(rdd.sample(0.05).show())


# In[2]:


#Get 5% sample of records and seed is used to reproduce the same random sample whenever there is a need to
#regenerate the same results as tested at a different phase.

print(rdd.sample(0.05, 25).show())


# In[5]:


#Different Results with only fraction usage
print(rdd.sample(0.05).show())

#the same results as above for the same seed.
print(rdd.sample(0.05,25).show())


# In[6]:


#To get random sample with repeated values, withReplacement has to be True.

print(rdd.sample(True,0.5,25).show())

print(rdd.sample(False,0.5,25).show())

