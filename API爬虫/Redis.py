# @Time    : 2018/12/7 0007 16:18
# @Author  : lzc
# @File    : Redis.py

#!/usr/bin/env python
# -*- coding:utf8 -*-

import redis

# 第一种：单连接,连接一次之后就会断开，这种方式相对比较耗费资源
# rd = redis.Redis(host='127.0.0.1',port=6379,password='123456')
#
# rd.set('name','admin')
#
# print(rd.get('name').decode('utf-8'))

# 第二种：数据库连接池【连接池中有一些连接不会断开，当程序中需要访问数据库时，直接从连接池拿，不需要重新连接数据库】
rd = redis.ConnectionPool(host='127.0.0.1',port=6379)

rds = redis.Redis(connection_pool=rd)

rds.set('password','123456')

print(rds.get('password').decode('utf-8'))


'''
String字符串操作
'''

'''
mset(*args, **kwargs)批量设置值
　　如：
        mset(k1='v1', k2='v2')
        或
        mset({'k1': 'v1', 'k2': 'v2'})
'''
# rds.mset(name = '王小二', name1 = '张三')
# print(rds.get('name1').decode('utf-8'))

rds.mset({'name':'zhangsan','name1':'lisi'})
# print(rds.get('name').decode('utf-8'))
# print(rds.get('name1').decode('utf-8'))

#批量获取值
# print(rds.mget('name','name1'))
names = ['name','name1']
# print(rds.mget(names))

# getset(key,value) 修改key对应的value，返回key值原来对应的值【如果对应的key值不存在，那么新增这条key值对应的数据，并返回None】
print(rds.getset('name3','wangwu'))
print(rds.get('name3'))


'''
setrange(name, offset, value)
    # 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
　　# 参数：
        # offset，字符串的索引，字节（一个汉字三个字节）
        # value，要设置的值
'''
rds.set('name','zhangsan')
rds.setrange('name',1,'zzzzzz')
print('修改',rds.get('name'))


'''
hset(name, key, value)
　　# name对应的hash中设置一个键值对（不存在，则创建；否则，修改）， 注意： 在python中，键值对是dict， 这里的name必须是dict格式。eg：xxx[]、　xxx[k]...     
　　# 参数：
        # name，redis的name
        #key，name对应的hash中的key
        # value，name对应的hash中的value
　　# 注：
        # hsetnx(name, key, value),当name对应的hash中不存在当前key时则创建（相当于添加）
'''
rds.hset('dict_name','a','aa')
rds.hset('dict_name','b','bb')

print(rds.hgetall('dict_name'))
print(rds.hget('dict_name','b'))

# # 获取name对应的hash中键值对的个数
print(rds.hlen('dict_name'))

# 获取name对应的hash中所有的key的值
print(rds.hkeys('dict_name'))

# 检查name对应的hash是否存在当前传入的key
print(rds.hexists('dict_name', 'c'))

'''
list操作
'''
'''
lpush(name,values)
　　# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
　　# 如：
        # r.lpush('oo', 11,22,33)
        # 保存顺序为: 33,22,11
　　# 扩展：
        # rpush(name, values) 表示从右向左操作
'''

# rds.lpush('list_name2',1,2,3)
# rds.rpush('list_name1',1,2,3)

# lrange来取值，后面两个坐标，0表示第一位，-1表示最后一位
print(rds.lrange('list_name2', 0 ,-1))


'''
lpop(name)
　　# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素,也是删除的值
　　# 更多：
        # rpop(name) 表示从右向左操作
'''
print(rds.lpop('list_name2'))
print(rds.lrange('list_name2', 0 ,-1))



'''
Set 集合操作,Set操作，Set集合就是不允许重复的列表。这里包括了一般的集合和有序集合。
'''
rds.sadd('set_name','a','b')

#scard(name) 获取name对应的集合中元素个数
print(rds.scard('set_name'))

# smembers(name) # 获取name对应的集合的所有成员
print(rds.smembers('set_name'))

#sismember(name, value) 检查value是否是name对应的集合的成员
print(rds.sismember('set_name','a'))
print(rds.sismember('set_name','c'))

#srem(name, values)  在name对应的集合中删除某些值
rds.srem('set_name','a')
print(rds.smembers('set_name'))

rds.sadd('set_name3','e','g','d','c','a','c','b')
print(rds.smembers('set_name3'))
