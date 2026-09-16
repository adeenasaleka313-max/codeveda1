try:
    with open("demo.txt", "r") as file:
        content = file.read()

        words = content.split()

        word_count = len(words)

        print("number of words:", word_count)

except FileNotFoundError:
    print("Error : File not found")