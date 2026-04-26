import json
import openai
from config import OPENAI_API_KEY
from database import cursor

openai.api_key = OPENAI_API_KEY

LOCATION_FILES = {
    "Livingston":    ("data0.json",  "data1.json",  "data2.json"),
    "Busch":         ("data3.json",  "data4.json",  "data5.json"),
    "Cook-Douglass": ("data6.json",  "data7.json",  "data8.json"),
    "College Ave":   ("data9.json",  "data10.json", "data11.json"),
}

DISEASE_REQUIREMENTS = {
    "Hypertension":    "requirements per day for hypertension - potassium:3400mg men, 2600mg women; sodium(max amount): 1500mg men, 1560mg women; calcium:1250mg; protein:102g; magnesium: 500mg; fiber:30g; saturatedFat(max):14g",
    "Diabetes":        "requirements per day for diabetes - calories:2500 men,2000 women; carbs:343.75g men,275g women;fat(max):83.33g men, 66.67g women;protein:62.5g men,50g women;sugar(max):31.25g men,25g women",
    "Menstrual Cycle": "requirements per day for menstrualCycle - carbs:225g, fat:56g, protein:150g, iron:18mg",
    "Physically Fit":  "requirements per day for generally physically fit people - carbs:300g men,260g women; protein:55g men,50g women; sugars(max):120g men,90g women; fat:95g men,70g women; saturatedFat(max):30g men,20g women",
}

_SYSTEM_PROMPT = "You are an assistant that gives nutritional advice to students based on input menus from campus dining halls"


def _get_meal_plan(meal_data, meal_name, user_input, disease_info):
    conversation = [{"role": "system", "content": _SYSTEM_PROMPT}]
    conversation.append({
        "role": "user",
        "content": (
            str(meal_data)
            + f"This is todays {meal_name} menu for dining hall. Give me a diet plan along with the number of servings for todays {meal_name} based on the following user preferences, user data and disease data"
            + user_input
            + " "
            + disease_info
        ),
    })
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)
    return response['choices'][0]['message']['content'].strip("\n").strip()


def DietPlanner(user_id, location):
    breakfast_file, lunch_file, dinner_file = LOCATION_FILES[location]
    with open(breakfast_file) as f:
        breakfast_data = json.load(f)
    with open(lunch_file) as f:
        lunch_data = json.load(f)
    with open(dinner_file) as f:
        dinner_data = json.load(f)

    cursor.execute(f"SELECT diet FROM menu WHERE id={user_id};")
    dietary_restriction = cursor.fetchone()
    cursor.execute(f"SELECT health FROM menu WHERE id={user_id};")
    health_condition = cursor.fetchone()
    cursor.execute(f"SELECT goals FROM menu WHERE id={user_id};")
    goals = cursor.fetchone()
    cursor.execute(f"SELECT gender FROM menu WHERE id={user_id};")
    gender = cursor.fetchone()
    cursor.execute(f"SELECT weight FROM menu WHERE id={user_id};")
    weight = cursor.fetchone()
    cursor.execute(f"SELECT height FROM menu WHERE id={user_id};")
    height = cursor.fetchone()
    cursor.execute(f"SELECT age FROM menu WHERE id={user_id};")
    age = cursor.fetchone()

    user_input = "dietary restriction:{}, health condition:{}, goals:{}, gender:{}, weight:{}, height:{}, age:{}".format(
        dietary_restriction, health_condition, goals, gender, weight, height, age
    )
    disease_info = DISEASE_REQUIREMENTS[health_condition[0]]

    breakfast_plan = _get_meal_plan(breakfast_data, "breakfast", user_input, disease_info)
    lunch_plan     = _get_meal_plan(lunch_data,     "lunch",     user_input, disease_info)
    dinner_plan    = _get_meal_plan(dinner_data,    "dinner",    user_input, disease_info)

    return [
        f"{location} Breakfast: {breakfast_plan}",
        f"{location} Lunch: {lunch_plan}",
        f"{location} Dinner: {dinner_plan}",
        f"{location} Dining Hall:\n\nBreakfast: {breakfast_plan}\n\nLunch: {lunch_plan}\n\nDinner: {dinner_plan}",
    ]
