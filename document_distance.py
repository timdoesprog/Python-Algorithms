# 15.05.2017
# Compute the document distance

import math

doc1 = "This is a test the document."
doc2 = "This is a test the document."


def main():
    count_doc1 = count_words(doc1)
    count_doc2 = count_words(doc2)
    distance = vector_angle(count_doc1, count_doc2)
    print("The distance between both documents is {0:.6f}.".format(distance))


def split_string_into_words(doc):
    result = []
    char_list = []
    for char in doc:
        if char.isalnum():
            char_list.append(char)
        elif len(char_list) > 0:
            word = "".join(char_list)
            word = word.lower()
            result.append(word)
            char_list = []
    if len(char_list) > 0:
        word = "".join(char_list)
        word = word.lower()
        result.append(word)
        char_list = []
    return result


def count_words(doc):
    list_of_words = split_string_into_words(doc)
    result = {}
    for word in list_of_words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


def vector_angle(vector1, vector2):
    numerator = inner_product(vector1, vector2)
    denominator = math.sqrt(inner_product(vector1, vector1) *
                            inner_product(vector2, vector2))
    return math.acos(numerator / denominator)


def inner_product(vector1, vector2):
    result = 0.0
    for word in vector1:
        if word in vector2:
            result += vector1[word] * vector2[word]
    return result


main()
