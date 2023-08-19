import pymongo

# Assuming you have a MongoDB connection set up
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient("mongodb+srv://nguyentuanduongtest:Nokia55301@cluster0.9igbpyj.mongodb.net/")
mydb = myclient["Tiki1"]
collections = mydb.list_collection_names()
count=0
document_count = 0
for collection in collections:
    col_1= mydb[collection]
    print(col_1)
    document_count += col_1.count_documents({})
print(document_count)