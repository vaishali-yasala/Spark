#!/usr/bin/env python
# coding: utf-8

# # Filter Transformation

# In[1]:


from pyspark.sql import SparkSession

if __name__ == '__main__':
#Create the spark session
     spark = SparkSession.builder.appName("filter transformation").getOrCreate()


#Dataset
data = spark.sparkContext.range(1,5)

#Show the dataset
print('Dataset')
print(data.collect())
print('-------------')

#Use the map function
rdd = data.map(lambda x: (x, x*x, x*x*x))

#Show the new dataset after the map function
print('New Dataset')
print(rdd.collect())


# In[2]:


columns = ["number","squared","cubed"]

#Create DataFrame 
df = spark.createDataFrame(data = rdd, schema = columns)

#show() displays the contents of the DataFrame in a Table Row and Column Format
df.show()


# In[3]:


#Applying Filter Transformation to result in a new DataFrame when column 1 is not 3

df1 = df.filter(df.number != 3).show(truncate = False)


# In[4]:


#Applying Filter Transformation to result in a new DataFrame when column 1 is not 2 and when column 3 is greater than 3
rdd3 = rdd.filter(lambda x: (x[2] > 5) & (x[0] != 2))
rdd3.toDF(["number","squared","cubed"]).show()

