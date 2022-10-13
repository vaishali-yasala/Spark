#!/usr/bin/env python
# coding: utf-8

# # aggregateByKey( ) Transformation 
# 
# Syntax of this transformation
# 
# source_rdd.aggregateByKey(zeroValue, lambda1, lambda2) --> target_rdd
# 
# aggregateByKey(
#    zeroValue,
#    seqFunc,
#    combFunc,
#    numPartitions=None,
#    partitionFunc=<function portable_hash>
#  )
#     
# Aggregate the values of each key, using given combine functions and a neutral "zero value". This function can return a different result type, U, than the type of the values in this RDD, V. Thus, we need one operation for merging a V into a U and one operation for merging two U's. The former operation is used for merging values within a partition, and the latter is used for merging values between partitions. To avoid memory allocation, both of these functions are allowed to modify and return their first argument instead of creating a new U.

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
sample_df = df1.sample(0.02,134)

sample_df.show()


# In[2]:


# apply a map() transformation to rdd to create (K, V) pairs

#In this key-value pair, key is the InvoiceNo and the number is the value

#whereas the price is obtained from UnitPrice*Qunatity


import decimal


def get_price(x3):
    try:
        UnitPrice = decimal.Decimal(x3[2])
        convert = UnitPrice * decimal.Decimal(x3[1])
    except decimal.InvalidOperation:
           print("Invalid input")
    key = x3[0]
    price = convert
    return (key, price)


new_rdd = df1.rdd.map(lambda x : get_price(x))
print("Number of elements =",len(new_rdd.collect()))
print("Number of Partitions =",new_rdd.getNumPartitions())



# In[3]:


#Showing the Result for the dataframe sample sample_df
sample_df_rdd = sample_df.rdd.map(lambda x : get_price(x))

print(sample_df_rdd.collect())


# In[4]:


# rdd2 = rdd1.aggregateByKey(
#    zero_value,
#    lambda x,y: (x[0] + y,    x[1] + 1),
#    lambda x,y: (x[0] + y[0], x[1] + y[1])
# )

# Where the following is true about the meaning of each x and y
# pair above :
#
# First lambda expression for Within-Partition Reduction Step::
#    x: is a TUPLE that holds: (runningSum, runningCount).
#    y: is a SCALAR that holds the next Value

# Second lambda expression for Cross-Partition Reduction Step::
#    x: is a TUPLE that holds: (runningSum, runningCount).
#    y: is a TUPLE that holds: (nextPartitionsSum, nextPartitionsCount).


# we are showing for each key (invoice), U is sum of prices for all items and no of items
price_and_Count = new_rdd.aggregateByKey(
        (0, 0), \
        lambda x, y: (x[0]+y, x[1]+1), \
        lambda rdd1, rdd2: (rdd1[0] + rdd2[0], rdd1[1] + rdd2[1]) \
    )
    

print("sum_count.count() = ", price_and_Count.count())
print("sum_count.collect() = ", price_and_Count.collect())

