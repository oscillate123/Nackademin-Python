import mysql.connector
import egna_projekt.phonebook_gui as gui
from mysql.connector import errorcode


def sql_connect():
    db = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='ThinkVision.24',
        db='phonebook',
    )
    return db


def add_execute(first, last, phone, email, age):
    my_db = sql_connect()
    cur = my_db.cursor()
    insert_string = "insert into contacts (first_name, last_name, phone_number, email_address, age) "
    values_string = f"values ('{first}', '{last}', '{phone}', '{email}', {age});"
    query_string = insert_string + str(values_string)
    print(query_string)
    cur.execute(query_string)
    my_db.commit()
    return


def search_execute(first, last, phone, email, age):
    my_db = sql_connect()
    cur = my_db.cursor()

    query = (f"select * from contacts WHERE "
             f"first_name LIKE '%{first}%' "
             f"and last_name LIKE '%{last}%' "
             f"and phone_number LIKE '%{phone}%' "
             f"and email_address LIKE '%{email}%' "
             f"and age LIKE '%{age}%';")
    # print(query)
    cur.execute(query)
    search_result = cur.fetchall()
    # print(search_result)
    return search_result


def describe_contacts():
    my_db = sql_connect()
    cur = my_db.cursor()
    query = "describe contacts;"
    cur.execute(query)
    describe_result = cur.fetchall()
    titles = []
    [titles.append(row[0]) for row in describe_result]
    return titles


if __name__ == "__main__":
    try:
        my_db = sql_connect()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    except ValueError as error:
        print(error)

    else:
        gui.phone_gui()
