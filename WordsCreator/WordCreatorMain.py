from WordsCreator.WordsListCreator import WordsListCreator


def CharactersToUse():
    print("From which character to which use (a-z:")
    charactersArray = []
    character_start = input("Input beginning letter: ")
    character_end = input("Input ending letter: ")
    if CharactersValidator(character_start, character_end):
        AddToArray(character_start, character_end, charactersArray)
    else:
        AddToArray('a', 'z', charactersArray)
    return charactersArray


def CharactersValidator(start_letter, end_letter):
    if ord(start_letter) > ord(end_letter):
        return False
    return True


def AddToArray(start_letter, end_letter, charactersArray):
    for i in range(ord(start_letter), ord(end_letter)):
        charactersArray.append(chr(i))


def ExpressionToUse(_length):
    while True:
        expression = input("Input expression to use in your word: ")
        if ExpressionValidator(expression, _length):
            return expression


def ExpressionValidator(expression, _length):
    if len(expression) <= _length:
        return True
    else:
        print("Invalid expression!")
        return False


def isRepeatedEvents():
    while True:
        answer = input("Do you want to letters to be repeated? (y/n)")
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print("Wrong answer! Answer y (Yes!) or n (No!)")


if __name__ == '__main__':
    print("Welcome to WordListCreator!")
    length = input("Length of word: ")
    words = ExpressionToUse(length)
    charactersArray = CharactersToUse()
    repeatedLetters = isRepeatedEvents()
    wordList = WordsListCreator(length, words, charactersArray, repeatedLetters)
