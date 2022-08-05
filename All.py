import sqlite3
from my_m_and_a import *

def main():
    all = pd.concat([table_1, table_2, table_3])
    connection = sqlite3.connect("All_data.db")
    cursor = connection.cursor()
    cursor.execute(f'CREATE TABLE IF NOT EXISTS customers(gender text, firstname text, lastname text, email text, age integer, city text, country text, created_at text, referral text)')
    connection.commit()
    all.to_sql('customers', connection, if_exists='replace', index = False)
    cursor.close()
    connection.close()
    #
    # print(all)

main()
