from bot.bot import create_bot
from config import DISCORD_TOKEN

if __name__ == "__main__":
    client = create_bot()
    client.run(DISCORD_TOKEN)
