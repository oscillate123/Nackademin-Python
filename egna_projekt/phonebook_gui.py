from appJar import gui
import egna_projekt.phonebook_sql as sql
import egna_projekt.phonebook_func as func
import mysql.connector
from mysql.connector import errorcode


def phone_gui():
    app = gui()

    def ok_box(output):
        app.okBox(" ", output)

    def error_box(error):
        app.clearAllEntries()
        ok_box(error)

    def search_contact():

        phone_entry = ""
        age_entry = ""
        try:
            sql.sql_connect()
            #  if user input is not empty, call function "is_entrytype_valid"
            if app.getEntry("search_phone") != "":
                phone_entry = func.is_number_valid(app.getEntry("search_phone"))
            if app.getEntry("search_age") != "":
                age_entry = func.is_age_valid(app.getEntry("search_age"))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                ok_box("Something is wrong with your database user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                ok_box("Database does not exist")
            else:
                ok_box(err)
        except ValueError as error:
            error_box(error)
        else:
            result = sql.search_execute(app.getEntry("search_first"),
                                        app.getEntry("search_last"),
                                        phone_entry,
                                        app.getEntry("search_email"),
                                        age_entry)

            app.startSubWindow("Search", modal=False)
            app.showAllSubWindows()
            app.addLabel("result_empty", "      ", 0, 0)

            for column_index, column in enumerate(sql.describe_contacts()):
                app.addLabel(f"{column_index}_head", f"{column}", 0, (int(column_index) + 1))
            for row_index, items in enumerate(result):
                app.addLabel(f"{row_index}_info", f"{row_index + 1}", (int(row_index) + 1), 0)
                items = list(items)
                i = 1
                for value in items:
                    app.addLabel(f"{value}_{items[0]}", f"{value}", (row_index + 1), i)
                    i += 1

            app.stopSubWindow()

    def add_contact():

        first_entry = ""
        last_entry = ""
        phone_entry = ""
        email_entry = ""
        age_entry = ""

        try:
            sql.sql_connect()
            #  if user input is not empty, call function "is_entrytype_valid"
            if app.getEntry("first_name") != "":
                first_entry = app.getEntry("first_name")
            else:
                pass
            if app.getEntry("last_name") != "":
                last_entry = app.getEntry("last_name")
            else:
                pass

            if app.getEntry("phone_number") != "":
                phone_entry = func.is_number_valid(app.getEntry("search_phone"))
            if app.getEntry("email_address") != "":
                age_entry = func.is_email_valid(app.getEntry("email_address"))
            if app.getEntry("age") != "":
                age_entry = func.is_age_valid(app.getEntry("search_age"))

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                ok_box("Something is wrong with your database user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                ok_box("Database does not exist")
            else:
                ok_box(err)

        except ValueError as error:
            error_box(error)

        else:
            sql.add_execute(first_entry,
                            last_entry,
                            phone_entry,
                            app.getEntry("email_address"),
                            age_entry)

            app.clearAllEntries()

            ok_box("Contact added!")

    def press(value):
        if value == "Add":
            add_contact()

        elif value == "Cancel":
            app.stop()

        elif value == "Search":
            search_contact()

    # WINDOW SETTINGS
    app.setTitle("  Phonebook")
    app.setTransparency(95)
    app.setIcon(image="galaxy.ico")
    app.setResizable(True)
    app.setSize("600x300")

    # HEADER ADD
    app.addLabel("title_empty1", " ", 0, 0)
    app.addLabel("title_header", "ADD CONTACT", 0, 1)
    app.addLabel("title_empty2", " ", 0, 2)

    # FIRST NAME
    app.addLabel("first_name", "First name:", 1, 0)
    app.addEntry("first_name", 1, 1)
    app.addLabel("first_name_empty", " ", 1, 2)

    # LAST NAME
    app.addLabel("last_name", "Last name:", 2, 0)
    app.addEntry("last_name", 2, 1)
    app.addLabel("last_name_empty", " ", 2, 2)

    # PHONE NUMBER
    app.addLabel("phone_number", "Phone:", 3, 0)
    app.addEntry("phone_number", 3, 1)
    app.addLabel("phone_empty", " ", 3, 2)

    # EMAIL ADDRESS
    app.addLabel("email_address", "Email:", 4, 0)
    app.addEntry("email_address", 4, 1)
    app.addLabel("email_empty", " ", 4, 2)

    # AGE
    app.addLabel("age", "Age:", 5, 0)
    app.addEntry("age", 5, 1)
    app.addLabel("age_empty", " ", 5, 2)

    # EMPTY
    app.addLabel("empty1", " ", 6, 0)
    app.addLabel("empty2", " ", 6, 1)
    app.addLabel("empty3", " ", 6, 2)

    # ADD BUTTONS
    app.addButtons(["Add", "Cancel"], press, 7, 1)

    # HEADER SEARCH
    app.addLabel("search_empty1", " ", 0, 4)
    app.addLabel("search_header", "SEARCH CONTACT", 0, 5)
    app.addLabel("search_empty2", " ", 0, 6)
    app.addLabel("search_empty3", " ", 0, 7)

    # SEARCH FIRST
    app.addLabel("search_first", "First name:", 1, 4)
    app.addEntry("search_first", 1, 5)
    app.addLabel("search_empty4", " ", 1, 6)

    # SEARCH LAST
    app.addLabel("search_last", "Last name:", 2, 4)
    app.addEntry("search_last", 2, 5)
    app.addLabel("search_empty5", " ", 2, 6)

    # SEARCH PHONE
    app.addLabel("search_phone", "Phone:", 3, 4)
    app.addEntry("search_phone", 3, 5)
    app.addLabel("search_empty6", " ", 3, 6)

    # SEARCH EMAIL
    app.addLabel("search_email", "Email:", 4, 4)
    app.addEntry("search_email", 4, 5)
    app.addLabel("search_empty7", " ", 4, 6)

    # SEARCH AGE
    app.addLabel("search_age", "Age:", 5, 4)
    app.addEntry("search_age", 5, 5)
    app.addLabel("search_empty8", " ", 5, 6)

    # EMPTY
    app.addLabel("empty4", " ", 6, 3)
    app.addLabel("empty5", " ", 6, 4)
    app.addLabel("empty6", " ", 6, 5)

    # ADD BUTTONS
    app.addButton("Search", press, 7, 5)

    app.go()


if __name__ == "__main__":
    phone_gui()
