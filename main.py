import mysql.connector as sqltor
mycon=sqltor.connect(host="na05-sql.pebblehost.com",user="customer_586593_ruontime", passwd="$5CtoqReuy@Zzr8nje#u",database="customer_586593_ruontime")
if mycon.is_connected():
    print('Succesfully Connected to MySql')
cursor=mycon.cursor()
#cursor.execute("DROP TABLE history")
#cursor.execute("DELETE FROM menu WHERE diet='Kosher';")
#mycon.commit()
#cursor.execute("CREATE TABLE history(id numeric(23) NOT NULL, description varchar(65000) NOT NULL, meal varchar(50) NOT NULL), points INT NOT NULL, date  ")
import openai
from typing import Any, final
import os
import discord
from discord.ext import commands
from discord.interactions import Interaction
from discord.ui.item import Item
import math
import json
from discord.ext import tasks
import pytz
from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

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
    myEmbed = discord.Embed(title="DietRX", description="**Eat The RITE food**\n\nCreate a profile 👤: </profile:1170722473633919026>\n Create Diet Plan 🍎: </diet:1170569290072719502>\n Find RWJ doctors 👨‍⚕️: </finddocs:1170612893314727967>\n Delete profile ❌: </deleteprofile:1170539459134107660>\n Point Leaderboard 🏆: </leaderboard:1170619099810889818>", color=0x00ff00)
    await content.response.send_message(embed=myEmbed)

openai.api_key = "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"
discordtoken = "MTE3MDQwNzUzOTQwMjM1NDgwMA.GYtmHM.0LNEK7debHEK92x91yzjkdC05h2UsBVvAERrm0"

