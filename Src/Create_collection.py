import requests
import csv
import re
import json
import pymongo
import time
from datetime import datetime
import os
import logging

import time
from concurrent.futures import ThreadPoolExecutor

logger = logging.Logger('catch_all')

def regex(var1,var2,strV):
    regexVar = re.search(f"{var1}(.+?){var2}",strV).group(1)
    return regexVar

def savetomonodb(db_name,tiki_info,product_id,name):
    mycol = mydb[f"{db_name}"]
    x = mycol.insert_one(tiki_info)
    print(f"{product_id}: {name}  ")  

if __name__ == "__main__":
    start_time = time.time()
    now = datetime.now()
    time_ = now.strftime("%Hh%Mm%Ss")
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
    path_txt = "D:/DEcourse/Project_4/version_2/Dup_solved/"
    # path_txt = "C:/Users/Administrator/Desktop/dist/Dup_solved/"


    file_txt = []
    limit_txt = []
    for (root, dirs, file) in os.walk(path_txt):
        for f in file:
            if '.txt' in f:
                file_txt.append(f)
    
    for i in range(0,500):
        mycol_ = file_txt[i]
        limit_txt.append(mycol_)
    executor = ThreadPoolExecutor(2)
    for i in range (len(limit_txt)):
        mycol_ = limit_txt[i]
        # future = executor.submit(Pro_csv,(mycol_))
        print(mycol_)
        try: 
            db_name = regex("^[0-9]+-","$",mycol_).replace(".txt","").replace("-","_")
            mycol = mydb.create_collection(db_name)
            elapsed = time.time() - start_time
            print(f"Elapsed: {elapsed:.2f}s")   
        except:
            continue  

#giữ lại 50,100 xử lý sau.