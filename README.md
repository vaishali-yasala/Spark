# Spark

In this Repository, we explore RDD Transformations and Actions. All these examples are coded in Python language and tested on Jupyter Notebook. 
Files ending with .py contains the Python language code.
Files ending with .pdf contains the input and output result at various steps.

## Table Of Contents
 1. RDD - map Transformation -
 map(func) is the transformation that takes a function and applies the function to each element of the input RDD. The result in the function will become the value of each element in the resultant RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.pdf)

 2. RDD - filter Transformation -
filter(func) is the transformation that returns a new RDD with only the elements that ppasses the filter condition.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.pdf)

 3. flatMap(func) Transformation -
 flatMap( ) is the transformation that takes a function and applies the function to each element of the RDD as in map( ) function. The difference is that flatMap will return multiple values for each element in the source RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.pdf)

 4. RDD mapPartitions(func) Transformation -
 Similar to map, but runs separately on each partition of the RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.pdf)

 5. mapPartitionsWithIndex(func) Transformation -
 mapPartitionsWithIndex( ) is similar to mapPartitions, but also provides func with an integer value representing the index of the partition. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.pdf)

 6. sample(withReplacement, fraction, seed) Transformation -
 Sample a function fraction of the data, with or without replacement, using a given random number generator seed. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.pdf)

 7. union(otherDataset) Transformation - 
 Return a new dataset that contains the union of the elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.pdf)

 8. intersection(otherDataset) Transformation -
 Return a new dataset that contains the intersection of elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.pdf)

 9. distinct([numPartitions]) Transformation -
 Return a new dataset that contains the distinct elements of the source dataset.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.pdf)

10. groupByKey([numPartitions]) Transformation -
When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable <V>) pairs. <br>
Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance.<br>
Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numPartitions argument to set a different number of tasks.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.pdf)

 11. reduceByKey(func, [numPartitions]) Transformation -
 When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function <i>func</i>, which must be of type (V,V) => V. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey.pdf)

12. aggregateByKey(zeroValue)(seqOp, combOp, [numPartitions]) Transformation - 
When called on a dataset of (K,V) pairs, returns a dataset of (K,U) pairs where the values for each key are aggregated using the given combine functions and a neutral "zero" value. Allows an aggregate value type that is different than the input value type, while avoiding the unnecesary allocations. Like in <i>groupByKey</i>, the number of reduce tasks is configurable through an optional second argument.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey.pdf)

 13. sortByKey([ascending], [numPartitions]) Transformation - 
 When called on a dataset of (K, V) pairs whete K implements Ordered, returns a datset of (K, V) pairs stored by keys in ascending or descending order, as specified in the boolean <i>ascending</i> argument.