from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.schema import MetaData
import time
import csv

start_time = time.time()
db_connection_str = 'mysql+mysqlconnector://root:882489@localhost:3306/tiki_db'
db_connection = create_engine(db_connection_str)
meta = MetaData()
meta.reflect(bind=db_connection)
df = pd.read_sql("SELECT id,description FROM tiki_info WHERE description LIKE '%Thành phần:%' OR description LIKE '%Thành phần/Ingredient%' OR description LIKE '%Thành phần/ Ingredient%;'", con=db_connection)

csv_file_path = 'Component.csv'
df.to_csv(csv_file_path, index=False)

elapsed = time.time() - start_time
print(f"Elapsed: {elapsed:.2f}s")  
