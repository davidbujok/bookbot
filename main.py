import re

def main():
    path = './books/frankenstein.txt'
    book_text = get_text_book(path)
    word_count = get_word_count(book_text)
    characters_statistics = count_character_occurance(book_text)
    create_report(word_count, characters_statistics)
    return word_count

def get_text_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    word_count = len(text.split(" "))
    return word_count

def count_character_occurance(text):
    statistics = {}
    unified_text = text.lower()

    for char in unified_text:
        if statistics.get(char) == None:
            statistics[char] = 1
        else:
            statistics[char] += 1
    return statistics

def create_report(word_count, characters_statistics):
    print(f"{word_count} words found in the book")
    list_of_characters = []
    def sort_on(dict):
        return dict['num']

    for (key, value) in characters_statistics.items():
        list_of_characters.append({'char': key, 'num': value})

    list_of_characters.sort(reverse=True, key=sort_on)

    match = re.compile("[a-z]")
    
    for char in list_of_characters:
        if match.match(char['char']):
            print(f"The {char['char']} was found {char['num']} times")


main()
