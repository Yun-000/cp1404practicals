"""
Word Occurrences
Estimate: 15 minutes
Actual:   16 minutes
"""


def main():
    input_string = input("Enter a string: ")
    word_to_count = count_word(input_string)

    sorted_word_to_count = dict(sorted(word_to_count.items()))
    max_length = max(len(word) for word in sorted_word_to_count.keys())

    print("Text:", input_string)
    for word, count in sorted_word_to_count.items():
        print(f"{word:{max_length}} : {count}")


def count_word(text):
    word_to_count = {}
    words = text.split()

    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    return word_to_count


main()


