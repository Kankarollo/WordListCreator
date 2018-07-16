import appJar

def GUIStarter():
    app = appJar.gui("WordListCreator", "800x600")
    return app


GUIStarter().go()
print("Test COmmit")