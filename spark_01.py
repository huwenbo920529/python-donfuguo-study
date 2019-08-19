# coding:utf-8

from __future__ import print_function
from pyspark import *
import os
import warnings

warnings.filterwarnings("ignore")
print(os.environ['SPARK_HOME'])
print(os.environ['HADOOP_HOME'])

# # logFile = "D:\spark-2.2.0-bin-hadoop2.7\spark-2.2.0-bin-hadoop2.7\README.md"
# # sc = SparkContext("local","Simple App")
# # logData = sc.textFile(logFile).cache()
# # numAs = logData.filter(lambda s: 'a' in s).count()
# # numBs = logData.filter(lambda s: 'b' in s).count()
# # print("Lines with a: %i,lines with b: %i"%(numAs,numBs))
#
sc = SparkContext('local', 'Simple2')
x = sc.parallelize([1, 2, 3])
x1 = sc.parallelize([1, 2, 3, 4], 2)
x2 = sc.parallelize(['A', 'B', 'C', 'A'])
x3 = sc.parallelize([('hello', 3), ('hi', 2), ('haha', 3)])

y1 = x.map(lambda t: (t, t ** 2))
y2 = x.flatMap(lambda t: (t, t ** 2))


def f3(iterator):
    yield sum(iterator)


y3 = x1.mapPartitions(f3)


def f4(partitionIndex, iterator):
    yield (partitionIndex, sum(iterator))


y4 = x1.mapPartitionsWithIndex(f4)

y5 = x1.getNumPartitions()
y6 = x.filter(lambda t: (t % 2 == 1))
y7 = x2.distinct()  # 去重
y8 = x1.union(x2)  # 并集
y9 = x.intersection(x1)  # 交集
y10 = x3.sortByKey()

print('x:', x.collect())
print('x1:', x1.collect())
print('x1.glom():', x1.glom().collect())
print('y1:', y1.collect())
print('y2:', y2.collect())
print('y3:', y3.collect())
print('y4:', y4.collect())
print('y5:', y5)
print('y6:', y6.collect())
print('y7:', y7.collect())
print('y8:', y8.collect())
print('y9:', y9.collect())
print('y10:', y10.collect())

# if __name__ == '__main__':
#     sc = SparkContext("local[8]")
#     rdd = sc.parallelize("hello Pyspark world".split(" "))
#     counts = rdd \
#         .flatMap(lambda line: line) \
#         .map(lambda word: (word, 1)) \
#         .reduceByKey(lambda a, b: a + b) \
#         .foreach(print)
#     sc.stop()
