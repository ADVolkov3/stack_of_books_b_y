def main():
    books_indices = map(int, input().split())
    bu_index = int(input())

    books = list(range(256))
    letters = []
    for index in books_indices:
        letter = chr(books[index])
        letters.append(letter)
        books = [books[index]] + books[0:index] + books[index+1:]
    print(f"The sequence of characters before encoding the stack of books: {''.join(letters)}")

    bu_words = sorted(letters)
    for _ in range(len(letters) - 1):
        for i in range(len(letters)):
            bu_words[i] = letters[i] + bu_words[i]
        bu_words.sort()
    initial_letters = bu_words[bu_index]
    print(f"Original character sequence:: {initial_letters}")


if __name__ == "__main__":
    main()
