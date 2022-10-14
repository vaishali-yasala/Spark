# Spark

In this Repository, we explore RDD Transformations and Actions. All these examples are coded in Python language and tested on Jupyter Notebook. 
Files ending with .py contains the Python language code.
Files ending with .pdf contains the input and output result at various steps.

## Table Of Contents
 1.[<b>map Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-map)-
 map(func) is the transformation that takes a function and applies the function to each element of the input RDD. The result in the function will become the value of each element in the resultant RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map/rdd-map.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-map/rdd-map.pdf)

 2. [<b>filter Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-filter)-
filter(func) is the transformation that returns a new RDD with only the elements that ppasses the filter condition.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter/rdd-filter.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-filter/rdd-filter.pdf)

 3. [<b>flatMap(func) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-flatMap) -
 flatMap( ) is the transformation that takes a function and applies the function to each element of the RDD as in map( ) function. The difference is that flatMap will return multiple values for each element in the source RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap/rdd-flatMap.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-flatMap/rdd-flatMap.pdf)

 4. [<b> mapPartitions(func) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-mapPartitions) -
 Similar to map, but runs separately on each partition of the RDD.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions/rdd-mapPartitions.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitions/rdd-mapPartitions.pdf)

 5. [<b> mapPartitionsWithIndex(func) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-mapPartitionsWithIndex)-
 mapPartitionsWithIndex( ) is similar to mapPartitions, but also provides func with an integer value representing the index of the partition. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex/rdd-mapPartitionsWithIndex.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-mapPartitionsWithIndex/rdd-mapPartitionsWithIndex.pdf)

 6. [<b>sample(withReplacement, fraction, seed) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-sample)-
 Sample a function fraction of the data, with or without replacement, using a given random number generator seed. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample/rdd-sample.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sample/rdd-sample.pdf)

 7. [<b>union(otherDataset) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-union)- 
 Return a new dataset that contains the union of the elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union/rdd-union.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-union/rdd-union.pdf)

 8. [<b>intersection(otherDataset) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-intersection) -
 Return a new dataset that contains the intersection of elements in the source dataset and the argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection/rdd-intersection.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-intersection/rdd-intersection.pdf)

 9. [<b>distinct([numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-distinct)-
 Return a new dataset that contains the distinct elements of the source dataset.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct/rdd-distinct.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-distinct/rdd-distinct.pdf)

10. [<b>groupByKey([numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-groupByKey)-
When called on a dataset of (K, V) pairs, returns a dataset of (K, Iterable <V>) pairs. <br>
Note: If you are grouping in order to perform an aggregation (such as a sum or average) over each key, using reduceByKey or aggregateByKey will yield much better performance.<br>
Note: By default, the level of parallelism in the output depends on the number of partitions of the parent RDD. You can pass an optional numPartitions argument to set a different number of tasks.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey/rdd-groupByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-groupByKey/rdd-groupByKey.pdf)

 11. [<b>reduceByKey(func, [numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-reduceByKey)-
 When called on a dataset of (K, V) pairs, returns a dataset of (K, V) pairs where the values for each key are aggregated using the given reduce function <i>func</i>, which must be of type (V,V) => V. Like in groupByKey, the number of reduce tasks is configurable through an optional second argument. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey/rdd-reduceByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-reduceByKey/rdd-reduceByKey.pdf)

12. [<b>aggregateByKey(zeroValue)(seqOp, combOp, [numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-aggregateByKey)- 
When called on a dataset of (K,V) pairs, returns a dataset of (K,U) pairs where the values for each key are aggregated using the given combine functions and a neutral "zero" value. Allows an aggregate value type that is different than the input value type, while avoiding the unnecesary allocations. Like in <i>groupByKey</i>, the number of reduce tasks is configurable through an optional second argument.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey/rdd-aggregateByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-aggregateByKey/rdd-aggregateByKey.pdf)

 13. [<b>sortByKey([ascending], [numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-sortByKey)- 
 When called on a dataset of (K, V) pairs whete K implements Ordered, returns a datset of (K, V) pairs stored by keys in ascending or descending order, as specified in the boolean <i>ascending</i> argument.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sortByKey/rdd-sortByKey.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-sortByKey/rdd-sortByKey.pdf)

 14. [<b>join(otherDataset, [numPartitions]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-join)- 
 When called on datasets of type (K, V) and (K,W), returns a dataset of (K, (V, W)) pairs with pairs of all elements for each key. Outer joins are supported through <i>leftOuterJoin, rightOuterJoin </i>, and <i>fullOuterJoin</i>.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-join/rdd-join.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-join/rdd-join.pdf)

 15. [<b> cogroup(otherDataset, [numPartitions]) Transformation</b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-cogroup) - 
 When called on datasets of type (K, V) and (K, W), returns a dataset of (K, (Iterable< V >, Iterable< W >)) tuples. This operation is also called <i>groupWith</i>.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-cogroup/rdd-cogroup.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-cogroup/rdd-cogroup.pdf)

 16. [<b>cartesian(otherDataset) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-cartesian) - 
 When called on datasets of type T and U, returns a dataset of (T, U) pairs (all pairs of elements).
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-cartesian/rdd-cartesian.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-cartesian/rdd-cartesian.pdf)

 17. [<b>pipe(command, [envVars]) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-pipe) -
 Pipe each partition of the RDD through a shell command, e.g. a Perl or bash script. RDD elements are written to the process's stdin and lines output to its stdout are returned as an RDD of strings.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-pipe/rdd-pipe.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-pipe/rdd-pipe.pdf)
 - [Shell Script Command](https://github.com/vaishali-yasala/Spark/tree/main/Exercise_Dependencies/pipe.sh)

 18. [<b>coalesce(numPartitions) Transformation </b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-coalesce) -
 Decrease the number of partitions in the RDD to numPartitions. Useful for running operations more efficiently after filering down a large dataset.
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-coalesce_rdd-repartition/rdd-coalesce.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-coalesce_rdd-repartition/rdd-coalesce.pdf)

 19. [<b> repartition(numPartitions) Transformation</b>](https://github.com/vaishali-yasala/Spark/tree/main/rdd-repartition) - 
 Reshuffle the data in the RDD randomly to create either more or fewer partitions and balance it acroos them. This always shuffles all data over the network. 
 - [Code](https://github.com/vaishali-yasala/Spark/blob/main/rdd-coalesce_rdd-repartition/rdd-coalesce.py)
 - [Output](https://github.com/vaishali-yasala/Spark/blob/main/rdd-coalesce_rdd-repartition/rdd-coalesce.pdf)
 
