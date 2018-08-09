
def MakingTextFile(_text):
    filename = "test.txt"
    with open(filename, "w+") as wordListFile:
        wordListFile.write(_text)
        print("It's done")
        wordListFile.close()

