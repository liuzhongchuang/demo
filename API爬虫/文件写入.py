# @Time    : 2018/11/23 0023 09:12
# @Author  : lzc
# @File    : 文件写入.py
# from pyspark.context import SparkContext
# sc = SparkContext(appName='mes')#这个是程序的执行入口SparkContext
# data = [1, 2, 3, 4, 5]
# distData = sc.parallelize(data).collect()
# print(distData)

import pandas as pd
import numpy as np
h = ["表头" , "表头" , "表头"]
list_one = [[1 , 2 , 3],[4,5,6] , [8 , 7 , 9]]
dt = pd.DataFrame (list_one , columns = h)
dt.to_csv ("Ex_info.csv" , encoding = "utf-8")
ex_first = pd.read_csv ("Ex_info.csv" , encoding = "utf-8")
print(ex_first)