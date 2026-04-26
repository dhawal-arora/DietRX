import discord
from database import cursor, mycon

_DIET_CHOICES = [
    discord.app_commands.Choice(name="Vegetarian (Veg)", value="1B"),
    discord.app_commands.Choice(name="Non-Vegetarian (Non-Veg)", value="2B"),
    discord.app_commands.Choice(name="Halal", value="3B"),
    discord.app_commands.Choice(name="Kosher", value="4B"),
    discord.app_commands.Choice(name="Vegan", value="5B"),
]

_ALLERGY_CHOICES = [
    discord.app_commands.Choice(name="Peanuts", value="1B"),
    discord.app_commands.Choice(name="Tree Nuts", value="2B"),
    discord.app_commands.Choice(name="Lactose Intolerance", value="3B"),
    discord.app_commands.Choice(name="Eggs", value="4B"),
    discord.app_commands.Choice(name="Soy", value="5B"),
    discord.app_commands.Choice(name="Wheat", value="6B"),
    discord.app_commands.Choice(name="Fish", value="7B"),
    discord.app_commands.Choice(name="Shellfish", value="8B"),
    discord.app_commands.Choice(name="Sesame", value="9B"),
    discord.app_commands.Choice(name="Mustard", value="10B"),
    discord.app_commands.Choice(name="Meat", value="11B"),
]

_HEALTH_CHOICES = [
    discord.app_commands.Choice(name="Hypertension", value="W1"),
    discord.app_commands.Choice(name="Diabetes", value="W2"),
    discord.app_commands.Choice(name="Menstrual Cycle", value="W3"),
    discord.app_commands.Choice(name="Physically Fit", value="W4"),
]

_GOAL_CHOICES = [
    discord.app_commands.Choice(name="Bulk Weight", value="W1"),
    discord.app_commands.Choice(name="Maintain Weight", value="W2"),
    discord.app_commands.Choice(name="Lose Weight", value="W3"),
    discord.app_commands.Choice(name="Improve my condition", value="W4"),
]

_LOCATION_CHOICES = [
    discord.app_commands.Choice(name="Busch", value="W1"),
    discord.app_commands.Choice(name="Livingston", value="W2"),
    discord.app_commands.Choice(name="College Ave", value="W3"),
    discord.app_commands.Choice(name="Cook-Douglass", value="W4"),
]

_CUSTOM_CHOICES = [
    discord.app_commands.Choice(name="Athlete", value="W1"),
    discord.app_commands.Choice(name="Patient", value="W2"),
    discord.app_commands.Choice(name="Fit Student", value="W3"),
]

_GENDER_CHOICES = [
    discord.app_commands.Choice(name="Male", value="W1"),
    discord.app_commands.Choice(name="Female", value="W2"),
]

_WEIGHT_CHOICES = [
    discord.app_commands.Choice(name="100-115", value="W1"),
    discord.app_commands.Choice(name="116-131", value="W2"),
    discord.app_commands.Choice(name="132-147", value="W3"),
    discord.app_commands.Choice(name="148-163", value="W4"),
    discord.app_commands.Choice(name="164-179", value="W5"),
    discord.app_commands.Choice(name="180-195", value="W6"),
    discord.app_commands.Choice(name="196-211", value="W7"),
    discord.app_commands.Choice(name="212-227", value="W7"),
    discord.app_commands.Choice(name="228-243", value="W7"),
    discord.app_commands.Choice(name="244-259", value="W7"),
    discord.app_commands.Choice(name="260-275", value="W7"),
]

_HEIGHT_CHOICES = [
    discord.app_commands.Choice(name="4.00-4.25", value="W1"),
    discord.app_commands.Choice(name="4.26-4.51", value="W2"),
    discord.app_commands.Choice(name="4.52-4.77", value="W3"),
    discord.app_commands.Choice(name="4.78-5.03", value="W4"),
    discord.app_commands.Choice(name="5.04-5.29", value="W5"),
    discord.app_commands.Choice(name="5.30-5.55", value="W6"),
    discord.app_commands.Choice(name="5.56-5.81", value="W7"),
    discord.app_commands.Choice(name="5.82-6.07", value="W7"),
    discord.app_commands.Choice(name="6.08-6.33", value="W7"),
    discord.app_commands.Choice(name="6.34-6.59", value="W7"),
]

_AGE_CHOICES = [discord.app_commands.Choice(name=str(age), value=age) for age in range(17, 26)]


def setup(client):
    @client.tree.command(name="profile", description="Step 1: Enter Your Info")
    @discord.app_commands.choices(diet=_DIET_CHOICES)
    @discord.app_commands.choices(allergies=_ALLERGY_CHOICES)
    @discord.app_commands.choices(health=_HEALTH_CHOICES)
    @discord.app_commands.choices(goals=_GOAL_CHOICES)
    @discord.app_commands.choices(location=_LOCATION_CHOICES)
    @discord.app_commands.choices(custom=_CUSTOM_CHOICES)
    @discord.app_commands.choices(gender=_GENDER_CHOICES)
    @discord.app_commands.choices(weight=_WEIGHT_CHOICES)
    @discord.app_commands.choices(height=_HEIGHT_CHOICES)
    @discord.app_commands.choices(age=_AGE_CHOICES)
    async def profile(
        content: discord.Interaction,
        diet: discord.app_commands.Choice[str],
        allergies: discord.app_commands.Choice[str],
        health: discord.app_commands.Choice[str],
        goals: discord.app_commands.Choice[str],
        gender: discord.app_commands.Choice[str],
        location: discord.app_commands.Choice[str],
        custom: discord.app_commands.Choice[str],
        weight: discord.app_commands.Choice[str],
        height: discord.app_commands.Choice[str],
        age: discord.app_commands.Choice[int],
    ):
        cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
        data = cursor.fetchone()
        if data is None:
            cursor.execute(
                "INSERT INTO menu VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (content.user.id, diet.name, allergies.name, health.name, goals.name,
                 gender.name, location.name, custom.name, weight.name, height.name, age.name, 0),
            )
            mycon.commit()
            await content.response.send_message(content="Profile Created.", ephemeral=True)
        else:
            await content.response.send_message(content="Profile Already Exists. Please Continue or Delete.", ephemeral=True)

    @client.tree.command(name="deleteprofile", description="Delete Stored Profile")
    async def deleteprofile(content: discord.Interaction):
        cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
        data = cursor.fetchone()
        if data is None:
            await content.response.send_message(content="Profile Doesn't Exist", ephemeral=True)
        else:
            cursor.execute(f"DELETE FROM menu WHERE id={content.user.id}")
            mycon.commit()
            await content.response.send_message(content="Succesfully Deleted.", ephemeral=True)
