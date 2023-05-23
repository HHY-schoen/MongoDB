
import pymongo

client = pymongo.MongoClient(['localhost:27017', 'localhost:27018'])
db = client.test

num = 480000
data = [13, 2, 5, 7, 7, 9, 9, 13, 14, 17, 13, 2, 9, 10]
for n in data:
    db.d.insert_one(
        {
            'lv': None,
            'n': n,
            'junk': '_' * num
        }
    )