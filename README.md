# Spark

In this Repository, we explore RDD Transformations and Actions. All these examples are coded in Python language and tested on Jupyter Notebook. 
Files ending with .py contains the Python language code.
Files ending with .pdf contains the input and output result at various steps.

## Table Of Contents
 1.<b>map Transformation </b> -
 map(func) is the transformation that takes a function and applies the function to each element of the input RDD. The result in the function will become the value of each element in the resultant RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map.pdf)

 2. <b>filter Transformation </b> -
filter(func) is the transformation that returns a new RDD with only the elements that ppasses the filter condition.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter.pdf)

 3. <b>flatMap(func) Transformation </b> -
 flatMap( ) is the transformation that takes a function and applies the function to each element of the RDD as in map( ) function. The difference is that flatMap will return multiple values for each element in the source RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap.pdf)

 4. <b> mapPartitions(func) Transformation </b> -
 Similar to map, but runs separately on each partition of the RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions.pdf)

 5. <b> mapPartitionsWithIndex(func) Transformation </b>-
 mapPartitionsWithIndex( ) is similar to mapPartitions, but also provides func with an integer value representing the index of the partition. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex.pdf)

 6. <b>sample(withReplacement, fraction, seed) Transformation </b>-
 Sample a function fraction of the data, with or without replacement, using a given random number generator seed. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample.pdf)

 7. <b>union(otherDataset) Transformation </b>- 
 Return a new dataset that contains the union of the elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union.pdf)

 8. <b>intersection(otherDataset) Transformation </b> -
 Return a new dataset that contains the intersection of elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection.pdf)

 9. <b>distinct([numPartitions]) Transformation </b>-
 Return a new dataset that contains the distinct elements of the source dataset.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct.pdf)

10. <b>groupByKey([numPartitions]) Transformation </b>-
When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable <V>) pairs. <br>
Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance.<br>
Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numPartitions argument to set a different number of tasks.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey.pdf)

 11. <b>reduceByKey(func, [numPartitions]) Transformation </b>-
 When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function <i>func</i>, which must be of type (V,V) => V. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey.pdf)

12. <b>aggregateByKey(zeroValue)(seqOp, combOp, [numPartitions]) Transformation </b>- 
When called on a dataset of (K,V) pairs, returns a dataset of (K,U) pairs where the values for each key are aggregated using the given combine functions and a neutral "zero" value. Allows an aggregate value type that is different than the input value type, while avoiding the unnecesary allocations. Like in <i>groupByKey</i>, the number of reduce tasks is configurable through an optional second argument.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey.pdf)

 13. <b>sortByKey([ascending], [numPartitions]) Transformation </b>- 
 When called on a dataset of (K, V) pairs whete K implements Ordered, returns a datset of (K, V) pairs stored by keys in ascending or descending order, as specified in the boolean <i>ascending</i> argument.
  - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sortByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sortByKey.pdf)
