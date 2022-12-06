# Task 3
import psycopg2
def connect_to_db():
    conn = psycopg2.connect(
        host="localhost",
        database="assessmentdb",
        user="postgres",
        password="xxxxx")
    return conn



def list(conn):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT*FROM contacts;")
    rows = cur.fetchall()
    conn.commit()
    cur.close()
    return rows

def insert(conn, first_name, last_name):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO contacts (first_name,last_name) VALUES ('{first_name}','{last_name}')")
    conn.commit()
    cur.close()

def delete(conn, first_name):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM contacts WHERE first_name = '{first_name}'")
    conn.commit()
    cur.close()

still_nerdy = True

while still_nerdy:
    commands = input('You can choose from the following commands: LIST, INSERT, DELETE, QUIT ').strip().upper()
    if commands == 'LIST':
        conn = connect_to_db()
        print("The contact list")
        listrows = list(conn)
        for listrow in listrows:
            print(listrow[0], "\t" + listrow[1], "\t" + listrow[2])
        print("\n")

    elif commands == 'INSERT':
        conn = connect_to_db()
        first_name = input("Your first name: ").strip().capitalize()
        last_name = input("Your last name: ").strip().capitalize()
        insert(conn,first_name,last_name)


    elif commands == 'DELETE':
        conn = connect_to_db()
        first_name = input("Your first name: ").strip().capitalize()
        delete(conn,first_name)



    elif commands == 'QUIT':
        print('Have a nice day, dude')
        conn.close()
        still_nerdy = False
    else:
        print('Invalid input, dude. Did you type wrong?')







