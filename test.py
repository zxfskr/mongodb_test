#!/usr/bin/env python
# coding: utf-8

from pymongo import MongoClient
from datetime import datetime, timezone, timedelta
from pprint import pprint
import pandas as pd
from bson.son import SON
import json
from bson import ObjectId
from bson.json_util import dumps
import time
import pymongo
import gridfs
import logging
import gc


# ### 1. 创建数据库和表
# 如果不存在，则创建，否则切换到指定位置。
# https://blog.csdn.net/yisun123456/article/details/78591255

client = MongoClient("mongodb://192.168.5.250:27017/", maxPoolSize=1, waitQueueMultiple=2)
# db = client.autoops
db = client['admin']
# db.add_user('root', '123456', roles=[{
#     'role':'userAdminAnyDatabase',
#     'db':'admin',
# }])
# db.authenticate(name="autoops", password="autoops")
# db.createUser(
#   {
#     user: "root",
#     pwd: "123456",
#     roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
#   }
# )
db.authenticate(name="root", password="123456")
# db.command("show user")

db_test = client["test"]["test"]
db_autoops = client["autoops_cycle"]["test"]
db_test2 = client["test2"]["test"]

r = db_test.find()
if r:
    print(list(r))

r = db_autoops.find()
if r:
    print(list(r))

r = db_test2.find()
if r:
    print(list(r))
# db = client["autoops_cycle"]
# db.add_user('autoops', 'autoops', roles=[{
#     'role':'readWrite',
#     'db':'autoops_cycle',
# }])

# db.getUsers()
# r = db["system.users"].find()
# list(r)

# db.authenticate(name="autoops", password="autoops")

# db.dropDatabase()
# collection = db.train_result
# dir(db)
# collection = db['datastream_datas']
# collection.drop()
