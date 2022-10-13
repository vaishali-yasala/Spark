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
 mapPartitionsWithIndex( ) is similar to mapPartitions, but also provides func with an integer value representing the index of the partition. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.pdf)

 6. sample() Transformation -
 Sample a function fraction of the data, with or without replacement, using a given random number generator seed. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.pdf)

 7. union() Transformation - 
 Return a new dataset that contains the union of the elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.pdf)

 8. intersection( ) Transformation -
 Return a new dataset that contains the intersection of elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.pdf)

 9. distinct( ) Transformation -
 Return a new dataset that contains the distinct elements of the source dataset.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.pdf)

10. groupByKey( ) Transformation -
When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable <V>) pairs. <br>
Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance.<br>
Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numPartitions argument to set a different number of tasks.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.pdf)
