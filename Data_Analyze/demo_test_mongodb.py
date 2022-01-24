import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
  print("数据库已存在！")