import requests
import pymongo
import json
from bson import json_util
from bson.json_util import dumps
from bs4 import BeautifulSoup
import logging
import time
from datetime import datetime
import os
import re
import time


def regex(var1,var2,strV):
    regexVar = re.search(f"{var1}(.+?){var2}",strV).group(1)
    return regexVar
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient("mongodb+srv://nguyentuanduongtest:Nokia55301@cluster0.9igbpyj.mongodb.net/")

mydb = myclient["Tiki1"]
header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language':'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
        'X-Access-Token':'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDI0MDE4OCIsImlhdCI6MTY4MzgxOTMyMywiZXhwIjoxNjgzOTA1NzIzLCJpc3MiOiJodHRwczovL3Rpa2kudm4iLCJjdXN0b21lcl9pZCI6IjEwMjQwMTg4IiwiZW1haWwiOiJhbmhfbGFfbWF0dHJvaV9jdWFlbV8yNTJAeWFob28uY29tIiwiY2xpZW50X2lkIjoidGlraS1zc28iLCJuYW1lIjoiMTAyNDAxODgiLCJzY29wZSI6InNzbyJ9.lcNTsI4fIcgs2sVA3Dmbx7L97JsNyv4jljtNOujOpdRrmTJlYTsZ5YmCz7PXfC3B9hEQEMAZNPKBBref09Sw5NS7N1sSRpKWOj4AnsBduzRsPIAFoRIC87u3mu7OhgNRsasdI2zNG2oUaAgh57KQKTGUhZ2rQ8ZX-STVncsVQLy2ZLUuR2AuMEAwxCT4pF46VjEOImx6GhgAlCplj-36HcGdcCkG-9wJDbchdGxgYcdzs3E1uh7rUzoskvz2Kko9nyDAPOdqzNFTQNK4ZkaRK5ptlORdUbw0HzHzFxKv5xCIYnEdCVz0JCQXkEj9IrcaENN-KvmS5zSuLPamyx3KdtuqyzIRnHcJQlkAdgh6-AM38Cjgb1PbpZR0WsVCC8P6XkwM3yj2qnTGGeigfGgAfdpsu2Gy0YSIavQDKg1uj5KcFdcisRUL-xPpJT0v-NHEqu45Owgmlt2xwajNQF42t6YseOupRyN1-34R1gKPulu-dBGvUNxI16AYLiWZ572Y_yrztalBYtXvo3k9wS0iMOuXeery7ejBF22YKuw2iV0OEtmM9WnorBoV434ho47MBpXsOASzz9ySBE17G_N3jQuDlu-JuNiVNRf52JR1wDQkWNctu5eFNBB5MsDXffq5JBg37UeGLjMPRkUcfavPlq1GagI8BiXmDvmnbQCn6No'
}
param ={
"platform": "web",
"spid": "118895419"
}
collections = mydb.list_collection_names()
jsonf = []
count = len(collections)
count_ = 0

def find_duplicates(lst):
    return list({x for x in lst if lst.count(x) > 1})

def savetomonodb(db_name,tiki_info,product_id,name):
    mycol = mydb[f"{db_name}"]
    x = mycol.insert_one(tiki_info)
    
    print(f"{product_id}: {name}  ")

if __name__ == "__main__":
 
    start_time = time.time()
    logger = logging.Logger('catch_all')
    path_txt = "D:/DEcourse/Project_4/version_2/Dup_solved/"
    file_txt = []
    limit_txt = []
    for (root, dirs, file) in os.walk(path_txt):
        for f in file:
            if '.txt' in f:
                file_txt.append(f)
    for i in range(0,200):
        mycol_ = file_txt[i]
        limit_txt.append(mycol_)
    ID_rows=[]
    count_total = 0
    count_db = 0
    for collection in collections:
        str_col = collection.replace("_","-")
        for txt in limit_txt:
            txt_filter = regex("^[0-9]+-",".txt",txt)
            if txt_filter == str_col:
                with open(f'D:/DEcourse/Project_4/version_2/Dup_solved/{txt}', 'r', encoding='UTF8') as ids: 
                    product_ids = ids.read().replace(",","\n").splitlines()
                    mydb_col = txt_filter.replace("-","_")
                    col_1= mydb[mydb_col]
                    doc_count = col_1.count_documents({})
                    count_len = len(product_ids)
                    count = 0
                    count_db+=1
                    print(txt)
                    print(col_1)
                    print(f"{count_db}: mongodb/txt:({doc_count}/{count_len})")
                    Remaining = count_len - doc_count
                    try:
                        for x in col_1.find({},{}):
                            col_json = json.loads(json_util.dumps(x))
                            ID_rows.append(col_json['id'])
                    except Exception as e:
                        continue  
                    for product_id in product_ids:
                        if product_id not in str(ID_rows):
                            print(product_id)
                            max_retries = 100
                            retry_delay = 5  # seconds
                            for attempt in range(max_retries):
                                try:
                                    url = f"https://tiki.vn/api/v2/products/{product_id}"
                                    response = requests.get(url,headers=header,params=param)
                                    if response.status_code == 200:
                                        tiki_info = response.json()
                                        name = tiki_info.get("name")
                                        print("try_1")
                                        count+=1    
                                        count_total+=1            
                                        print(txt)
                                        print(col_1)        
                                        savetomonodb(mydb_col,tiki_info,product_id,name)
                                        Remaining = count_len - doc_count
                                        print(f"{count_total}:Remaining: {count}/ {Remaining} ({doc_count}/{count_len})")
                                        break
                                    else:
                                        print(f"max_retries at else {product_id}: {max_retries}")
                                        print(f"{response.status_code} - retry_delay: {retry_delay} ")
                                        max_retries-=1
                                        retry_delay+=1  
                                except Exception as e:
                                    print(f"max_retries at except {product_id}: {max_retries}")
                                    print(f"{response.status_code} - retry_delay: {retry_delay} ")
                                    time.sleep(retry_delay)
                                    max_retries-=1
                                    retry_delay+=1        
                                    if retry_delay < 80:
                                        logger.error(e, exc_info=True)
elapsed = time.time() - start_time
print(f"Elapsed: {elapsed:.2f}s")  