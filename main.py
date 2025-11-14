import sys
from stats import get_num_of_words, get_character_counts, get_character_count_summary

def get_book_text(filepath):
    file_contents=""
    with open(filepath) as f:
        file_contents=f.read()
    
    return(file_contents)



def main():
    
    if not len(sys.argv)==2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    book_path=sys.argv[1]
    
    book_contents=get_book_text(book_path)


    num_words=get_num_of_words(book_contents)

    # print(f"Found {num_words} total words")
    
    character_counts=get_character_counts(book_contents)
    #print(character_counts)

    character_count_summary=get_character_count_summary(character_counts)
    
    #print(character_count_summary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for record in character_count_summary:
        if record["char"].isalpha():
            print(f"{record["char"]}: {record["count"]}")
    print("============= END ===============")

main()
