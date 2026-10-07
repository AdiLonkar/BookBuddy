"""Shared rule-based logic for Book Buddy (used by console and web UI)."""
import random
import string

# ---------------------------------------------------------------- DATA
BOOKS = {
    "1984": {
        "title": "1984",
        "author": "George Orwell",
        "genre": "Dystopian Fiction",
        "synopsis": "Winston Smith lives under constant surveillance by Big Brother and secretly dares to think for himself.",
    },
    "mockingbird": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Classic Fiction",
        "synopsis": "Scout Finch watches her father, a lawyer, defend a Black man falsely accused in 1930s Alabama.",
    },
    "hobbit": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "synopsis": "Bilbo Baggins leaves his comfortable hole to help dwarves reclaim their mountain from the dragon Smaug.",
    },
    "pride": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": "Romance / Classic",
        "synopsis": "Elizabeth Bennet and the proud Mr. Darcy must overcome first impressions and social expectations.",
    },
    "atomic": {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self-Help",
        "synopsis": "A practical guide to building good habits and breaking bad ones through tiny, consistent changes.",
    },
    "dune": {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "Sci-Fi",
        "synopsis": "Paul Atreides is thrust into a war over Arrakis, the desert planet that produces the universe's most valuable spice.",
    },
    "potter": {
        "title": "Harry Potter and the Philosopher's Stone",
        "author": "J.K. Rowling",
        "genre": "Fantasy",
        "synopsis": "An orphan discovers he is a wizard and begins his first year at Hogwarts.",
    },
    "orient": {
        "title": "Murder on the Orient Express",
        "author": "Agatha Christie",
        "genre": "Mystery",
        "synopsis": "Detective Hercule Poirot investigates a murder aboard a snowbound train.",
    },
    "none": {
        "title": "And Then There Were None",
        "author": "Agatha Christie",
        "genre": "Mystery",
        "synopsis": "Ten strangers on an island are killed one by one, following a nursery rhyme.",
    },
    "gone": {
        "title": "Gone Girl",
        "author": "Gillian Flynn",
        "genre": "Thriller",
        "synopsis": "When Amy disappears on her anniversary, suspicion falls on her husband Nick.",
    },
    "notebook": {
        "title": "The Notebook",
        "author": "Nicholas Sparks",
        "genre": "Romance",
        "synopsis": "A summer romance in the 1940s that is tested by class, war and time.",
    },
    "gatsby": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Classic Fiction",
        "synopsis": "Jay Gatsby's lavish parties hide his obsession with winning back Daisy Buchanan.",
    },
    "sapiens": {
        "title": "Sapiens",
        "author": "Yuval Noah Harari",
        "genre": "Non-Fiction",
        "synopsis": "A sweeping history of humankind, from the Stone Age to the present.",
    },
    "lotr": {
        "title": "The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "genre": "Fantasy",
        "synopsis": "Frodo sets out with eight companions to destroy the One Ring.",
    },
}

# Ordered: first match wins. Keywords are matched against normalized single words.
BOOK_RULES = [
    ("1984", ["1984"]),
    ("mockingbird", ["mockingbird"]),
    ("hobbit", ["hobbit"]),
    ("pride", ["pride", "prejudice"]),
    ("atomic", ["atomic", "habits"]),
]

AUTHORS = [
    (
        ["orwell"],
        "George Orwell",
        "George Orwell (1903-1950) was an English novelist and critic, famous for political satire and dystopian fiction.",
        ["1984"],
    ),
    (
        ["austen", "jane"],
        "Jane Austen",
        "Jane Austen was an English novelist known for her sharp observations of society and courtship.",
        ["pride"],
    ),
    (
        ["clear", "james"],
        "James Clear",
        "James Clear is an author known for writing about habits, decision-making and continuous improvement.",
        ["atomic"],
    ),
    (
        ["rowling", "jk"],
        "J.K. Rowling",
        "J.K. Rowling is a British author, best known for the Harry Potter fantasy series.",
        ["potter"],
    ),
    (
        ["christie", "agatha"],
        "Agatha Christie",
        "Agatha Christie is the 'Queen of Crime', creator of detectives Hercule Poirot and Miss Marple.",
        ["orient", "none"],
    ),
    (
        ["tolkien", "jrr"],
        "J.R.R. Tolkien",
        "J.R.R. Tolkien was an English professor and author of The Hobbit and The Lord of the Rings.",
        ["hobbit", "lotr"],
    ),
    (
        ["harper", "lee"],
        "Harper Lee",
        "Harper Lee was an American novelist who won the Pulitzer Prize for To Kill a Mockingbird.",
        ["mockingbird"],
    ),
]

