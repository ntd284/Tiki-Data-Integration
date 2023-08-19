import pymongo

# Assuming you have a MongoDB connection set up
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Tiki2"]
collections = mydb.list_collection_names()
count=0
for collection in collections:
    col_1= mydb[collection]
    # Define the aggregation pipeline
    Duplicate = [
    { "$group": { "_id": "_id", "count": { "$sum": 1 } } },
    { "$match": { "count": { "$gt": 1 } } }
    ]
    document_count = col_1.count_documents({})
    result = list(col_1.aggregate(Duplicate))
    print(f"{col_1}: {document_count}" )

    # Print the result
    for doc in result:
        count+=1
        print(f"{count}:{doc}: {document_count}")
        # Delte_dup = col_1.delete_many({"id":doc["_id"]})
        # print(Delte_dup.deleted_count)




