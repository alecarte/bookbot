import sys

from stats import get_char_count, get_num_words, sorted_dict

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

else:

    def main(filepath):
        print(
            f"============ BOOKBOT ============\nAnalyzing book found at {filepath}\n----------- Word Count ----------\nFound {get_num_words(filepath)} total words\n--------- Character Count -------"
        )
        for i in sorted_dict(get_char_count(filepath)):
            print(f"{i['char']}: {i['num']}")
        print("\n============= END ===============")

    filepath = sys.argv[1]
    main(filepath)
