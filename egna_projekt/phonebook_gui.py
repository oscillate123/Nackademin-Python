from appJar import gui


def phone_gui():
    app = gui()

    user_info = []
    user_search = []

    def press(value):

        if value == "Add":
            (first, last, phone, email, age) = (app.getEntry("first_name"),
                                                app.getEntry("last_name"),
                                                app.getEntry("phone_number"),
                                                app.getEntry("email_address"),
                                                app.getEntry("age"))
            user_info.append(first)
            user_info.append(last)
            user_info.append(phone)
            user_info.append(email)
            user_info.append(age)

            app.clearAllEntries()

            app.setTitle("  Confirm message")
            app.setTransparency(95)
            app.setIcon(image="galaxy.ico")
            app.setResizable(False)
            app.setSize("200x150")

            app.okBox("ok_box", "Contact added!")

            app.setTitle("  Phonebook")
            app.setTransparency(95)
            app.setIcon(image="galaxy.ico")
            app.setResizable(True)
            app.setSize("600x300")

            return user_info
        elif value == "Cancel":
            app.stop()
        elif value == "Search":
            name_search = app.getEntry("search")

            if " " in name_search:
                print(name_search.split())
                name_search = name_search.split()
                for item in name_search:
                    user_search.append(item)
            else:
                print(name_search)
                user_search.append(name_search)

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

    # HEADER SEARCH
    app.addLabel("search_empty1", " ", 0, 4)
    app.addLabel("search_header", "SEARCH CONTACT", 0, 5)
    app.addLabel("search_empty2", " ", 0, 6)
    app.addLabel("search_empty3", " ", 0, 7)

    # FIRST NAME
    app.addLabel("first_name", "First name:", 1, 0)
    app.addEntry("first_name", 1, 1)
    app.addLabel("first_name_empty", " ", 1, 2)

    # SEARCH
    app.addLabel("search", "Search:", 1, 4)
    app.addEntry("search", 1, 5)
    app.addLabel("search_empty4", " ", 1, 6)
    app.addButton("Search", press, 1, 7)
    app.addLabel("search_empty5", " ", 1, 8)

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

    # BUTTONS
    app.addButtons(["Add", "Cancel"], press, 7, 1)

    app.go()

    return user_info, user_search


if __name__ == "__main__":
    print(phone_gui())
