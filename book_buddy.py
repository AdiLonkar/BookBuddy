"""Book Buddy - console version (run: python book_buddy.py)."""
from book_logic import get_book_buddy_response


def banner():
    print("=" * 60)
    print("              BOOK BUDDY - Book Recommendation Bot")
    print("=" * 60)
    print("Ask about genres, authors or books. Type 'help' or 'bye'.\n")


def main():
    banner()
    while True:
        try:
            user = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBook Buddy: Goodbye! Happy reading!")
            break
        result = get_book_buddy_response(user)
        print("Book Buddy:", result["response"])
        for book in result["books"]:
            if result["category"] != "book":
                print(f"   - {book['title']} by {book['author']} [{book['genre']}]")
        print()
        if result["end"]:
            break


if __name__ == "__main__":
    main()