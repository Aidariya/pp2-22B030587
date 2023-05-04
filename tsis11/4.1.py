import psycopg2
from psycopg2 import Error
l, o = int(input()), int(input())
try:
    conn = psycopg2.connect(
        host = 'localhost',
        database = 'postgres',
        user = 'postgres',
        password = 'aidariya2005'
        )

    cursor = conn.cursor()
    # хранимая процедура
    cursor.callproc('pagi2', (l, o,))
    result = cursor.fetchall()
    for i in result:
        print(*i)

except (Exception, Error) as error:
    print("ERROR", error)
finally:
    if conn:
        cursor.close()
        conn.close()