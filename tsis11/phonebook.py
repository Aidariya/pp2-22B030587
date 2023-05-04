import psycopg2
import csv

#подключение к бд
conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'aidariya2005'

)

cur = conn.cursor()

#создаю таблицу
cur.execute('''CREATE TABLE IF NOT EXISTS phonebook
               (phone_id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                phone_number TEXT NOT NULL);''')

#добавление через CSV 
def insert_from_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader) #пропуск первой строки
        for row in reader:
            name, phone_number = row
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s);", (name, phone_number))
            conn.commit()
    print("Data inserted from CSV successfully.")

# ввод данных и проверка номера
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("SELECT * FROM phonebook WHERE name = %s;", (name,))
    existing_user = cur.fetchone()
    if existing_user:
        cur.execute("UPDATE phonebook SET phone_number = %s WHERE name = %s;", (phone, name))
        conn.commit()
        print(f"Phone number updated for {name}.")
    else:
        cur.execute("INSERT INTO phonebook (name, phone_number) VALUES (%s, %s);", (name, phone))
        conn.commit()
        print(f"Data inserted for {name} successfully.")

#обновление данных
def update_phonebook():
    inp = input('What would you like to update?\nName or phone?\n')
    if inp == 'name':
        user_input = input("Enter the name to update: ")
        cur.execute("SELECT * FROM phonebook WHERE name=%s;", (user_input,))
        records = cur.fetchall()
    elif inp == 'phone':
        user_input = input("Enter the phone number to update: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number=%s;", (user_input,))
        records = cur.fetchall()
    if len(records) == 0:
        print("No records found.")
        return
    elif len(records) == 1:
        record = records[0]
    else:
        print("Multiple records found. Please select one to update.")
        for i, record in enumerate(records):
            print(f"{i+1}. Name: {record[1]}, Phone: {record[2]}")
        selection = int(input("Enter selection: "))
        record = records[selection-1]
    new_name = input("Enter new name (leave blank to keep existing name): ")
    new_phone = input("Enter new phone number (leave blank to keep existing phone number): ")
    if new_name == "":
        new_name = record[1]
    if new_phone == "":
        new_phone = record[2]
    cur.execute("UPDATE phonebook SET name=%s, phone_number=%s WHERE phone_id=%s;", (new_name, new_phone, record[0]))
    conn.commit()
    print("Record updated successfully.")

#запрос данных
def query_phonebook():
    inp = input('What would you like to query?\nBy name or phone?\n')
    if inp == 'name':
        user_input = input("Enter the name to query: ")
        cur.execute("SELECT * FROM phonebook WHERE name=%s;", (user_input,))
        records = cur.fetchall()
    elif inp == 'phone':
        user_input = input("Enter phone number to query: ")
        cur.execute("SELECT * FROM phonebook WHERE phone_number=%s;", (user_input,))
        records = cur.fetchall()
    if len(records) == 0:
        print("No records found.")
    else:
        for record in records:
            print(f"Name: {record[1]}, Phone: {record[2]}")

#удаление контакта
def delete_from_phonebook():
    inp = input('What would you like to update?\nName or phone?\n')
    if inp == 'name':
        user_input = input("Enter the name to delete: ")
        cur.execute("SELECT * FROM phonebook WHERE name=%s;", (user_input,))
        records = cur.fetchall()
    elif inp == 'phone':
        user_input = int(input("Enter the phone number to delete: "))
        cur.execute("SELECT * FROM phonebook WHERE phone_number=%s;", (user_input,))
        records = cur.fetchall()
    if len(records) == 0:
        print("No records found.")
        return
    elif len(records) == 1:
        record = records[0]
    else:
        print("Multiple records found. Please select one to delete.")
    for i, record in enumerate(records):
        print(f"{i+1}. Name: {record[1]}, Phone: {record[2]}")
    cur.execute("DELETE FROM phonebook WHERE phone_id=%s;", (record[0],))
    conn.commit()
    print("Record deleted successfully.")

#показ всех контактов
def show_all_records():
    cur.execute("SELECT * FROM phonebook;")
    records = cur.fetchall()
    if len(records) == 0:
        print("No records found.")
    else:
        for record in records:
            print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")

#выводит контакты по паттерну
def return_based_on_patterns():
    inp = input('Do you want to search by name or phone?\n')
    if inp == 'name':
        pattern = input('Enter a search pattern: ')
        cur.execute("SELECT * FROM phonebook;")
        records = cur.fetchall()
        matches = []
        for record in records:
            if pattern in record[1]:
                matches.append(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")

        if len(matches) == 0:
            print('No matches found.')
        else:
            for mat in matches:
                print(mat)

    
    elif inp == 'phone':
        pattern = input('Enter a search pattern: ')
        cur.execute("SELECT * FROM phonebook;")
        records = cur.fetchall()
        matches = []
        for record in records:
            if pattern in record[2]:
                matches.append(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")

        if len(matches) == 0:
            print('No matches found.')
        else:
            for mat in matches:
                print(mat)

#ввод юзеров через лист
def insert_users(users):
    incorrect_users = []
    for user in users:
        name, phone = user
        cur.execute("SELECT insert_user(%s, %s)", (name, phone))
        success = cur.fetchone()[0]
        if not success:
            incorrect_users.append(user)

    return incorrect_users


while True:
    print("Choose an option:")
    print("1. Insert data from CSV")
    print("2. Insert data from console")
    print("3. Update data")
    print("4. Query data")
    print("5. Delete data")
    print("6. Show all contacts")
    print("7. Search by pattern")
    print("8. Add data from list")
    print("9. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        filename = input("Enter CSV filename: ")
        insert_from_csv(filename)
    elif choice == '2':
        insert_from_console()
    elif choice == '3':
        update_phonebook()
    elif choice == '4':
        query_phonebook()
    elif choice == '5':
        delete_from_phonebook()
    elif choice == '6':
        show_all_records()
    elif choice == '7':
        return_based_on_patterns()
    elif choice == '8':
        incorrect_users = insert_users(conn, users)
        print(incorrect_users)
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")
    users = [("Alice", "1234567890"), ("Bob", "555-1234"), ("Charlie", "abc1234567")]
