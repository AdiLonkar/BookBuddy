# Book Buddy - Book Recommendation Chatbot

This Flask project was reconstructed from the code shown in the shared chat. The share clipped several code blocks, so omitted portions have been filled in to match the described behavior; this is not a byte-for-byte extraction of the original ZIP.

## Project structure

```text
BookBuddy/
├── README.md
├── app.py
├── book_buddy.py
├── book_logic.py
├── requirements.txt
├── static/
│   ├── app.js
│   └── style.css
└── templates/
    └── index.html
```

The project uses Python and Flask, not PHP or MySQL. Book data is stored in `book_logic.py`; there is no database file.

## Run in VS Code

1. Optionally create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

2. Install the dependency:

   ```powershell
   pip install -r requirements.txt
   ```

3. Start the web app:

   ```powershell
   python app.py
   ```

4. Open http://127.0.0.1:5000.

To run the console version instead, use `python book_buddy.py`.

## Sample conversation

```text
You: hi
Book Buddy: Hello! I'm Book Buddy. Ask me for a genre, an author or a book!

You: mystery
Book Buddy: Great choice! Here are some Mystery & Thriller picks:
   - Murder on the Orient Express by Agatha Christie [Mystery]

You: bye
Book Buddy: Goodbye! Happy reading!
```

The chatbot normalizes input and matches keywords to books, authors, genres, greetings, help, and farewell intents. It uses no machine-learning dependencies.