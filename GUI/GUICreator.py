import appJar

def savePath():
    print("Wykonana funkcja")

def gUIStarter():
    app = appJar.gui("WordListCreator", "600x400", )
    app.addLabelNumericEntry("Password Length: ", 0, 0)
    app.addLabelEntry("Includes: ", 1, 0)
    app.addLabelEntry("Which letters(a-z): ", 0, 1)
    app.addLabelEntry("Which characters(a,g,!,5...): ", 1, 1)
    app.addLabelEntry("Choose path to save: ", 2, 0)
    app.checkBox("UpperLetters")
    app.checkBox("With repeats:")


    return app
