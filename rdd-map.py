#!/usr/bin/env python
# coding: utf-8


from pyspark.sql import SparkSession

if __name__ == '__main__':
#Create the spark session
     spark = SparkSession.builder.appName("map transformation").getOrCreate()

#Create a dataset
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
     



#New Dataset
data = [(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]

columns = ["number","squared","cubed"]

#Create DataFrame 
df = spark.createDataFrame(data = data, schema = columns)

#show() displays the contents of the DataFrame in a Table Row and Column Format
df.show()



#Double  Column 2  and  Column 3  and  return  a  new  DataFrame
rdd2 = df.rdd.map(lambda x: (x[0], x[1]*2, x[2]*2))
df2 = rdd2.toDF(["number","square_doubled", "cube_doubled"]).show()

#Using a function 
data = [('1','1','1'),
        ('2','4','8'),
        ('3','9','27'),
        ('4','16','64')
       ]
columns = ["number","squared","cubed"]

df = spark.createDataFrame(data = data, schema = columns)
df.show()

#Referring Column Names
rdd2 =df.rdd.map(lambda x:
                 (x["number"],x["squared"],x["cubed"]*2)
                )
def func1(x):
    number = x.number
    square = x.squared
    newNumber = x.cubed*2
    return (number,square, newNumber)

rdd2 = df.rdd.map(lambda x: func1(x)).toDF(["number","sqaured_number","new_number"]).show()






