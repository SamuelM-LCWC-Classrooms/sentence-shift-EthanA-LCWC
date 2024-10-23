def shift_sentence(sentence):
    new_list = []
    sentence = sentence.split()
    for item in sentence:
        if item == sentence[0]:
            new_list.append(item)
            letter = item[0]
            continue
        new_item = item[1:]
        new_item = letter + new_item
        letter = item[0]
        new_list.append(new_item)
    first_word = sentence[0]
    first_word = first_word[1:]
    first_word = letter + first_word
    new_list[0] = first_word
    new_sentence = ""
    final_word = new_list[len(new_list) - 1]
    for item in new_list:
        new_sentence += item
        if not item == final_word:
            new_sentence += " "
    return new_sentence
