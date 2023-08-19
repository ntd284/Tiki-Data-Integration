import pymongo
import json
from bson import json_util
from bson.json_util import dumps
from bs4 import BeautifulSoup
import logging
import csv
import time
from datetime import datetime
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor


def regex(var1,var2,strV):
    regexVar = re.search(f"{var1}(.+?){var2}",strV).group(1)
    return regexVar
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Tiki1"]
collections = mydb.list_collection_names()
jsonf = []
count = len(collections)
count_ = 0

def find_duplicates(lst):
    return list({x for x in lst if lst.count(x) > 1})

if __name__ == "__main__":
 
    start_time = time.time()
    logger = logging.Logger('catch_all')
    path_txt = "D:/DEcourse/Project_4/version_2/ProductID/"
    file_txt = []
    limit_txt = []
    for (root, dirs, file) in os.walk(path_txt):
        for f in file:
            if '.txt' in f:
                file_txt.append(f)
    for i in range(200,300):
        mycol_ = file_txt[i]
        limit_txt.append(mycol_)
    count = 0
    for sample in limit_txt:
        print(sample)
        with open(f'D:/DEcourse/Project_4/version_2/ProductID/{sample}', 'r', encoding='UTF8') as ids: 
            product_ids = ids.read().replace(",","\n").splitlines()
            print(sample)
            duplicates = find_duplicates(product_ids)
            print(duplicates)
            print(f"len product_id before: {len(product_ids)}")
            product_lst_id = list(set(product_ids))
            print(f"len product_id after: {len(product_lst_id)}")
            with open(f"D:/DEcourse/Project_4/version_2/Dup_solved/{sample}", 'w', encoding='UTF8') as f:
                writer = csv.writer(f)
                writer.writerow(product_lst_id)
                count+=1
                print(f"{count}: {sample}")




                            