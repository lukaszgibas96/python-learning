from helpers import get_words, save_counts

def main():

    words = get_words("address.txt")
    lowercase_word = [word.lower() for word in words if len(word) > 4 ]

    counts = {word: words.count(word) for word in lowercase_word}
    
    save_counts(counts)

main()

 