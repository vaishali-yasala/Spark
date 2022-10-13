#!/usr/bin/env python
# coding: utf-8

# # Union Transformation
# 
# 

# In[1]:


from pyspark.sql import SparkSession

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("Union Transformation") \
        .getOrCreate()
    
    #Two lists 
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    rdd = spark.sparkContext.parallelize(list1, 5)
    rdd1 = spark.sparkContext.parallelize(list2, 2)
    
    #with union() they are both combined
    union_rdd = rdd.union(rdd1)
    
    print(union_rdd.collect())
    


# In[2]:


#Reading two files 
file1= spark.read.text("file.txt")

print("Printing files1_rdd: ", file1.show())

file2= spark.read.text("tech_overview.txt")
print("Printing files2_rdd: ", file2.show())


# In[3]:


#Joining them 
str_rdd = file1.union(file2)
print(str_rdd.show())

