def count_words_chars_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            characters = len(text)
            lines = text.count('\n') + 1  # Add 1 for the last line

            print("Number of words:", len(words))
            print("Number of characters:", characters)
            print("Number of lines:", lines)

    except FileNotFoundError:
        print("File not found.")

count_words_chars_lines("lorem.txt")