GENRES = [
    (
        ["scifi", "science", "sci", "fantasy", "dystopian"],
        "Sci-Fi & Fantasy",
        ["dune", "hobbit", "potter", "1984"],
    ),
    (
        ["mystery", "thriller", "detective", "crime", "suspense"],
        "Mystery & Thriller",
        ["orient", "none", "gone"],
    ),
    (
        ["romance", "romantic", "love"],
        "Romance",
        ["pride", "notebook"],
    ),
    (
        ["nonfiction", "selfhelp", "self", "motivation", "habit", "history"],
        "Non-Fiction & Self-Help",
        ["atomic", "sapiens"],
    ),
    (
        ["fiction", "classic", "classics", "novel", "novels"],
        "Fiction & Classics",
        ["mockingbird", "gatsby", "pride", "1984"],
    ),
]

GREETINGS = ["hello", "hi", "hey", "hii", "greetings", "namaste"]
THANKS = ["thanks", "thank", "thx", "thankyou"]
BYES = ["bye", "goodbye", "exit", "quit", "cya"]
HELPS = ["help", "menu", "options", "commands"]
GENERAL = ["book", "books", "read", "reading", "recommend", "suggest", "suggestion"]

GREETING_REPLIES = [
    "Hello! I'm Book Buddy. Ask me for a genre, an author or a book!",
    "Hi there, book lover! What would you like to read today?",
    "Hey! Looking for your next great read? Try 'sci-fi' or 'mystery'.",
]

THANKS_REPLIES = [
    "You're welcome! Happy reading!",
    "Anytime! Want another recommendation?",
]

BYE_REPLIES = [
    "Goodbye! Happy reading!",
    "See you soon. Keep turning pages!",
    "Bye! Come back for more books.",
]

HELP_TEXT = (
    "I can help with:\n"
    "  - Genres: sci-fi, mystery, romance, fiction/classics, non-fiction/self-help\n"
    "  - Authors: George Orwell, J.K. Rowling, Agatha Christie, J.R.R. Tolkien, Harper Lee\n"
    "  - Books: 1984, To Kill a Mockingbird, The Hobbit, Pride and Prejudice, Atomic Habits\n"
    "  - Say 'bye' to exit."
)

FALLBACK = (
    "Hmm, I didn't catch that. Try a genre (e.g. 'mystery'), an author "
    "(e.g. 'who is Tolkien') or type 'help'."
)


# ---------------------------------------------------------------- LOGIC
def normalize(text: str) -> list:
    """Lowercase, strip punctuation, split into words."""
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    return text.split()


def _has(words, keywords):
    return any(word in words for word in keywords)


def _reply(text, category, book_ids=None, end=False):
    return {
        "response": text,
        "category": category,
        "books": [BOOKS[book_id] for book_id in (book_ids or [])],
        "end": end,
    }


def get_book_buddy_response(user_input: str) -> dict:
    words = normalize(user_input)

    if not words:
        return _reply("Please type something and I'll help you find a book.", "empty")

    for book_id, keywords in BOOK_RULES:
        if _has(words, keywords):
            book = BOOKS[book_id]
            return _reply(
                f"'{book['title']}' by {book['author']} ({book['genre']}): {book['synopsis']}",
                "book",
                [book_id],
            )

    for keywords, name, bio, book_ids in AUTHORS:
        if _has(words, keywords):
            return _reply(f"{bio} Here are some of their books:", "author", book_ids)

    for keywords, label, book_ids in GENRES:
        if _has(words, keywords):
            return _reply(f"Great choice! Here are some {label} picks:", "genre", book_ids)

    if _has(words, BYES):
        return _reply(random.choice(BYE_REPLIES), "farewell", end=True)

    if _has(words, GREETINGS):
        return _reply(random.choice(GREETING_REPLIES), "greeting")

    if _has(words, THANKS):
        return _reply(random.choice(THANKS_REPLIES), "thanks")

    if _has(words, HELPS):
        return _reply(HELP_TEXT, "help")

    if _has(words, GENERAL):
        return _reply(
            "I love books too! Which genre do you prefer: sci-fi, mystery, romance, "
            "classics or self-help?",
            "general",
        )

    return _reply(FALLBACK, "unknown")


QUICK_TOPICS = [
    "Recommend Sci-Fi",
    "Mystery Novels",
    "Romance books",
    "Who is George Orwell?",
    "Who is J.K. Rowling?",
    "Tell me about 1984",
    "Self-help",
    "Help",
]