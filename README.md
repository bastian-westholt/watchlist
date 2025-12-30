# Watchlist

```
██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗██╗     ██╗███████╗████████╗
██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██║     ██║██╔════╝╚══██╔══╝
██║ █╗ ██║███████║   ██║   ██║     ███████║██║     ██║███████╗   ██║
██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██║     ██║╚════██║   ██║
╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║███████║   ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝
```

Eine moderne, production-ready Flask-Webanwendung zum Verwalten deiner persönlichen Film-Watchlists mit vollständigem Error Handling und Security Features.

## 🎯 Über das Projekt

Watchlist ist eine professionelle Web-App mit:
- **Multi-User Support** - Jeder User hat seine eigene Watchlist
- **OMDB API Integration** - Automatisches Abrufen von Film-Metadaten
- **Comprehensive Error Handling** - Alle API & Database Errors werden sauber gehandhabt
- **Authorization System** - User können nur ihre eigenen Movies bearbeiten/löschen
- **Modern Dark-Mode Design** - Minimalistisches, responsive UI
- **PEP8-Konform** - Professionell dokumentierter, sauberer Code

## ✨ Features

### Core Features
- ✅ **Multi-User Management** - Mehrere User mit separaten Watchlists
- ✅ **OMDB Integration** - Automatische Film-Daten (Poster, Director, Jahr)
- ✅ **CRUD Operations** - Erstellen, Lesen, Bearbeiten, Löschen von Filmen
- ✅ **Dark Mode Design** - Modernes UI mit Emerald Green Accents
- ✅ **Responsive Layout** - Desktop & Mobile optimiert

### Security & Error Handling
- 🔒 **Authorization** - Ownership-basierte Zugriffskontrolle
- ⚠️ **Error Handling** - Comprehensive Exception Handling für:
  - OMDB API Errors (Timeout, Connection, Invalid Response)
  - Database Errors (NoResultFound, IntegrityError)
  - User Input Validation
- 🛡️ **Security** - Protection gegen unauthorized Movie manipulation
- 📄 **Custom Error Pages** - 404 & 500 Error Pages im Design

### Code Quality
- 📝 **PEP8-Konform** - Alle Python Files formatiert & dokumentiert
- 📖 **Docstrings** - Vollständige Dokumentation aller Funktionen/Klassen
- 🧪 **Error Recovery** - Automatisches `db.session.rollback()` bei Fehlern

## 🛠️ Tech Stack

**Backend:**
- Python 3.13
- Flask 3.1.0 (Web Framework)
- Flask-SQLAlchemy 3.1.1 (ORM)
- SQLite (Database)
- python-dotenv 1.1.1 (Environment Variables)
- requests 2.32.5 (HTTP Client)

**Frontend:**
- HTML5 + Jinja2 Templates
- CSS3 (Custom Design System mit CSS Variables)
- Google Fonts (BBH Bartle, Jersey 20)

