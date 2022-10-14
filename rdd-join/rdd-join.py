#!/usr/bin/env python
# coding: utf-8

# # join Transformation
# 
# When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (V, W)) pairs with all pairs of elements for each key. Outer joins are supported through leftOuterJoin, rightOuterJoin, and fullOuterJoin. Below, these are explored.
# 
# syntax of join for DataFrame - join(dataset,joinExprs,joinType) 

# In[1]:


from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .master("local[2]") \
        .appName("join Transformation") \
        .enableHiveSupport() \
        .getOrCreate()

#key-value pairs from dataset 1
kvPair = [(1,"v"), (1,"i"), (2, "s"), (3,"h"), (4,"a") ]

kvPairRDD = spark.sparkContext.parallelize(kvPair)
print(kvPairRDD.collect())

#key-value pairs from dataset 2
otherKvPair = [(1,"y"), (1,"l"), (2, "d"), (3,"m"), (8,"z2") ]

otherKvPairRDD = spark.sparkContext.parallelize(otherKvPair)
print(otherKvPairRDD.collect())


#join() transformation to join both datasets to return (K, (V,W))
joined = kvPairRDD.join(otherKvPairRDD)
print("joined.count(): ", joined.count())
print("joined.collect(): ", joined.collect())


# In[2]:


#Let us look at another example to understand various joinType

data1 = [(1,"John",-1,"2019","10","M"), \
       (2,"Alex",1,"2015","20","M"), \
       (3,"Williams",1,"2016","10","M"), \
       (4,"Arjun",2,"2010","10","F"), \
       (5,"Brown",2,"2012","40",""), \
       (6,"Brown",2,"2012","50","") \
  ]

data1_columns = ["employee_id", "name", "superior_emp_id", "year_joined", "emp_dept_id","gender"]

df1 = spark.createDataFrame(data= data1, schema = data1_columns)
df1.printSchema()
df1.show(truncate=False)


# In[3]:


data2 = [("Finance",10), \
         ("Marketing",20), \
         ("Sales",30), \
         ("IT",40)]

data2_columns = ["dept_name","dept_id"]

df2 = spark.createDataFrame(data = data2, schema = data2_columns)
df2.printSchema()
df2.show(truncate=False)


# In[4]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"inner") \
     .show(truncate=False)


# In[5]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"cross") \
     .show(truncate=False)


# In[6]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"outer") \
     .show(truncate=False)


# In[7]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"fullouter") \
     .show(truncate=False)


# In[8]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"left") \
     .show(truncate=False)
  


# In[9]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"leftouter") \
     .show(truncate=False)


# In[10]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"right") \
     .show(truncate=False)


# In[11]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"rightouter") \
     .show(truncate=False)


# In[12]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"leftsemi") \
     .show(truncate=False)


# In[13]:


df1.join(df2, df1.emp_dept_id == df2.dept_id,"leftanti") \
     .show(truncate=False)
   

