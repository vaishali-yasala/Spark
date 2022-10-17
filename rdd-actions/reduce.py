from pyspark.sql import SparkSession
from tempfile import NamedTemporaryFile
from fileinput import input
from glob import glob

def f(x):
    print(x*2)

if __name__ == '__main__':
#Create the spark session
    spark = SparkSession \
        .builder \
        .appName("actions") \
        .enableHiveSupport() \
        .getOrCreate()

numbers_list = [1,2,3,4,5]
data=[("A", 10),("B", 20),("C", 30),("B", 40),("B", 50),("F",60)]

data_rdd = spark.sparkContext.parallelize(data)
numbers_rdd = spark.sparkContext.parallelize(numbers_list)

print("Using reduce on numbers_rdd to multiply all its elements =", numbers_rdd.reduce(lambda a,b: a*b))
print("numbers_rdd =", numbers_rdd.collect())
print("length of numbers_rdd =", numbers_rdd.count())

print("data_rdd = ", data_rdd)
print("First element in data_rdd =", (data_rdd.first()))
print("First 3 elements after reducedByKey transformation (sum) is used =",data_rdd.reduceByKey(lambda a,b: a+b).take(3))
print("Random Sample of 5 elements after reducedByKey transformation (sum) with replacement =", \
      data_rdd.reduceByKey(lambda a,b: a+b).takeSample(True,5,1))
print('Random Sample of 5 elements after reducedByKey transformation (sum) without replacement =', \
      data_rdd.reduceByKey(lambda a, b: a + b).takeSample(False, 5, 2))
print("First 6 elements in data_RDD in their natural order =", data_rdd.takeOrdered(6))
print("First 6 elements in numbers_RDD in a custom (descending) order", numbers_rdd.takeOrdered(3,key=lambda x: -x))

#Create a temporary file 'name' to save it as a text file.
tempFile = NamedTemporaryFile(delete=True)
tempFile.close()
print(data_rdd.saveAsTextFile(tempFile.name))
print("data_rdd saved in a text file temporarily= ", ''.join((input(glob(tempFile.name + "/part-0000*")))))

print("Count of elements in data_rdd corresponding to their key =", data_rdd.countByKey().items())

print("Function applied on each element in numbers_rdd to double them =")
print(numbers_rdd.foreach(f))