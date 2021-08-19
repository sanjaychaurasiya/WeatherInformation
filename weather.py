import requests
import smtplib
import email_pass_api_key as ep


# My latitude and longitude and api key and emails to send the list of email to send mail.
MY_LAT = ep.MY_LAT
MY_LONG = ep.MY_LONG
API_KEY = ep.WEATHER_API_KEY
GMAILS = [ep.MY_EMAIL, ep.EMAIL]

parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'exclude': "current,minutely,daily,alerts"
}
response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
data = response.json()['hourly'][0:12]

rain = False

for j in data:
    a = j['weather'][0]['id']
    if a > 700:
        rain = True

if rain:
    with smtplib.SMTP('smtp.gmail.com') as smtp:
        smtp.starttls()
        smtp.login(
            user=ep.EMAIL,
            password=ep.PASSWORD,
        )
        for gmail in GMAILS:
            smtp.sendmail(
                from_addr=ep.EMAIL,
                to_addrs=ep.MY_EMAIL,
                msg='Subject: Rain \n\nBring Umbrella, it might be rain today.'
            )
            