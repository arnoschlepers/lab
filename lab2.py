#!/usr/bin/env python

from pyspark import SparkContext
sc = SparkContext("local")

file = sc.textFile("gs://qwiklabs-gcp-3741e3bd8b7b2ae8/unstructured/lab2-input.txt")
dataLines = file.map(lambda s: s.split(",")).map(lambda x : (x[0], [x[1]]))
print dataLines.take(100)

databyKey = dataLines.reduceByKey(lambda a, b: a + b)
print databyKey.take(100)

countByKey = databyKey.map(lambda (k,v): (k, len(v)))
print countByKey.take(100)