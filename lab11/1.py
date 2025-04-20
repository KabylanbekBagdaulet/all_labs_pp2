import psycopg2
import csv
from tabulate import tabulate 

conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="0211bako", port=5432)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (
      user_id SERIAL PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      surname VARCHAR(255) NOT NULL, 
      phone VARCHAR(255) NOT NULL
)
""")

cur.execute("""
CREATE OR REPLACE FUNCTION search_phonebook(pattern TEXT)
RETURNS TABLE(user_id INT, name TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook
    WHERE name ILIKE '%' || pattern || '%' 
       OR surname ILIKE '%' || pattern || '%' 
       OR phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE upsert_user(p_name TEXT, p_surname TEXT, p_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name AND surname = p_surname) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name AND surname = p_surname;
    ELSE
        INSERT INTO phonebook(name, surname, phone) VALUES (p_name, p_surname, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE insert_many_users(names TEXT[], surnames TEXT[], phones TEXT[])
LANGUAGE plpgsql
AS $$
DECLARE
    i INT := 1;
    invalid_data TEXT := '';
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^[0-9+()-]+$' THEN
            CALL upsert_user(names[i], surnames[i], phones[i]);
        ELSE
            invalid_data := invalid_data || FORMAT('Invalid phone for %s %s: %s\n', names[i], surnames[i], phones[i]);
        END IF;
    END LOOP;
    RAISE NOTICE '%', invalid_data;
END;
$$;
""")

cur.execute("""
CREATE OR REPLACE FUNCTION get_page(limit_num INT, offset_num INT)
RETURNS TABLE(user_id INT, name TEXT, surname TEXT, phone TEXT)
AS $$
BEGIN
    RETURN QUERY
    SELECT * FROM phonebook ORDER BY user_id LIMIT limit_num OFFSET offset_num;
END;
$$ LANGUAGE plpgsql;
""")

cur.execute("""
CREATE OR REPLACE PROCEDURE delete_by_name_or_phone(p_name TEXT, p_phone TEXT)
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = p_name OR phone = p_phone;
END;
$$ LANGUAGE plpgsql;
""")

conn.commit()

def insert_data():
    print('Type "csv" or "con": ')
    method = input().lower()
    if method == "con":
        name = input("Name: ")
        surname = input("Surname: ")
        phone = input("Phone: ")
        cur.execute("CALL upsert_user(%s, %s, %s);", (name, surname, phone))
    elif method == "csv":
        filepath = input("Enter a file path: ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            names, surnames, phones = [], [], []
            for row in reader:
                names.append(row[0])
                surnames.append(row[1])
                phones.append(row[2])
            cur.execute("CALL insert_many_users(%s, %s, %s);", (names, surnames, phones))
    conn.commit()

def update_data():
    name = input("Name: ")
    surname = input("Surname: ")
    new_phone = input("New phone: ")
    cur.execute("CALL upsert_user(%s, %s, %s);", (name, surname, new_phone))
    conn.commit()

def delete_data():
    name = input("Name (or leave empty): ")
    phone = input("Phone (or leave empty): ")
    cur.execute("CALL delete_by_name_or_phone(%s, %s);", (name if name else None, phone if phone else None))
    conn.commit()

def query_data():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"]))

def display_data():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))
    cur.execute("SELECT * FROM get_page(%s, %s);", (limit, offset))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Name", "Surname", "Phone"], tablefmt='fancy_grid'))

while True:
    print("""
    1. Type "i" to INSERT data.
    2. Type "u" to UPDATE data.
    3. Type "q" to SEARCH data.
    4. Type "d" to DELETE data.
    5. Type "s" to DISPLAY table.
    6. Type "f" to FINISH.
    """)
    command = input().lower()
    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "f":
        break

cur.close()
conn.close()
