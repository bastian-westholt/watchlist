# Watchlist 🎬

```
██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗██╗     ██╗███████╗████████╗
██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██║     ██║██╔════╝╚══██╔══╝
██║ █╗ ██║███████║   ██║   ██║     ███████║██║     ██║███████╗   ██║
██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██║     ██║╚════██║   ██║
╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║███████║   ██║
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝╚══════╝   ╚═╝
```

Eine moderne Flask-Webanwendung zum Verwalten deiner persönlichen Film-Watchlists. Behalte den Überblick über alle Filme, die du sehen möchtest!

## 📖 Über das Projekt

Watchlist ist eine Web-App, die es dir ermöglicht:
- Mehrere User zu erstellen (perfekt für Familien oder WGs!)
- Filme zu deiner persönlichen Watchlist hinzuzufügen
- Film-Infos automatisch über die OMDB API abzurufen (Poster, Director, Jahr)
- Filme zu bearbeiten und zu löschen
- Alles in einem schicken Dark-Mode-Design zu verwalten

## ✨ Features

- 🎭 **Multi-User Support** - Jeder User hat seine eigene Watchlist
- 🎬 **OMDB Integration** - Automatisches Abrufen von Film-Daten
- 🎨 **Dark Mode Design** - Modernes, minimalistisches UI
- ✏️ **CRUD Operations** - Erstellen, Lesen, Bearbeiten, Löschen von Filmen
- 📱 **Responsive** - Funktioniert auf Desktop & Mobile
- ⚡ **Schnell & Leichtgewichtig** - Flask + SQLite

## 🛠️ Tech Stack

**Backend:**
- Python 3.13
- Flask (Web Framework)
- SQLAlchemy (ORM)
- SQLite (Database)

**Frontend:**
- HTML5 + Jinja2 Templates
- CSS3 (Custom Design System)
- Google Fonts (BBH Bartle, Jersey 20)

**APIs:**
- OMDB API (Movie Database)

## 📦 Installation

### Voraussetzungen
- Python 3.13 oder höher
- pip (Python Package Manager)

### Setup

1. **Repository klonen**
   ```bash
   git clone <your-repo-url>
   cd watchlist
   ```

2. **Virtual Environment erstellen**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # oder
   .venv\Scripts\activate  # Windows
   ```

3. **Dependencies installieren**
   ```bash
   pip install flask flask-sqlalchemy python-dotenv requests
   ```

4. **OMDB API Key einrichten**
   - Gehe zu [omdbapi.com](http://www.omdbapi.com/apikey.aspx)
   - Registriere dich für einen kostenlosen API Key
   - Erstelle eine `.env` Datei im Projektordner:
     ```
     OMDB_API_KEY=dein_api_key_hier
     ```

5. **App starten**
   ```bash
   python app.py
   ```

6. **Browser öffnen**
   ```
   http://localhost:5001
   ```

Die Datenbank wird automatisch beim ersten Start erstellt!

## 🚀 Usage

### User erstellen
1. Gehe zur Homepage
2. Scrolle zu "ADD NEW USER"
3. Gib einen Namen ein und klicke auf "ADD USER"

### Filme hinzufügen
1. Klicke auf "VIEW MOVIES" bei einem User
2. Scrolle zu "ADD NEW MOVIE"
3. Gib den Filmtitel ein (z.B. "Inception")
4. Die App holt automatisch alle Infos von OMDB!

### Filme bearbeiten/löschen
- **Update:** Ändere den Titel im Input-Feld und klicke "Update"
- **Delete:** Klicke auf "Delete" (mit Bestätigung)

## 📁 Projektstruktur

```
watchlist/
├── app.py              # Main Flask Application
├── models.py           # Database Models (User, Movie)
├── data_manager.py     # Business Logic & DB Operations
├── .env                # Environment Variables (API Key)
├── templates/
│   ├── base.html       # Base Template
│   ├── home.html       # Homepage (User List)
│   └── movies.html     # Movie List Page
├── static/
│   └── style.css       # Custom Styling
└── data/
    └── watchlist.db    # SQLite Database
```

## 🎨 Design Features

- **Dark Theme** - Emerald Green Accents (#10b981)
- **Modern Typography** - Custom Font Stack
- **Smooth Animations** - Hover-Effekte & Transitions
- **Responsive Layout** - Mobile-First Design
- **Alert System** - Success/Error Messages

## 🐛 Known Issues

- Keine User-Authentifizierung (jeder kann alles bearbeiten)
- OMDB API limitiert auf 1000 Requests/Tag (Free Tier)
- Keine Duplikat-Prüfung bei Filmen

## 🚧 Roadmap

- [ ] User Authentication & Login
- [ ] Film-Ratings hinzufügen
- [ ] Suche & Filter für Filme
- [ ] Export zu CSV/PDF
- [ ] Dark/Light Mode Toggle
- [ ] Film-Empfehlungen basierend auf Watchlist

## 📝 License

Dieses Projekt wurde für Lernzwecke erstellt.

## 🙏 Credits

- **OMDB API** - Movie Database
- **Google Fonts** - Typography
- **Flask** - Web Framework
- **SQLAlchemy** - Database ORM

---

Made with ❤️ and Python
