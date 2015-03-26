import sys
sys.path.append("mongo-java-driver-3.0.0-rc1.jar")

from com.mongodb import *

m = MongoClient("localhost")
db = m.getDB("test")
coll = db.getCollection("accounts")
a = coll.findOne()
print a
