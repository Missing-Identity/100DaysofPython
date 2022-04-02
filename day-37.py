import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "sdfsdfswer475346thjdfgv",
    "username": "ogprime",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# Create user on Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create Graph
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Code Graph",
    "unit": "Days",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": user_params['token'],
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

today = dt.datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),  # Formatting date to match API needs
    "quantity": "1",
}

# Posting Pixel to our created graph
response = requests.post(url=f"{graph_endpoint}/{graph_config['id']}", json=pixel_config, headers=headers)
print(response)

update_config = {
    "quantity": "2",
}

# Update Pixel
response = requests.put(url=f"{graph_endpoint}/{graph_config['id']}/{pixel_config['date']}", json=update_config,
                        headers=headers)

# Delete Pixel
delete = requests.delete(url=f"{graph_endpoint}/{graph_config['id']}/{pixel_config['date']}", headers=headers)
print(response)
print(delete)