**External APIs:**
- OMDB API (http://www.omdbapi.com/)

## 📦 Installation

### Voraussetzungen
- Python 3.13 oder höher
- pip (Python Package Manager)
- OMDB API Key (kostenlos)

### Setup

1. **Repository klonen**
   ```bash
   git clone <your-repo-url>
   cd watchlist
   ```

2. **Virtual Environment erstellen**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   # oder
   .venv\Scripts\activate  # Windows
   ```

3. **Dependencies installieren**
   ```bash
   pip install -r requirements.txt
   ```

4. **OMDB API Key einrichten**
   - Gehe zu [omdbapi.com](http://www.omdbapi.com/apikey.aspx)
   - Registriere dich für einen kostenlosen API Key
   - Erstelle eine `.env` Datei im Projektordner:
     ```env
     OMDB_API_KEY=your_api_key_here
     ```

5. **App starten**
   ```bash
   python app.py
   ```

6. **Browser öffnen**
   ```
   http://localhost:5002
   ```

Die Datenbank wird automatisch beim ersten Start erstellt!

## 🚀 Usage

### User erstellen
1. Gehe zur Homepage (`/`)
2. Scrolle zu "ADD NEW USER"
3. Gib einen Namen ein und klicke auf "ADD USER"

### Filme hinzufügen
1. Klicke auf "VIEW MOVIES" bei einem User
2. Scrolle zu "ADD MOVIE"
3. Gib den Filmtitel ein (z.B. "Inception")
4. Die App holt automatisch alle Infos von OMDB!

### Filme bearbeiten/löschen
- **Update:** Ändere den Titel im Input-Feld und klicke "Update"
- **Delete:** Klicke auf "Delete" (mit Bestätigungs-Dialog)

**Security:** User können nur ihre eigenen Movies bearbeiten/löschen!

## 📁 Projektstruktur

```
watchlist/
├── app.py                      # Flask Application & Routes
├── models.py                   # SQLAlchemy Database Models
├── data_manager.py             # Business Logic & Error Handling
├── requirements.txt            # Python Dependencies
├── .env                        # Environment Variables (API Key)
├── .claude/
│   ├── CLAUDE.md              # Project Documentation
│   └── ERROR_HANDLING_PLAN.md # Error Handling Implementation
├── templates/
│   ├── base.html              # Base Template (Layout)
│   ├── home.html              # Homepage (User List)
│   ├── movies.html            # Movie List Page
│   ├── 404.html               # Custom 404 Error Page
│   └── 500.html               # Custom 500 Error Page
├── static/
│   └── style.css              # Custom Design System
└── data/
    └── watchlist.db           # SQLite Database (auto-generated)
```

## 🎨 Design Features

### Color Palette
- **Background:** `#0a0a0a` (Deep Black)
- **Surface:** `#151515` / `#1a1a1a` (Dark Gray)
- **Accent:** `#10b981` (Emerald Green)
- **Text:** `#e5e5e5` (Light Gray)
- **Error:** `#ef4444` (Red) / `#fb7185` (Pink)

### CSS Features
- **Design System** - CSS Variables für konsistente Styling
- **Smooth Animations** - Transitions & Hover-Effekte
- **Responsive Breakpoints** - Mobile-optimiert ab 768px
- **Alert System** - Success (Türkis) & Error (Rosa) Alerts

## 🔒 Security & Error Handling

### Authorization
- **Ownership Check:** User können nur ihre eigenen Movies bearbeiten/löschen
- **Permission Errors:** "You do not have permission" Messages bei unauthorized Access
- **User Validation:** User Existence Check bei allen Movie Operations

### Error Handling
**OMDB API:**
- `Timeout` → "Request timed out"
- `ConnectionError` → "Connection error. Check your internet."
- `RequestException` → "Failed to fetch movie data"
- `ValueError` → "Invalid data from OMDB"

**Database:**
- `NoResultFound` → "Movie not found"
- Generic `Exception` → Automatic `db.session.rollback()` + Error Message

**Custom Error Pages:**
- `404 Not Found` → Styled 404.html Page
- `500 Internal Server Error` → Styled 500.html Page mit Rollback

### Input Validation
- Empty title checks
- User existence verification
- OMDB response validation (Director, Year fields)
- Poster "N/A" handling

## 📊 Database Schema

### User Model
```python
- id (Integer, Primary Key, Auto-Increment)
- name (String(100), Not Null)
```

### Movie Model
```python
- id (Integer, Primary Key, Auto-Increment)
- title (String(100), Not Null)
- director (String(100), Not Null)
- year (Integer, Not Null)
- poster_url (String(200), Nullable)
- user_id (Integer, Foreign Key → users.id, Not Null)
```

**Relationship:** One-to-Many (1 User → Many Movies)

## 🧪 Testing

### Manual Test Cases
- ✅ Add Movie: "Inception" → Success
- ✅ Add Movie: "xyz123gibberish" → "Movie not found" Error
- ✅ Disconnect Internet → "Connection error" Alert
- ✅ Timeout Test (>5s) → "Request timed out" Alert
- ✅ Update Movie (as owner) → Success
- ✅ Update Movie (not owner) → "Permission denied" Error
- ✅ Delete Movie (as owner) → Success
- ✅ Delete Movie (not owner) → "Permission denied" Error
- ✅ Invalid Movie ID → "Movie not found" Error
- ✅ 404 Route → Custom 404 Page
- ✅ Database Error → Custom 500 Page + Rollback

## 📝 API Reference

### Routes

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Homepage - List all users |
| `POST` | `/users` | Create new user |
| `GET` | `/users/<user_id>/movies` | Get user's movies |
| `POST` | `/users/<user_id>/movies` | Add movie via OMDB |
| `POST` | `/users/<user_id>/movies/<movie_id>/update` | Update movie (with auth) |
| `POST` | `/users/<user_id>/movies/<movie_id>/delete` | Delete movie (with auth) |

### Query Parameters
- `?success=True` - Show success alert
- `?update=True` - Show update alert
- `?delete=True` - Show delete alert
- `?error=<message>` - Show error alert with message

## 🔧 Configuration

### Environment Variables (.env)
```env
OMDB_API_KEY=your_api_key_here
```

### Flask Config (app.py)
```python
SQLALCHEMY_DATABASE_URI = "sqlite:///data/watchlist.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True  # Development only
HOST = "0.0.0.0"
PORT = 5002
```

## 🐛 Known Issues

- ⚠️ Keine User-Authentifizierung (URL-basierter Access)
- ⚠️ OMDB API Free Tier: 1000 Requests/Tag Limit
- 🟡 TV-Serien Year Parsing (En-Dash vs Bindestrich) → Year = 0 (minor)

## 🗺️ Roadmap

### Planned Features
- [ ] User Authentication & Session Management
- [ ] Password Protection für User Accounts
- [ ] Film-Ratings System (1-5 Stars)
- [ ] Suche & Filter für Movies (Genre, Jahr, Director)
- [ ] Export zu CSV/PDF
- [ ] Dark/Light Mode Toggle
- [ ] Film-Empfehlungen basierend auf Watchlist
- [ ] Watchlist Sharing via Public Links
- [ ] Movie Details Modal (Plot, Actors, Runtime)
- [ ] Watched/Unwatched Status Toggle

### Code Improvements
- [ ] Unit Tests (pytest)
- [ ] Integration Tests
- [ ] API Rate Limiting
- [ ] Caching für OMDB Requests
- [ ] Migration zu PostgreSQL (für Production)
- [ ] Docker Support

## 📄 License

Dieses Projekt wurde für Lernzwecke erstellt.

## 🙏 Credits

- **OMDB API** - Open Movie Database
- **Google Fonts** - BBH Bartle & Jersey 20 Typography
- **Flask** - Web Framework by Pallets
- **SQLAlchemy** - Python SQL Toolkit & ORM
- **Claude Code** - Development Assistance

## 👨‍💻 Development

### Code Quality Standards
- ✅ PEP8 Compliance
- ✅ Comprehensive Docstrings
- ✅ Type Hints (where applicable)
- ✅ Error Handling Best Practices
- ✅ Security-First Design

### Contributing
Dieses Projekt ist ein Lernprojekt. Contributions sind willkommen!

---

**Made with ❤️ and Python**
**Version:** 1.0.0 (Production-Ready)
**Last Updated:** 2025-12-30
