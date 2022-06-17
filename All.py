import pandas as pd
import sqlite3

from table_1 import *
from table_2 import *
from table_3 import *


# print(table_1)
# print(table_2)
# print(table_3)
all = pd.concat([table_1, table_2, table_3])
# print(all)

connection = sqlite3.connect("All_data.db")

cursor = connection.cursor()
cursor.execute(f'CREATE TABLE IF NOT EXISTS customers(gender text, firstname text, lastname text, email text, age integer, city text, country text, created_at text, referral text)')
connection.commit()
all.to_sql('customers', connection, if_exists='replace', index = False)
cursor.close()
connection.close()

print(all)
