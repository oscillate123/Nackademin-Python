import mysql.connector
import ProgrammeringOchSystemering.caesar.cipher as c
from mysql.connector import errorcode


try:
    my_db = mysql.connector.connect(
        host='localhost',
        port='3306',
        user='root',
        password=c.getTranslatedMessage(c.getMode(), c.getMessage(), c.getKey()),
        db='world',
    )

except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)

else:
    # Create a Cursor object to execute queries.
    cur = my_db.cursor()

    # Select data from table using SQL query.
    cur.execute("SELECT * FROM city;")

    # print the first and second columns
    for row in cur.fetchall():
        print(row[0], " ", row[1], " ", row[2], " ", row[3])