def DietPlanner(id, location):
    if(location == "Livingston"):
        with open("data0.json") as breakfast:
            data1 = json.load(breakfast)
        with open("data1.json") as lunch:
            data2 = json.load(lunch)
        with open("data2.json") as dinner:
            data3 = json.load(dinner)
    elif(location == "Busch"):
        with open("data3.json") as breakfast:
            data1 = json.load(breakfast)
        with open("data4.json") as lunch:
            data2 = json.load(lunch)
        with open("data5.json") as dinner:
            data3 = json.load(dinner)        
    elif(location == "Cook-Douglass"):
        with open("data6.json") as breakfast:
            data1 = json.load(breakfast)
        with open("data7.json") as lunch:
            data2 = json.load(lunch)
        with open("data8.json") as dinner:
            data3 = json.load(dinner)
    else:
        with open("data9.json") as breakfast:
            data1 = json.load(breakfast)
        with open("data10.json") as lunch:
            data2 = json.load(lunch)
        with open("data11.json") as dinner:
            data3 = json.load(dinner)        
    diningHallData = str(data1) 
    
    cursor.execute("SELECT diet FROM menu WHERE id={};".format(id))
    dietaryRestriction = cursor.fetchone()
    cursor.execute("SELECT health FROM menu WHERE id={};".format(id))
    healthCondition = cursor.fetchone()
    cursor.execute("SELECT goals FROM menu WHERE id={};".format(id))
    goals = cursor.fetchone()
    cursor.execute("SELECT gender FROM menu WHERE id={};".format(id))
    gender = cursor.fetchone()
    cursor.execute("SELECT weight FROM menu WHERE id={};".format(id))
    weight = cursor.fetchone()
    cursor.execute("SELECT height FROM menu WHERE id={};".format(id))
    height = cursor.fetchone()
    cursor.execute("SELECT age FROM menu WHERE id={};".format(id))
    age = cursor.fetchone()
    
    diseasesDict = {"Hypertension":"requirements per day for hypertension - potassium:3400mg men, 2600mg women; sodium(max amount): 1500mg men, 1560mg women; calcium:1250mg; protein:102g; magnesium: 500mg; fiber:30g; saturatedFat(max):14g",
                 "Diabetes" : "requirements per day for diabetes - calories:2500 men,2000 women; carbs:343.75g men,275g women;fat(max):83.33g men, 66.67g women;protein:62.5g men,50g women;sugar(max):31.25g men,25g women", 
                 "Menstrual Cycle" : "requirements per day for menstrualCycle - carbs:225g, fat:56g, protein:150g, iron:18mg",
                 "Physically Fit" : "requirements per day for generally physically fit people - carbs:300g men,260g women; protein:55g men,50g women; sugars(max):120g men,90g women; fat:95g men,70g women; saturatedFat(max):30g men,20g women; sodium(max):6g"}
    
    conversation = [{"role":"system", "content":"You are an assistant that gives nutritional advice to students based on input menus from campus dining halls"}]

    discordInput = "dietary restriction:{}, health condition:{}, goals:{}, gender:{}, weight:{}, height:{}, age:{}".format(dietaryRestriction,healthCondition,goals,gender,weight,height,age)
    conversation.append({"role":"user","content":diningHallData+ 'This is todays breakfast menu for dining hall. Give me a diet plan along with the number of servings for todays breakfast based on the following user preferences, user data and disease data'+ discordInput + " " + diseasesDict[healthCondition[0]]})
    GPTresponse1 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    conversation.pop()

    diningHallData = str(data2)
    conversation.append({"role":"user","content":diningHallData+ 'This is todays lunch menu for dining hall. Give me a diet plan along with the number of servings for todays lunch based on the following user preferences, user data and disease data'+ discordInput + " " + diseasesDict[healthCondition[0]]})
    GPTresponse2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    conversation.pop()

    diningHallData = str(data3)
    conversation.append({"role":"user","content":diningHallData+ 'This is todays dinner menu for dining hall. Give me a diet plan along with the number of servings for todays dinner based on the following user preferences, user data and disease data'+ discordInput + " " + diseasesDict[healthCondition[0]]})
    GPTresponse3 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    conversation.pop()
    x = []
    x.append(location + " Breakfast: " + GPTresponse1['choices'][0]['message']['content'].strip("\n").strip())
    x.append(location + " Lunch: " + GPTresponse2['choices'][0]['message']['content'].strip("\n").strip())
    x.append(location + " Dinner: " + GPTresponse3['choices'][0]['message']['content'].strip("\n").strip())
    
    x.append(location + " Dining Hall:\n\n" +  "Breakfast: " + GPTresponse1['choices'][0]['message']['content'].strip("\n").strip() + "\n\n" + "Lunch: " + GPTresponse2['choices'][0]['message']['content'].strip("\n").strip() + "\n\n" +"Dinner: " + GPTresponse3['choices'][0]['message']['content'].strip("\n").strip())

    return x
#_-------------------------------------------

def get_docs(id):
    command = "SELECT health FROM menu WHERE id="+str(id)+";"
    cursor.execute(command)
    condition = cursor.fetchone()
    condition = condition[0]
    # discordtoken = "MTE3MDQwNzUzOTQwMjM1NDgwMA.GMTV-Y.6BAtXH8KoLmQIKW_nPmjnfxzJ-YKt5VaJ3JUzU"

    # URL = "https://www.zocdoc.com/search?address=08901&after_5pm=false&before_10am=false&day_filter=AnyDay&dr_specialty=153&filters=%7B%7D&fit_questionnaire_type=PCP&gender=-1&insurance_carrier=323&insurance_plan=2364&language=-1&offset=0&reason_visit=3849&searchOriginator=SearchBar&searchQueryGuid=&searchType=specialty&search_query=Primary+Care+Physician+%28PCP%29&sees_children=false&sort_type=Default&visitType=inPersonAndVirtualVisits"
    # URL = "https://umg.rwjms.rutgers.edu/find_provider.php"
    URL = "https://umg.rwjms.rutgers.edu/search_results.php?chosen_insurance=&chosen_insurance_label=&chosen_specialty=&chosen_symptoms_or_condition=" + \
        str(condition)+"&typed_specialty=&typed_symptoms_or_condition=&view="

    docs = {}

    req = requests.get(URL).text

    bs = soup(req, 'html5lib')

    body = bs.find('body')

    div1 = body.find('div', attrs={'id': 'container '})

    div2 = div1.find('div', attrs={'id': 'main-slide'})

    cont = div2.find('div', attrs={'class': 'container'})

    form = cont.find('form', attrs={'id': 'doc_form'})

    table_div = form.find('table', attrs={'class': 'table table-striped'})

    # table = table_div.find('table', attrs={'id': 'myTable'})
    tbody = table_div.find('tbody')

    for i in tbody.find_all('tr'):
        # docs[i.find('td').text]
        print(i.find('td').text)
        li = []
        for w, j in enumerate(i.find_all('td')):
            if w == 0:
                continue
            li.append(j.get_text(strip=True))

        docs[i.find('td').text] = li

    doctors = " "
    for a, q in enumerate(docs.keys()):
        doctors = doctors + str(q) + '\n' + str(docs[q][1]) + '\n' + str(docs[q][2]) + '\n\n'
        if a > 3: 
            break

    return doctors
