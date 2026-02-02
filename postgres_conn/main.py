import os
from dotenv import load_dotenv

import psycopg2

load_dotenv()

insert_cmd = """
    INSERT INTO number VALUES (3, 11, 'yeehaw');
"""

query_cmd = """select * from number"""

if __name__ == '__main__':
    with psycopg2.connect(os.getenv("DSN")) as conn:
        cur = conn.cursor()

        # cur.execute(insert_cmd)
        cur.execute(query_cmd)

        for row in cur.fetchall():
            print(row)

        conn.commit()
