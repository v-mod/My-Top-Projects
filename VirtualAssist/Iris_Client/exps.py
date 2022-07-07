from PyDictionary import PyDictionary
def dictSYS():
    dict = PyDictionary()

    meaning = dict.meaning("banana")
    print(meaning)

    translation = dict.translate("happy",'de')
    print(translation)





