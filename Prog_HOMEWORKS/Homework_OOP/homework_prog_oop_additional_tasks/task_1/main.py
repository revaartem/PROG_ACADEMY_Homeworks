import text_method

if __name__ == "__main__":
    unit = text_method.TextMethods('text.txt')
    print(unit.characters())
    print(unit.characters_without_spaces())
    print(unit.words())
    print(unit.sentences())
