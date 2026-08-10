# 📚 Bookshelf Tracker

A small full-stack practice project built to consolidate FastAPI + Pydantic
concepts (CRUD, path/query params, enums, `Field()` constraints, response
models). Tracks books across three
states — To Read, Reading, Finished — with genre/status filtering and a
star-rating flow when you mark something finished.


---

## Tech Stack

- **Backend:** FastAPI + Pydantic (in-memory storage, no database)
- **Frontend:** Plain HTML/CSS/JS — no build tooling, no framework
- **Docs:** Scalar (`/scalar`) instead of the default Swagger UI

## Project Structure

```
bookshelf-tracker/
├── backend/
│   ├── main.py           # FastAPI app, CORS, all CRUD routes
│   ├── schema.py          # Genre/Status enums + Book models
│   ├── venv/
│   ├── requirements.txt
│   └── .gitignore
├── frontend/
│   ├── index.html          # Kanban board UI + fetch calls to the API
│   └── styles.css
└── README.md
```

## Data Model

**Enums**
- `Genre`: fiction, nonfiction, sci_fi, biography, fantasy
- `Status`: to_read, reading, finished

**Models**
| Model | Used for |
|---|---|
| `AddBook` | POST body — title, author, genre, pages |
| `EditBook` | PUT body — full replace, includes status + rating |
| `StatusUpdate` | PATCH body — status + optional rating only |
| `ReadBook` | Every response — full stored record |

New books always start at `status = to_read`, assigned server-side.

## API Endpoints

| Method | Path | Notes |
|---|---|---|
| GET | `/books` | List all books |
| GET | `/book/{id}` | Single book, 404 if missing |
| POST | `/book` | Create a book (starts as `to_read`) |
| PUT | `/book/{id}` | Full replace |
| PATCH | `/book/{id}` | Update status (+ rating when finishing) |
| DELETE | `/book/{id}` | Remove a book |
| GET | `/scalar` | Interactive API docs |

## Running Locally

Requires two terminals running at the same time.

**Backend**
```bash
cd backend
python3 -m venv venv          # first time only
source venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```
Runs at `http://127.0.0.1:8000`

**Frontend**
```bash
cd frontend
python -m http.server 5500 --bind 127.0.0.1
```
Open `http://127.0.0.1:5500/index.html` — type the URL directly rather
than relying on browser autocomplete/history, to avoid it resolving to the
IPv6 loopback (`[::1]`) instead of `127.0.0.1`, which will fail CORS.

## Notes

- No database — in-memory dict, intentionally simple so the project stays
  focused on the API layer rather than persistence.
- No auth, single-shelf, personal-use scope only.
- CORS is configured for `127.0.0.1:5500`, `localhost:5500`, and `[::1]:5500`
  specifically, to cover every way a local dev server might resolve.
