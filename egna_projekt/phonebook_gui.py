from appJar import gui
import pandas as pd
import numpy as np
import ProgrammeringOchSystemering.egna_projekt.phonebook_sql as sql


def phone_gui():
    app = gui()

    def ok_box(output):

        app.setTitle("  Confirm message")
        app.setTransparency(95)
        app.setIcon(image="galaxy.ico")
        app.setResizable(False)
        app.setSize("200x150")

        app.okBox("ok_box", output)

    def press(value):

        if value == "Add":
            sql.add_execute(app.getEntry("first_name"),
                            app.getEntry("last_name"),
                            app.getEntry("phone_number"),
                            app.getEntry("email_address"),
                            app.getEntry("age"))

            app.clearAllEntries()

            ok_box("Contact added!")

        elif value == "Cancel":
            app.stop()

        elif value == "Search":
            result = sql.search_execute(app.getEntry("search_first"),
                                        app.getEntry("search_last"),
                                        app.getEntry("search_phone"),
                                        app.getEntry("search_email"),
                                        app.getEntry("search_age"))
            result = list(result)
            result_len = []
            [result_len.append(i + 1) for i, v in enumerate(result)]
            pd_df = pd.DataFrame(np.array([result]).reshape(len(result), 6),
                                 index=result_len,
                                 columns=sql.describe_contacts())
            print(pd_df)


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
