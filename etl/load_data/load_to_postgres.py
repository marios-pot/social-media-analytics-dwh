import json 
import psycopg2 
from datetime import datetime

def load_instagram_to_db():
    with open("data/raw_instagram.json","r") as f:
        data=json.load(f)

    conn=psycopg2.connect("dbname=postgres user=postgres paswword=test1234")
    cursor=conn.cursor() 

    for item in data['data']:
        metric = item['name']
        for val in item['values']:
            date=datetime.strptime(val['end_time'],"%Y-%m-%dT%H:%M:%S%z").date()
            value=val['value']
            cursor.execute("""
                INSERT INTO smanalytics.daily_metrics (account_id,date,enegagement_rate)
                VALUES (%s,%s,%s)
                ON CONFLICT (account_id,date) DO NOTHING
            """, (1,date,value))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    load_instagram_to_db()
                                                                                                   