# Spark

In this Repository, we explore RDD Transformations and Actions. All these examples are coded in Python language and tested on Jupyter Notebook. 
Files ending with .py contains the Python language code.
Files ending with .pdf contains the input and output result at various steps.

## Table Of Contents
 1. RDD - map Transformation -
 map( ) is the transformation that takes a function and applies the function to each element of the input RDD. The result in the function will become the value of each element in the resultant RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.pdf)

 2. RDD - filter Transformation -
filter( ) is the transformation that returns a new RDD with only the elements that ppasses the filter condition.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.pdf)

 3. RDD - flatMap Transformation -
 flatMap( ) is the transformation that takes a function and applies the function to each element of the RDD as in map( ) function. The difference is that flatMap will return multiple values for each element in the source RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.pdf)

 4. RDD mapPartitions Transformation -
 Similar to map, but runs separately on each partition of the RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.pdf)

 5. mapPartitionsWithIndex(func) Transformation -
 mapPartitionsWithIndex( ) is similar to mapPartitions, but also provides func with an integer value representing the index of the partition, so func must be of type (Int, Iterator <T>) => Iterator<U> when running on an RDD of type T. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.pdf)

 6. sample() Transformation -
 Sample a function fraction of the data, with or without replacement, using a given random number generator seed. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.pdf)