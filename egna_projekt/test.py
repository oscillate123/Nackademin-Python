# from appJar import gui
# import ProgrammeringOchSystemering.egna_projekt.phonebook_sql as sql
#
# app = gui()
#
#
# def result_box(value):
#     # value will be 'Search'
#
#     app.showSubWindow(value)
#
#     result = sql.search_execute(app.getEntry("search_first"),
#                                 app.getEntry("search_last"),
#                                 app.getEntry("search_phone"),
#                                 app.getEntry("search_email"),
#                                 app.getEntry("search_age"))
#
#     result = list(result)
#
#     app.setTitle("  Confirm message")
#     app.setTransparency(95)
#     app.setIcon(image="galaxy.ico")
#     app.setResizable(False)
#     app.setSize("200x150")
#
#     app.startSubWindow("Search", modal=False)
#     app.addLabel("l2", str(result))
#     app.stopSubWindow()
#
#
# app.go()