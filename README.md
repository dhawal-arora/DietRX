# DietRX

A Discord bot built in 36 hours for **Rutgers Health Hack 2023**. DietRX matches students' dietary needs and health conditions to meals available at Rutgers dining halls, generating personalized daily meal plans powered by GPT-3.5.

---

## Features

- **User Profiles** — store dietary restrictions, allergies, health conditions, fitness goals, and biometrics
- **AI Diet Planning** — generates breakfast, lunch, and dinner plans from live dining hall menus via the OpenAI API
- **Meal Tracking** — interactive Discord buttons to log meals and earn points throughout the day
- **Doctor Finder** — surfaces relevant RWJ physicians based on the user's health condition
- **Leaderboard** — points-based leaderboard to encourage healthy eating habits

## Bot Commands

| Command | Description |
|---|---|
| `/profile` | Create your profile (diet, allergies, health, goals, biometrics) |
| `/deleteprofile` | Delete your stored profile |
| `/diet` | Generate a daily meal plan for a chosen dining hall |
| `/finddocs` | Find RWJ doctors matching your health condition |
| `/leaderboard` | View the points leaderboard |
| `/help` | Show all available commands |

## Project Structure

```
DietRX/
├── main.py                  # Entry point
├── config.py                # Loads config from environment variables
├── database.py              # Shared MySQL connection
├── scrapers/
│   ├── nutrition.py         # Scrapes nutritional info from Rutgers menu portal
│   └── menu.py              # Scrapes full dining hall menus → data*.json
├── services/
│   ├── diet_planner.py      # Builds meal plans via OpenAI GPT-3.5
│   └── doctor_finder.py     # Scrapes RWJ doctor listings
└── bot/
    ├── bot.py               # Bot factory and on_ready event
    ├── views.py             # MealTrackerView (breakfast/lunch/dinner buttons)
    └── commands/
        ├── profile.py       # /profile, /deleteprofile
        ├── diet.py          # /diet
        ├── docs.py          # /finddocs
        └── misc.py          # /help, /leaderboard
```

## Setup

### 1. Clone the repository

```sh
git clone https://github.com/dhawal-arora/DietRX.git
cd DietRX
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and fill in your credentials:

```sh
cp .env.example .env
```

```env
DB_HOST=your_mysql_host
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_NAME=your_database_name

OPENAI_API_KEY=your_openai_api_key
DISCORD_TOKEN=your_discord_bot_token
```

### 4. Set up the MySQL database

Two tables are required:

```sql
CREATE TABLE menu (
    id          NUMERIC(23)    NOT NULL,
    diet        VARCHAR(50),
    allergies   VARCHAR(50),
    health      VARCHAR(50),
    goals       VARCHAR(50),
    gender      VARCHAR(50),
    location    VARCHAR(50),
    custom      VARCHAR(50),
    weight      VARCHAR(50),
    height      VARCHAR(50),
    age         VARCHAR(50),
    points      INT
);

CREATE TABLE history (
    id           NUMERIC(23)    NOT NULL,
    description  VARCHAR(65000) NOT NULL,
    meal         VARCHAR(50)    NOT NULL,
    points       INT            NOT NULL,
    date_column  DATE,
    time_column  TIME
);
```

### 5. Generate dining hall menu data

Menu data is not stored in the repository. Run the scraper to generate the JSON files the bot reads from:

```sh
python -m scrapers.menu
```

This writes `breakfast.json` (and equivalents for other meals/locations) to the project root.

### 6. Run the bot

```sh
python main.py
```

## Tech Stack

- **Discord.py** — bot framework
- **OpenAI GPT-3.5** — AI meal plan generation
- **MySQL** — user profile and history storage
- **BeautifulSoup + Requests** — menu and doctor data scraping

## Built at

Rutgers Health Hack 2023 — 36-hour hackathon
