import requests
import cv2

cap = cv2.VideoCapture(1)

while(True):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    cv2.imwrite("captured_image.jpg", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

# Nutritionix Data
nutritionix_app_id = "72c83243"
nutritionix_app_key = ""
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
nutritionix_headers = {
    "x-app-id": nutritionix_app_id,
    "x-app-key": nutritionix_app_key,
}

# LogMeal API Data
logmeal_app_user_token = ""
logmeal_headers = {'Authorization': 'Bearer ' + logmeal_app_user_token}
logmeal_endpoint = 'https://api.logmeal.es/v2/recognition/dish'

# Sheety API Data
sheety_project_name = "foodRecognitionUsingImageProcessingData"
sheety_project_sheet = "sheet1"
sheety_app_key = ""
sheety_endpoint = f"https://api.sheety.co/{sheety_app_key}/{sheety_project_name}/{sheety_project_sheet}"

# Sheety Header Token
sheety_headers = {
    "Authorization": "Bearer "
}

# Image Input Data
img = 'captured_image.jpg'
response_logmeal = requests.post(logmeal_endpoint, files={'image': open(img, 'rb')},
                                 headers=logmeal_headers)
print(response_logmeal.json()) 
query = response_logmeal.json()

# Received Food Data
food_name = query['recognition_results'][0]['name'].title()
food_family = query['foodFamily'][0]['name'].title()
food_prediction_accuracy = query['recognition_results'][0]['prob']
print(food_family)
print(food_name)
print(food_prediction_accuracy)

# Nutritionix Params
nutritionix_params = {
    "query": food_name
}

# Nutritionix Response
response_nutritionix = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
print(response_nutritionix.json())
response_nutritionix_data = response_nutritionix.json()['foods'][0]
calorie_count = response_nutritionix_data['nf_calories']

# Sheety Data
sheety_data = {
    "sheet1": {
        "food": food_name,
        "family": food_family,
        "accuracy": food_prediction_accuracy,
        "calories": calorie_count
    }
}

response_sheety = requests.post(url=sheety_endpoint, json=sheety_data, headers=sheety_headers)
print(response_sheety.json())
