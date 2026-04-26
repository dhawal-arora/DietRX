import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "na05-sql.pebblehost.com")
DB_USER = os.getenv("DB_USER", "customer_586593_ruontime")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "customer_586593_ruontime")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
COMMAND_PREFIX = "d."
