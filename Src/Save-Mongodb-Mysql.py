from sqlalchemy import create_engine, Column, Integer, String, JSON,Float, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import pymongo
from bson.json_util import dumps
from bson import json_util
from bs4 import BeautifulSoup

def main():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["Tiki2"]
    collections = mydb.list_collection_names()
    count_collection = len(collections)
    for count,collection in enumerate (collections):
        col_1= mydb[collection]
        doc_count = col_1.count_documents({})
        print(f"{count}/{len(collections)}: {collection} - {doc_count} values ")
        Base = declarative_base()
        class Prod_info(Base):
            __tablename__ = f'{collection}'
            id = Column(Integer, primary_key=True)
            name = Column(String(255))
            short_description = Column(Text)
            origin = Column(String(255))
            description = Column(Text)
            short_url = Column(String(255))
            rating_average = Column(Float)
            all_time_quantity_sold = Column(Integer)
            price = Column(Float)
            category = Column(String(255))
        engine = create_engine('mysql+mysqlconnector://root:882489@localhost:3306/tiki_db')
        Base.metadata.create_all(engine)
        for x in col_1.find({},{"id":1,"name":1,"price":1,"short_description":1,"category":1,"description":1,"short_url":1,"specifications":1,"rating_average":1,"all_time_quantity_sold":1}):
            try:
                col_json = json.loads(json_util.dumps(x))
                col_json['_id']=str(col_json['_id'])
                specss = col_json["specifications"]
                count=0
                descriptions = BeautifulSoup(col_json['description'])
                col_json['description'] = descriptions.get_text()
                col_json['short_description'] = col_json['short_description'].replace("\n","")
                if "code': 'origin" in str(specss):
                    for specs in specss:
                        attribute = specs['attributes']
                        for spec in attribute:
                            if spec['code'] == "origin":
                                col_json["specifications"]=spec['value']
                                Pro_col_1 = Prod_info(
                                    id = col_json.get('id', 0),
                                    name = col_json.get('name', 'Null'),
                                    short_description = col_json.get('short_description', 'Null'),
                                    description = col_json.get('description', 'Null'),
                                    origin = col_json.get('specifications', 'Null'),
                                    short_url = col_json.get('short_url', 'Null'),
                                    rating_average = col_json.get('rating_average', 0),
                                    all_time_quantity_sold = col_json.get('all_time_quantity_sold', 0),
                                    price = col_json.get('price', 0) ,  
                                    category =  col_json.get('category', 0) 
                                )
                                Session = sessionmaker(bind=engine)
                                session = Session()
                                session.add(Pro_col_1)
                                session.commit()
                                count-=1
            except:
                continue
    count_collection-=1
if __name__== "__main__":
    main()