def count_words(file):
    words = file.split()
    word_count = 0
    for word in words:
        word_count += 1

    return word_count

def count_character(file):
    character = {}
    for char in file:
        if char.lower() in character:
            character[char.lower()] += 1
        else:
            character[char.lower()] = 1

    return character


def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        file_contents = f.read()

        print(f"--- Begin report of {path} ---")

        words = count_words(file_contents)
        print(f"{words} words found in the document")

        character = count_character(file_contents)
        #print(character)

        char_list = []
        for char in character:
            if char.isalpha():
                char_list.append(character[char])

        char_list.sort()
        print()

        for i in range(len(char_list) - 1, -1, -1):
            for char in character:
                if char.isalpha() and character[char] == char_list[i]:
                    print(f"The '{char}' character was found {char_list[i]} times")

        print("--- End report ---")



main()
