from sqlalchemy import create_engine, Column, Integer, String, JSON,Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import pymongo
from bson.json_util import dumps
from bson import json_util
from bs4 import BeautifulSoup
import logging

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb1 = myclient["Tiki1"]
    mydb2 = myclient["Tiki2"]
    collections = mydb1.list_collection_names()
    count_collection = len(collections)
    logger = logging.Logger('catch_all')

    for count,collection in enumerate (collections):
        col_1= mydb1[collection]
        col_2= mydb2["Tiki_info"]
        doc_count = col_1.count_documents({})

        print(f"{count}/{len(collections)}: {collection} - {doc_count} values ")
        for x in col_1.find({},{}):   
            tiki_info = json.loads(json_util.dumps(x).replace("$",""))
            tiki_info['category'] = collection.replace("_"," ")
            try:
                insert_db = col_2.insert_one(tiki_info)
                print(f"{count}/{doc_count}/{len(collections)}: {collection} ")
            except Exception as e:
                logger.error(e, exc_info=True)

                continue
if __name__== "__main__":
    main()