{\rtf1\ansi\ansicpg1252\cocoartf2638
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import requests\
import datetime as dt\
import os\
\
# Date Data\
today_day = dt.datetime.now().strftime("%d")\
today_month = dt.datetime.now().strftime("%m")\
today_year = dt.datetime.now().strftime("%Y")\
today_date = f"\{today_day\}/\{today_month\}/\{today_year\}"\
today_time = dt.datetime.now().strftime("%X")\
\
# Nutritiontionix Data\
nutritionix_app_id = os.environ['NUTRI_APP_ID']\
nutritionix_app_key = os.environ['NUTRI_APP_KEY']\
nutritionix_endpoint = os.environ['NUTRI_ENDPOINT']\
nutritionix_headers = \{\
    "x-app-id": nutritionix_app_id,\
    "x-app-key": nutritionix_app_key,\
\}\
\
# Sheety API Data\
sheety_project_name = os.environ['SHEETY_NAME']\
sheety_project_sheet = os.environ['SHEETY_SHEET']\
sheety_app_key = os.environ['SHEETY_KEY']\
sheety_endpoint = f"https://api.sheety.co/\{sheety_app_key\}/\{sheety_project_name\}/\{sheety_project_sheet\}"\
\
# User Input Data\
query = input("Enter your workout session today:\\n")\
gender = input("Enter your gender: male or female: \\n").lower()\
weight = float(input("Enter your weight:\\n"))\
height = float(input("Enter your height in cm:\\n"))\
age = int(input("Enter your age:\\n"))\
\
# Nutritionix Params\
nutritionix_params = \{\
    "query": query,\
    "gender": gender,\
    "weight_kg": weight,\
    "height_cm": height,\
    "age": age,\
\}\
\
sheety_headers = \{\
    "Authorization": os.environ['SHEETY_HEADER']\
\}\
\
response_nutritionix = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)\
\
for list_item in response_nutritionix.json()['exercises']:\
    exercise = list_item['user_input']\
    duration_of_exercise = list_item['duration_min']\
    calories_burnt = list_item['nf_calories']\
    sheety_data = \{\
        "workout": \{\
            "date": f"\{today_date\}",\
            "time": f"\{today_time\}",\
            "exercise": exercise.title(),\
            "duration": duration_of_exercise,\
            "calories": calories_burnt,\
        \}\
    \}\
    response = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)\
    print(response.json())\
\
print(response_nutritionix.json())}