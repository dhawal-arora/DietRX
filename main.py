import mysql.connector as sqltor
mycon=sqltor.connect(host="",user="", passwd="",database="")
if mycon.is_connected():
    print('Succesfully Connected to MySql')
cursor=mycon.cursor()
#cursor.execute("DROP TABLE menu")
#cursor.execute("CREATE TABLE menu(id numeric(23) NOT NULL PRIMARY KEY, diet varchar(100) NOT NULL,allergies varchar(100) NOT NULL,health varchar(100) NOT NULL,goals varchar(100) NOT NULL,gender varchar(100) NOT NULL,location varchar(100) NOT NULL,custom varchar(100) NOT NULL,weight varchar(100) NOT NULL,height varchar(100) NOT NULL,age varchar(100) NOT NULL);")
import openai
from typing import Any, final
import os
import discord
from discord.ext import commands
from discord.interactions import Interaction
from discord.ui.item import Item
import math
import datetime
from discord.ext import tasks
import pytz
from datetime import datetime as dhawal

openai.api_key = "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"

client = commands.Bot(command_prefix=['d.'], intents=discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
  print ('We have logged in as {0.user}' .format (client))
  await client.wait_until_ready()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/busreport"))
  await client.tree.sync()


@client.tree.command(name="help", description="Help command.")
async def help(content: discord.Interaction):
    myEmbed = discord.Embed(title="RU On Time", description="I help save your time...\n\n**Step 1. Enter On-Campus Housing Details**\n</buschhousing:1160279628703862784>: Choose if staying on Busch.\n</livihousing:1160291767032221708>: Choose if staying on Livingston.\n</collegeavehousing:1160291767032221706>: Choose if staying on College Avenue.\n</cookdoughousing:1160291767032221707>: Choose if staying on Cook-Douglass.\n\n**Step 2. Enter Class Schedule After /openschedule**\n</buschclass:1160304171770196011>: Enter Busch Class.\n</liviclass:1160323302645043352>: Enter Livingston Class.\n</collegeaveclass:1160323302645043353>: Enter College Ave Class.\n</cookdougclass:1160323302645043354>: Enter Cook-Douglass class.\n\n**Step 3: Use /closeschedule To Submit Final Class List **\n\n**Step 4. Use /busreport for Generated Report**\n\n**Extra Commands:**\n </openschedule:1160456245887635527>: To denote you will add classes.\n</closeschedule:1160360343437058190>: To denote you are done entering schedule.\n</deletehousing:1160449357141790752>: Delete stored housing info completely.\n</deleteschedule:1160449357141790751>: Delete stored schedule completely.", color=0x00ff00)
    #buttons=Empty()
    #support(buttons)
    #await content.response.send_message(embed=myEmbed, view=buttons)
    await content.response.send_message(embed=myEmbed)

discordtoken = ""
#----------------HOUSING--------------------------------------------
def send(x):
    return (x)

@client.tree.command(name="info", description="Step 1: Enter Your Info")
@discord.app_commands.choices(diet=
                              [discord.app_commands.Choice(name="Vegetarian (Veg)", value="1B"),
                               discord.app_commands.Choice(name="Non-Vegetarian (Non-Veg)", value="2B"),
                               discord.app_commands.Choice(name="Halal", value="3B"),
                               discord.app_commands.Choice(name="Kosher", value="4B"),
                               discord.app_commands.Choice(name="Vegan", value="4B"),
                               ])
@discord.app_commands.choices(allergies=
                              [discord.app_commands.Choice(name="Peanuts", value="1B"),
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
                               ])
@discord.app_commands.choices(health=
                              [discord.app_commands.Choice(name="Monday", value="W1"),
                               discord.app_commands.Choice(name="Tuesday", value="W2"),
                               discord.app_commands.Choice(name="Wednesday", value="W3"),
                               discord.app_commands.Choice(name="Thursday", value="W4"),
                               discord.app_commands.Choice(name="Friday", value="W5"),
                               discord.app_commands.Choice(name="Saturday", value="W6"),
                               discord.app_commands.Choice(name="Sunday", value="W7"),
                               ])
@discord.app_commands.choices(goals=
                              [discord.app_commands.Choice(name="Bulk Weight", value="W1"),
                               discord.app_commands.Choice(name="Maintain Weight", value="W2"),
                               discord.app_commands.Choice(name="Lose Weight", value="W3"),
                               discord.app_commands.Choice(name="Improve my condition", value="W4"),
                               ])
@discord.app_commands.choices(location=
                              [discord.app_commands.Choice(name="Busch", value="W1"),
                               discord.app_commands.Choice(name="Livingston", value="W2"),
                               discord.app_commands.Choice(name="College Ave", value="W3"),
                               discord.app_commands.Choice(name="Cook-Douglass", value="W4"),
                               ])
@discord.app_commands.choices(custom=
                              [discord.app_commands.Choice(name="Athlete", value="W1"),
                               discord.app_commands.Choice(name="Patient", value="W2"),
                               discord.app_commands.Choice(name="Fit Student", value="W3"),
                               ])
@discord.app_commands.choices(gender=
                              [discord.app_commands.Choice(name="Male", value="W1"),
                               discord.app_commands.Choice(name="Female", value="W2"),
                               ])
@discord.app_commands.choices(weight=
                              [discord.app_commands.Choice(name="100-115", value="W1"),
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
                               ])
@discord.app_commands.choices(height=
                              [discord.app_commands.Choice(name="4.00-4.25", value="W1"),
                               discord.app_commands.Choice(name="4.26-4.51", value="W2"),
                               discord.app_commands.Choice(name="4.52-4.77", value="W3"),
                               discord.app_commands.Choice(name="4.78-5.03", value="W4"),
                               discord.app_commands.Choice(name="5.04-5.29", value="W5"),
                               discord.app_commands.Choice(name="5.30-5.55", value="W6"),
                               discord.app_commands.Choice(name="5.56-5.81", value="W7"),
                               discord.app_commands.Choice(name="5.82-6.07", value="W7"),
                               discord.app_commands.Choice(name="6.08-6.33", value="W7"),
                               discord.app_commands.Choice(name="6.34-6.59", value="W7"),
                               ])
@discord.app_commands.choices(age=
                              [discord.app_commands.Choice(name=17, value=17),
                               discord.app_commands.Choice(name=18, value=18),
                               discord.app_commands.Choice(name=19, value=19),
                               discord.app_commands.Choice(name=20, value=20),
                               discord.app_commands.Choice(name=21, value=21),
                               discord.app_commands.Choice(name=22, value=22),
                               discord.app_commands.Choice(name=23, value=23),
                               discord.app_commands.Choice(name=24, value=24),
                               discord.app_commands.Choice(name=25, value=25),
                               ])

def DietPlanner(id, dietaryRestriction, healthCondition, goals, gender, weight, height, age, diningHallData):
    diseasesDict = {"Hypertension":"requirements per day for hypertension - potassium:3400mg men, 2600mg women; sodium(max amount): 1500mg men, 1560mg women; calcium:1250mg; protein:102g; magnesium: 500mg; fiber:30g; saturatedFat(max):14g",
                 "diabetes" : "requirements per day for diabetes - calories:2500 men,2000 women; carbs:343.75g men,275g women;fat(max):83.33g men, 66.67g women;protein:62.5g men,50g women;sugar(max):31.25g men,25g women", 
                 "menstrualCycle" : "requirements per day for menstrualCycle - carbs:225g, fat:56g, protein:150g, iron:18mg"}
    
    conversation = [{"role":"system", "content":"You are an assistant that gives nutritional advice to students based on input menus from campus dining halls"}]

    discordInput = "dietary restriction:{}, health condition:{}, goals:{}, gender:{}, weight:{}, height:{}, age:{}".format(dietaryRestriction,healthCondition,goals,gender,weight,height,age)
    conversation.append({"role":"user","content":str(diningHallData)+ ' This is todays breakfast menu for dining hall. Give me a diet plan along with the number of servings for todays breakfast based on the following user preferences, user data and disease data: '+ discordInput + " " + diseasesDict[healthCondition]})
    GPTresponse = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return GPTresponse['choices'][0]['message']['content'].strip("\n").strip()

async def info(content: discord.Interaction, diet:discord.app_commands.Choice[str], allergies:discord.app_commands.Choice[str] ,health:discord.app_commands.Choice[str],goals:discord.app_commands.Choice[str],gender:discord.app_commands.Choice[str],location:discord.app_commands.Choice[str],custom:discord.app_commands.Choice[str],weight:discord.app_commands.Choice[str],height:discord.app_commands.Choice[str],age:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
            cursor.execute("INSERT INTO menu VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (content.user.id, diet.name, allergies.name,health.name,goals.name,gender.name,location.name,custom.name,weight.name,height.name,age.name))
            mycon.commit()
            await content.response.send_message(content="Profile Created.", ephemeral=True)
    else: 
            await content.response.send_message(content="Profile Already Exists. Please Continue or Delete.", ephemeral=True)


'''
async def cookdougclass(content: discord.Interaction, location:discord.app_commands.Choice[str], classname: str, starthour:discord.app_commands.Choice[int], startminute:discord.app_commands.Choice[int], endhour:discord.app_commands.Choice[int], endminute:discord.app_commands.Choice[int],day:discord.app_commands.Choice[str]):
    cursor.execute(f"SELECT * FROM housing WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Please add Dorm first using /housing (Step:1)", ephemeral=True)
    else:
        if (starthour.name*60)+startminute.name < (endhour.name*60)+endminute.name:
            cursor.execute("INSERT INTO classes VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, location.name, classname,datetime.time(starthour.name,startminute.name), datetime.time(endhour.name,endminute.name),day.name))
            mycon.commit()
            await content.response.send_message(content="Class Added. Add Next Class OR End Entering using /closeschedule", ephemeral=True)
        else: 
            await content.response.send_message(content="Start time after end time. Please Try Again.", ephemeral=True)
'''
client.run(discordtoken)

