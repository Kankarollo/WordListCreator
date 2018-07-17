from GUI import GUICreator


def savePath():
    global filepath
    filepath = app.saveBox()
    app.setEntry("Choose path to save: ", filepath)


filepath = ""
letters_to_use = ""
characters_to_use = ""
password_length = 0
words_to_use = ""
app = GUICreator.gUIStarter()
app.addButton("Path", savePath, 2, 1)
app.addButton("GENERATE", None, 3, 1)
app.go()
