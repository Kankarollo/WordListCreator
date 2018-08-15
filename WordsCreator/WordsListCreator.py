from math import factorial
import itertools

class WordsListCreator(object):
    def __init__(self, _length, _words, _charactersArray, _repeatedLetters):
        self.length = _length
        self.words = _words
        self.charactersArray = _charactersArray
        self.repeatedLetters = _repeatedLetters

    def CreateWordList(self):
        word = ""
        if self.words:
            self.CreateWordListWITHwordsInIt()
        else:
            self.CreateWordListWITHOUTwordsInIt()
        return word

    # if string words is empty
    def CreateWordListWITHwordsInIt(self):
        if self.repeatedLetters:
            self.CreateWordListWITHRepeatedLetters()
        else:
            self.CreateWordListWITHOUTRepeatedLetters()

    # if string words is NOT empty
    def CreateWordListWITHOUTwordsInIt(self):
        if self.repeatedLetters:
            self.CreateWordListWITHRepeatedLetters()
        else:
            self.CreateWordListWITHOUTRepeatedLetters()

    @staticmethod
    def CreateWordListWITHRepeatedLetters(_charactersArray):
        wordlistArray = []
        for letter in _charactersArray:
            print(letter)
            wordlistArray.append(letter)
        list = itertools.combinations(wordlistArray, 3)
        for i in list:
            print(i)

    def CreateWordListWITHOUTRepeatedLetters(self):
        pass


if __name__ == '__main__':
    charactersArray = []
    for i in range(ord('a'), ord('z')):
        charactersArray.append(chr(i))
    WordsListCreator.CreateWordListWITHRepeatedLetters(charactersArray)
