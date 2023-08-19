import requests
import csv
import re
import logging

logger = logging.Logger('catch_all')
def regex(var1,var2,strV):
    regexVar = re.search(f"{var1}(.+?){var2}",strV).group(1)
    return regexVar

def main():
    Paths = []
    with open("D:/DEcourse/Project_4/version_2/categories_v1.csv", 'r',encoding="utf-8") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            url = row[7]
            Paths.append(url)
    Pro_id(Paths)        

def Pro_id(Paths):
    count_len = len(Paths)
    count_Path = 0
    for Path in Paths:
        category = re.findall(r'\d+', Path)
        if Path == "https://tiki.vn/tikingon/ngon/c44792":
            urlKey = regex("https://tiki.vn/","/c",Path).replace("/","-")
        else:
            urlKey = regex("https://tiki.vn/","/c",Path)
        rows = []
        csv_name = urlKey
        print(csv_name)
        
        for page in range(1,21,1):
            print(page)
            count=0
            try:
                header={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                    'Accept': 'application/json, text/plain, */*',
                    'Accept-Language':'en-US,en;q=0.9,vi-VN;q=0.8,vi;q=0.7',
                    'Referer': Path,
                    'X-Access-Token':'eyJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMDI0MDE4OCIsImlhdCI6MTY4MzgxOTMyMywiZXhwIjoxNjgzOTA1NzIzLCJpc3MiOiJodHRwczovL3Rpa2kudm4iLCJjdXN0b21lcl9pZCI6IjEwMjQwMTg4IiwiZW1haWwiOiJhbmhfbGFfbWF0dHJvaV9jdWFlbV8yNTJAeWFob28uY29tIiwiY2xpZW50X2lkIjoidGlraS1zc28iLCJuYW1lIjoiMTAyNDAxODgiLCJzY29wZSI6InNzbyJ9.lcNTsI4fIcgs2sVA3Dmbx7L97JsNyv4jljtNOujOpdRrmTJlYTsZ5YmCz7PXfC3B9hEQEMAZNPKBBref09Sw5NS7N1sSRpKWOj4AnsBduzRsPIAFoRIC87u3mu7OhgNRsasdI2zNG2oUaAgh57KQKTGUhZ2rQ8ZX-STVncsVQLy2ZLUuR2AuMEAwxCT4pF46VjEOImx6GhgAlCplj-36HcGdcCkG-9wJDbchdGxgYcdzs3E1uh7rUzoskvz2Kko9nyDAPOdqzNFTQNK4ZkaRK5ptlORdUbw0HzHzFxKv5xCIYnEdCVz0JCQXkEj9IrcaENN-KvmS5zSuLPamyx3KdtuqyzIRnHcJQlkAdgh6-AM38Cjgb1PbpZR0WsVCC8P6XkwM3yj2qnTGGeigfGgAfdpsu2Gy0YSIavQDKg1uj5KcFdcisRUL-xPpJT0v-NHEqu45Owgmlt2xwajNQF42t6YseOupRyN1-34R1gKPulu-dBGvUNxI16AYLiWZ572Y_yrztalBYtXvo3k9wS0iMOuXeery7ejBF22YKuw2iV0OEtmM9WnorBoV434ho47MBpXsOASzz9ySBE17G_N3jQuDlu-JuNiVNRf52JR1wDQkWNctu5eFNBB5MsDXffq5JBg37UeGLjMPRkUcfavPlq1GagI8BiXmDvmnbQCn6No'

                }
                param ={
                    "limit": "100",
                    "include": "advertisement",
                    "aggregations": 2,
                    "trackity_id": "841a9807-eae4-7cb4-9ef7-deea31792b2f",
                    "category": category,
                    "page": page,
                    "urlKey": urlKey
                }
                url = "https://tiki.vn/api/personalish/v1/blocks/listings?"
                response = requests.get(url,headers=header,params=param)
                if response.status_code == 200:
                    for i in range(0,100):
                        try:
                            product_id = response.json().get('data')[i].get('id')
                            print(product_id)
                            rows.append(product_id)
                            count+=1
                            print(count)
                        except IndexError:
                            raise

            except:
                continue
        print(count_Path)
        print(f"before set: {len(rows)}")
        row_set = set(rows)
        print(f"after set: {len(row_set)}")
        with open(f"D:/DEcourse/Project_4/version_2/ProductID1/{count_len}-{csv_name}.txt", 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row_set)
            print(f"Total:{count} ids")
        count_len-=1

if __name__ == "__main__":
    main()