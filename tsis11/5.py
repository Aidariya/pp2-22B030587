#процедурa удаления данных из таблиц по имени пользователя или телефону
import psycopg2
from psycopg2 import Error

def create_func(query):
    try:
        conn = psycopg2.connect(
            host = 'localhost',
            database = 'postgres',
            user = 'postgres',
            password = 'aidariya2005'
            )
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except (Exception, Error) as error:
        print("Error during the work with PostgreSQL", error)
    finally:
        if conn:
            cursor.close()
            conn.close()
            print('Procedure is created')

postgresql_proc = """
CREATE OR REPLACE PROCEDURE delete_user(n_name varchar) 
AS $$ 
BEGIN
    DELETE FROM phonebook WHERE name = n_name;
END;
$$ 
LANGUAGE plpgsql
"""
create_func(postgresql_proc)