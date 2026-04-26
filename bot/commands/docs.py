import discord
from database import cursor
from services.doctor_finder import get_docs


def setup(client):
    @client.tree.command(name="finddocs", description="Get RWJ docs")
    async def finddocs(content: discord.Interaction):
        cursor.execute(f"SELECT * FROM menu WHERE health!=\"Physically Fit\" AND id={content.user.id}")
        data = cursor.fetchone()
        if data is not None:
            doctors = get_docs(content.user.id)
            await content.response.send_message(content=f"{doctors}", ephemeral=True)
        else:
            await content.response.send_message(content="Please create a profile first/You are physically fit.", ephemeral=True)
