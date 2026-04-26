import discord
from datetime import datetime
from database import cursor, mycon


class MealTrackerView(discord.ui.View):
    def __init__(self, user, location, menu):
        self.user = user
        self.location = location
        self.menu = menu
        super().__init__(timeout=None)

    @discord.ui.button(label="Breakfast Done", style=discord.ButtonStyle.green, custom_id="1")
    async def breakfast(self, content: discord.Interaction, button: discord.ui.Button):
        if self.user == content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column='{formatted_date}' AND meal=\"Breakfast\";")
            data = cursor.fetchone()
            if data is None:
                cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[0], "Breakfast", 2, formatted_date, formatted_time))
                mycon.commit()
                cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
                mycon.commit()
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = str(cursor.fetchone())
                await content.response.send_message(content=f"Breakfast Data Entered. You have 2 points! Win more throughout the day.", ephemeral=True)
            else:
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = cursor.fetchone()
                await content.response.send_message(content=f"Breakfast Already Eaten. You have {points} points! Win more throughout the day.", ephemeral=True)

    @discord.ui.button(label="Lunch Done", style=discord.ButtonStyle.red, custom_id="2")
    async def lunch(self, content: discord.Interaction, button: discord.ui.Button):
        if self.user == content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column='{formatted_date}' AND meal=\"Lunch\";")
            data = cursor.fetchone()
            if data is None:
                cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[1], "Lunch", 2, formatted_date, formatted_time))
                mycon.commit()
                cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
                mycon.commit()
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = cursor.fetchone()
                await content.response.send_message(content=f"Lunch Data Entered. You have {points} points! Win more in dinner!", ephemeral=True)
            else:
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = cursor.fetchone()
                await content.response.send_message(content=f"Lunch Already Eaten. You have {points} points! Win more in dinner.", ephemeral=True)

    @discord.ui.button(label="Dinner Done", style=discord.ButtonStyle.blurple, custom_id="3")
    async def dinner(self, content: discord.Interaction, button: discord.ui.Button):
        if self.user == content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column='{formatted_date}' AND meal=\"Dinner\";")
            data = cursor.fetchone()
            if data is None:
                cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[2], "Dinner", 2, formatted_date, formatted_time))
                mycon.commit()
                cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
                mycon.commit()
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = cursor.fetchone()
                await content.response.send_message(content=f"Dinner Data Entered. You have {points} points! Win more tomorrow!", ephemeral=True)
            else:
                cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
                points = cursor.fetchone()
                await content.response.send_message(content=f"Dinner Already Eaten. You have {points} points! Win more tomorrow!", ephemeral=True)
            self.stop()
