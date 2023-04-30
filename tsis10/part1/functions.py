import psycopg2
from config import config

params = config()

def create_tables():
    create_table_sql = """
        CREATE TABLE phonebook(
            phone_id SERIAL NOT NULL,
            name VARCHAR(40) NOT NULL,
            surname VARCHAR(40) NOT NULL,
            address VARCHAR(20) NOT NULL,
            phone_number INTEGER NOT NULL
        )
    """

    connect = psycopg2.connect(**params)
    
    with connect.cursor() as cursor:
        cursor.execute(create_table_sql)
    connect.commit()
    print("Successfully created a table")
    connect.close()

#create_tables()

def insert_element_console():
    insert_element_sql = """
        INSERT INTO phonebook(name, surname, address, phone_number)
        VALUES(%s, %s, %s, %s)
    """

    connect2 = psycopg2.connect(**params)

    with connect2.cursor() as cursor:
        cursor.execute(insert_element_console)
    connect2.commit()
    print("Inserted element from console")
    connect2.close()



