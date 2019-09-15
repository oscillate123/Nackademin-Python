import mysql.connector
import ProgrammeringOchSystemering.egna_projekt.phonebook_gui as gui
from mysql.connector import errorcode


def add_query(first, last, phone, email, age):
    insert_string = "insert into contacts (first_name, last_name, phone_number, email_address, age) "
    values_string = f"values ('{first}', '{last}', {phone}, '{email}', {age});"
    query_string = insert_string + str(values_string)
    return cur.execute(query_string)


try:
    my_db = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password='ThinkVision.24',
        db='phonebook',
    )

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

else:
    # Get user info from the GUI
    user_info = gui.phone_gui()

    # Create a Cursor object to execute queries.
    cur = my_db.cursor()

    # Executing the query received from add_query. Functions add_query uses data from user_info list.
    cur.execute(add_query(first=user_info[0],
                          last=user_info[1],
                          phone=user_info[2],
                          email=user_info[3],
                          age=user_info[4]))
    my_db.commit()

    # print the first and second columns
    for row in cur.fetchall():
        print(row)
