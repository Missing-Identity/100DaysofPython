import requests
from newsapi import NewsApiClient
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

headline_line = ''
brief_line = ''

# All API Keys and Phone Numbers are removed for privacy. Please re-enter them later!

# News API Config
news_key = ""
newsapi = NewsApiClient(api_key=news_key)
news_url = "https://newsapi.org/v2/everything"
news_params = {
    'q': f"{COMPANY_NAME}",
    'apikey': news_key,
}
news_response = requests.get(news_url, params=news_params)
news_data = news_response.json()
# print(news_data)
headline = [0, 0, 0]
brief = [0, 0, 0]
for num in range(0, 3):
    headline[num] = f"{news_data['articles'][num]['title']}"
    brief[num] = f"{news_data['articles'][num]['description']}"

# Stock API Config
stock_key = ""
stock_url = ""
stock_function = "TIME_SERIES_DAILY"
stock_symbol = "TSLA"
stock_params = {
    'function': stock_function,
    'symbol': stock_symbol,
    'apikey': stock_key,
}
response = requests.get(url=stock_url, params=stock_params)
data = response.json()

# Twilio API Config
twilio_accid = ""
twilio_authtoken = ""
client = Client(twilio_accid, twilio_authtoken)


# Stock Data
data = data['Time Series (Daily)']
# print(data)
data_dates_list = list(data.keys())
stock_yesterday = data[data_dates_list[0]]
stock_day_before = data[data_dates_list[1]]
closing_yesterday = float(stock_yesterday['4. close'])
closing_day_before = float(stock_day_before['4. close'])
change = abs(closing_yesterday - closing_day_before)


# Function to send the 3 SMSs
def send_sms(index):
    global headline, brief, headline_line, brief_line, client
    headline_line = f"Headline-{index + 1}: {headline[index]}"
    brief_line = f"Brief-{index + 1}: {brief[index]}"
    message = client.messages \
        .create(body=f"{change_text}\n{headline_line}\n{brief_line}", from_='', to='')
    print(message.status)


# Checking for % change in stock price
if (closing_day_before - (5 / 100) * closing_day_before) < closing_yesterday < (closing_day_before + (5 / 100) *
                                                                                closing_day_before):
    print("Not a huge change. No SMS sent")
# If Stock Decreased
elif closing_yesterday < (closing_day_before - (5 / 100) * closing_day_before):
    # News Data
    perc_change = round((change/closing_day_before)*100, 2)
    change_text = f"{COMPANY_NAME}: 🔻{perc_change}%"
    print(change_text)
    for n in range(3):
        send_sms(n)
# If Stock Increased
else:
    # News Data
    perc_change = round((change / closing_day_before) * 100, 2)
    change_text = f"{COMPANY_NAME}: 🔺{perc_change}%"
    print(change_text)
    for n in range(3):
        send_sms(n)
