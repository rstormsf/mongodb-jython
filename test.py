import sys
sys.path.append("mongo-java-driver-3.0.0-rc1.jar")

from com.mongodb import *
from com.mongodb.client.model import *
from org.bson import *

m = MongoClient("localhost")
db = m.getDatabase("test")
coll = db.getCollection("dub_accs")
print coll.count()
user = coll.find(Filters.and(Filters.exists("ImageUrl"), Filters.exists("snapshot", False))).first()
email = user["EmailAddress"]
coll.updateOne(Filters.eq("EmailAddress", email), Document("$set", Document("snapshot", True)))

