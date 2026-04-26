import discord
from database import cursor
from services.diet_planner import DietPlanner
from bot.views import MealTrackerView

_LOCATION_CHOICES = [
    discord.app_commands.Choice(name="Busch", value="W1"),
    discord.app_commands.Choice(name="Livingston", value="W2"),
    discord.app_commands.Choice(name="College Ave", value="W3"),
    discord.app_commands.Choice(name="Cook-Douglass", value="W4"),
]


def setup(client):
    @client.tree.command(name="diet", description="Find Diet Plan")
    @discord.app_commands.choices(location=_LOCATION_CHOICES)
    async def dietplan(content: discord.Interaction, location: discord.app_commands.Choice[str]):
        cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
        data = cursor.fetchone()
        await content.response.defer(ephemeral=True)
        if data is None:
            await content.followup.send("Please create a profile first")
        else:
            menu = DietPlanner(content.user.id, location.name)
            checking = MealTrackerView(content.user, location.name, menu)
            myEmbed = discord.Embed(
                title="DietRX",
                description=f"Please find your diet chart below.\n{menu[3]}",
                color=0x00ff00,
            )
            await content.followup.send(embed=myEmbed, view=checking)
            checking.message = await content.original_response()

    @dietplan.error
    async def on_dietplan_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
        if isinstance(error, discord.app_commands.CommandOnCooldown):
            await interaction.response.send_message(str(error), ephemeral=True)
