from appJar import gui


def error_box(output):

    app.setTitle("  Confirm message")
    app.setTransparency(95)
    app.setIcon(image="galaxy.ico")
    app.setResizable(False)
    app.setSize("200x150")

    app.okBox("ok_box", output)
