ALPHABETS = {
    'a': [[3], [2, 4], [1, 2, 3, 4, 5], [1, 5], [1, 5]],
    'b': [[1, 2, 3, 4], [1, 5], [1, 2, 3, 4], [1, 5], [1, 2, 3, 4]],
    'c': [[2, 3, 4, 5], [1], [1], [1], [2, 3, 4, 5]],
    'd': [[1, 2, 3, 4], [1, 5], [1, 5], [1, 5], [1, 2, 3, 4]],
    'e': [[1, 2, 3, 4, 5], [1], [1, 2, 3, 4, 5], [1], [1, 2, 3, 4, 5]],
    'f': [[1, 2, 3, 4, 5], [1], [1, 2, 3, 4, 5], [1], [1]],
    'g': [[2, 3, 4, 5], [1], [1, 3, 4, 5], [1, 5], [2, 3, 4, 5]],
    'h': [[1, 5], [1, 5], [1, 2, 3, 4, 5], [1, 5], [1, 5]],
    'i': [[1, 2, 3, 4, 5], [3], [3], [3], [1, 2, 3, 4, 5]],
    'j': [[1, 2, 3, 4, 5], [3], [3], [1, 3], [2, 3]],
    'k': [[1, 4], [1, 3], [1, 2], [1, 3], [1, 4]],
    'l': [[1], [1], [1], [1], [1, 2, 3, 4]],
    'm': [[1, 5], [1, 2, 4, 5], [1, 3, 5], [1, 5], [1, 5]],
    'n': [[1, 5], [1, 2, 5], [1, 3, 5], [1, 4, 5], [1, 5]],
    'o': [[2, 3, 4], [1, 5], [1, 5], [1, 5], [2, 3, 4]],
    'p': [[1, 2, 3, 4], [1, 5], [1, 2, 3, 4], [1], [1]],
    'q': [[3], [2, 4], [1, 5], [2, 4], [3, 5]],
    'r': [[1, 2, 3, 4], [1, 5], [1, 2, 3, 4], [1, 3], [1, 4, 5]],
    's': [[2, 3, 4, 5], [1], [2, 3, 4], [5], [1, 2, 3, 4]],
    't': [[1, 2, 3, 4, 5], [3], [3], [3], [3]],
    'u': [[1, 5], [1, 5], [1, 5], [1, 5], [2, 3, 4]],
    'v': [[1, 5], [1, 5], [1, 5], [2, 4], [3]],
    'w': [[1, 5], [1, 5], [1, 3, 5], [1, 2, 4, 5], [1, 5]],
    'x': [[1, 5], [2, 4], [3], [2, 4], [1, 5]],
    'y': [[1, 5], [2, 4], [3], [3], [3]],
    'z': [[1, 2, 3, 4, 5], [4], [3], [2], [1, 2, 3, 4, 5]],
}

def zoom_print(word):
    word_split = list(word)
    each_char_length = 6
    word_length = len(word_split)

    full_word_cord_array = []
    for each_alphabet in word_split:
        full_word_cord_array.append(ALPHABETS[each_alphabet])

    for row in range(5):
        new_cords = []
        for col in range(word_length):
            new_values_array = [(num + (col *  each_char_length)) for num in full_word_cord_array[col][row]]
            new_cords.append(new_values_array)
        flattened_array = [element for sublist in new_cords for element in sublist]
        for cord in range(flattened_array[-1]+1):
            print("*", end="") if cord in flattened_array else  print(" ", end="")
        print("")


while(True):
    word = input("Enter Word : ")
    if word == "e":
        break
    zoom_print(word)