#!/usr/bin/env python
# coding: utf-8

# # flatMap Transformation

# In[1]:


from pyspark.sql import SparkSession

if __name__ == '__main__':
#Create the spark session
     spark = SparkSession.builder.appName("flatMap transformation").getOrCreate()


#Dataset
data = ["list of strings", "to test", "flatMap", "Transformation", "and compare it", "with map Transformation"]

#Show the dataset
print('Dataset =', data)

rdd = spark.sparkContext.parallelize(data)
print('rdd =', rdd.collect())


# In[2]:


#Printing all the elements in the RDD
for element in rdd.collect():
    print(element)


# In[3]:


#Map - map() is the transformation takes a function and applies the function to each element of the input RDD.
#The result in the function will become the value of each element in the resultant RDD.

#split() method splits a string into a list. Here, the separator is whitespace.

rdd2 = rdd.map(lambda x: x.split(" "))
for element in rdd2.collect():
    print(element)
print (rdd2.collect())


# In[4]:


#Flatmap - flatMap() is the transformation that takes a function and applies the function to each elements of the RDD as in the map() function.
#The DIFFERENCE is that flatMap will return multiple values for each element in the source RDD. 

rdd3=rdd.flatMap(lambda x: x.split(" "))
for element in rdd3.collect():
    print(element)
print(rdd3.collect())


# In[5]:


#Using a function to split the words of each element and return multiple values for each element if their word length is more than 2 letters
def tokenize(x):
    tokens = x.split()
    newlist = []
    for words in tokens:
        if(len(words) > 2):
            newlist.append(words)
    return newlist
    
rdd4 = rdd.flatMap(lambda x: tokenize(x))
print("rdd4 = ", rdd4)
print("rdd4.collect() = ", rdd4.collect())


# In[ ]:




