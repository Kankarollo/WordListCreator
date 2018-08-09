class WordCreator(object):
    def __init__(self):
        pass

    @staticmethod
    def AllWordsToOneText(_word):
        allWords = ""
        allWords.join(_word)
        return allWords

    @staticmethod
    def CreateWord(_length, _words, _charactersArray, _repeatedLetters):
        word = ""
        return word