#----------------HOUSING--------------------------------------------

@client.tree.command(name="profile", description="Step 1: Enter Your Info")
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
                              [discord.app_commands.Choice(name="Hypertension", value="W1"),
                               discord.app_commands.Choice(name="Diabetes", value="W2"),
                               discord.app_commands.Choice(name="Menstrual Cycle", value="W3"),
                               discord.app_commands.Choice(name="Physically Fit", value="W4"),
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

async def profile(content: discord.Interaction, diet:discord.app_commands.Choice[str], allergies:discord.app_commands.Choice[str] ,health:discord.app_commands.Choice[str],goals:discord.app_commands.Choice[str],gender:discord.app_commands.Choice[str],location:discord.app_commands.Choice[str],custom:discord.app_commands.Choice[str],weight:discord.app_commands.Choice[str],height:discord.app_commands.Choice[str],age:discord.app_commands.Choice[int]):
    cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
            cursor.execute("INSERT INTO menu VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (content.user.id, diet.name, allergies.name,health.name,goals.name,gender.name,location.name,custom.name,weight.name,height.name,age.name,0))
            mycon.commit()
            await content.response.send_message(content="Profile Created.", ephemeral=True)
    else:
            await content.response.send_message(content="Profile Already Exists. Please Continue or Delete.", ephemeral=True)


@client.tree.command(name="deleteprofile", description="Delete Stored Profile")
async def deleteprofile(content: discord.Interaction):
    cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
    data=cursor.fetchone()
    if data==None:
        await content.response.send_message(content="Profile Doesn't Exist", ephemeral=True)
    else:
        cursor.execute(f" DELETE FROM menu WHERE id={content.user.id}")
        mycon.commit()
        await content.response.send_message(content="Succesfully Deleted.", ephemeral=True)

@client.tree.command(name="diet", description="Find Diet Plan")
@discord.app_commands.choices(location=
                              [discord.app_commands.Choice(name="Busch", value="W1"),
                               discord.app_commands.Choice(name="Livingston", value="W2"),
                               discord.app_commands.Choice(name="College Ave", value="W3"),
                               discord.app_commands.Choice(name="Cook-Douglass", value="W4"),
                               ])
async def dietplan(content: discord.Interaction, location:discord.app_commands.Choice[str]):
    cursor.execute(f"SELECT * FROM menu WHERE id={content.user.id}")
    data=cursor.fetchone()
    await content.response.defer(ephemeral=True)
    if data==None:
        await content.followup.send("Please create a profile first")
    else:
        menu=DietPlanner(content.user.id,location.name)
        checking = checker(content.user,location.name,menu)
        myEmbed = discord.Embed(title="DietRX", description=f"Please find your diet chart below.\n{menu[3]}",color=0x00ff00)
        await content.followup.send(embed=myEmbed,view=checking)
        checking.message = await content.original_response()

class checker(discord.ui.View):
    def __init__(self, user, location,menu):
      self.user = user
      self.location = location
      self.menu = menu
      super().__init__()

    @discord.ui.button(label="Breakfast Done",style=discord.ButtonStyle.green, custom_id="1")
    async def breakfast(self, content:discord.Interaction,button:discord.ui.Button):
        if self.user==content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column={formatted_date} AND meal=\"Breakfast\";")
            data=cursor.fetchone()
            if data==None:
               cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[0], "Breakfast",2,formatted_date,formatted_time))
               mycon.commit()
               cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
               mycon.commit()
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=str(cursor.fetchone())
               await content.response.send_message(content=f"Breakfast Data Entered. You have 2 points! Win more throughout the day.",ephemeral=True)
            else:
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=cursor.fetchone()
               await content.response.send_message(content=f"Breakfast Already Eaten. You have {points} points! Win more throughout the day.",ephemeral=True) 




    @discord.ui.button(label="Lunch Done",style=discord.ButtonStyle.red, custom_id="2")
    async def lunch(self, content:discord.Interaction,button:discord.ui.Button):
        if self.user==content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column={formatted_date} AND meal=\"Lunch\";")
            data=cursor.fetchone()
            if data==None:
               cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[1], "Lunch",2,formatted_date,formatted_time))
               mycon.commit()
               cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
               mycon.commit()
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=cursor.fetchone()
               await content.response.send_message(content==f"Lunch Data Entered. You have {points} points! Win more in dinner!",ephemeral=True)
            else:
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=cursor.fetchone()
               await content.response.send_message(content==f"Lunch Already Eaten. You have {points} points! Win more in dinner.",ephemeral=True) 
    
    @discord.ui.button(label="Dinner Done",style=discord.ButtonStyle.blurple, custom_id="3")
    async def dinner(self, content:discord.Interaction,button:discord.ui.Button):
        if self.user==content.user:
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime('%Y-%m-%d')
            formatted_time = current_datetime.strftime('%H:%M:%S')
            cursor.execute(f"SELECT * FROM history WHERE id={content.user.id} AND date_column={formatted_date} AND meal=\"Dinner\";")
            data=cursor.fetchone()
            if data==None:
               cursor.execute("INSERT INTO history VALUES (%s,%s,%s,%s,%s,%s)", (content.user.id, self.menu[2], "Dinner",2,formatted_date,formatted_time))
               mycon.commit()
               cursor.execute(f"UPDATE menu SET points=points+2 WHERE id={content.user.id}")
               mycon.commit()
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=cursor.fetchone()
               await content.response.send_message(content==f"Dinner Data Entered. You have {points} points! Win more tomorrow!",ephemeral=True)
            else:
               cursor.execute(f"SELECT points FROM menu WHERE id={content.user.id}")
               points=cursor.fetchone()
               await content.response.send_message(content==f"Dinner Already Eaten. You have {points} points! Win more tomorrow! ",ephemeral=True) 
            self.stop
