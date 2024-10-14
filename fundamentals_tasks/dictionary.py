
word_and_definition = input()
test_words = input()
command = input()
word_dict = {}

word_and_definition = word_and_definition.split(' | ')
for parts in word_and_definition:
    if ': ' in parts:
        part = parts.split(': ')
        word, definition = part[0], part[1]
        if word in word_dict:
            word_dict[word].append(definition)
        else:
            word_dict[word] = [definition]

test_words_lst = test_words.split(' | ')
if command == "Test":
    result = []
    for word in test_words_lst:
        if word in word_dict:
            result.append(f"{word}:")
            for definition in word_dict[word]:
                result.append(f" -{definition}")

    print("\n".join(result))

elif command == "Hand Over":
    result = " ".join(word_dict.keys())
    print(result)