@dietplan.error
async def on_dietplan_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.CommandOnCooldown):
        await interaction.response.send_message(str(error), ephemeral=True)

async def on_error(self, content: Interaction[client], error: Exception, item: Item[Any]):
      await self.message.edit(content="**Error Occured**\nPlease make sure:\n1. You and your friend are in a VC.\n2. The person being dragged has role permission to join the VC.\n3. Bot has required permissions.", view=None)
      self.stop()

@client.tree.command(name="leaderboard", description="Points")
async def finddocs(content: discord.Interaction):
        myEmbed1 = discord.Embed(title="Patzer Bot", description="**Leaderboard**\n1. Vijay (10 Points) 🥇\n2. Nandan Gondi (6 Points) 🥈\n3. Zarah (4 Points) 🥉\n4. Dhawal Arora (2 Points)",color=0x00ff00)
        await content.response.send_message(embed=myEmbed1, ephemeral=True)

@client.tree.command(name="finddocs", description="Get RWJ docs")
async def finddocs(content: discord.Interaction):
        cursor.execute(f"SELECT * FROM menu WHERE health!=\"Physically Fit\" AND id={content.user.id}")
        data=cursor.fetchone()
        if data!=None:
            doctors= get_docs(content.user.id)
            await content.response.send_message(content=f"{doctors}", ephemeral=True)
        else:
           await content.response.send_message(content="Please create a profile first/You are physically fit.", ephemeral=True) 


client.run(discordtoken)