# from twilio.rest import TwilioRestClient
import os
# import logging
import json
import requests


# def load_twilio_config():
#     twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
#     twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
#     twilio_number = os.environ.get('TWILIO_NUMBER')
#
#     if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
#         logger.error(NOT_CONFIGURED_MESSAGE)
#         raise MiddlewareNotUsed
#
#     return (twilio_number, twilio_account_sid, twilio_auth_token)


def getWeatherInfo(latitude, longitude):
    apiKey = getApiKey('darkSky')
    unit = 'si'
    url = 'https://api.darksky.net/forecast/{0}/{1},{2}?units={3}'.format(
        apiKey, latitude, longitude, unit
    )
    r = requests.get(url)
    return r.json()


def temperatureToWords(temp):
    tempWords = []
    for t in temp:
        if (float(t) <= -31):
            tempWords.append('I would not recommend that you go out.')
        elif (-10 < float(t) < -30):
            tempWords.append('freezing cold. You should wear a jacket')
        elif (0 < float(t) < 15):
            os.system('say {0}'.format('cold'))
            tempWords.append('cold')
        elif (15 < float(t) < 20):
            tempWords.append('warm, Room indoors')
        elif (20 < float(t) < 25):
            tempWords.append('warm, Warm room')
        elif (25 < float(t) < 30):
            tempWords.append('Hot day')
        elif (30 < float(t) < 37):
            tempWords.append('Very Hot, Body temperature')
        elif (37 < float(t) < 40):
            tempWords.append(
                'Very Hot, Washing machine setting for clothes for normal wash'
            )
        elif (40 < float(t) < 50):
            tempWords.append('Extremely hot')
    return tempWords


def getHourly(Json):
    weatherTemperature = []
    for i in range(len(Json['hourly']['data'])):
        weatherTemperature.append(Json['hourly']['data'][i]['temperature'])
    return weatherTemperature


def getApiKey(key):
    data = ''
    with open('apiKeys.json') as data_file:
        data = json.load(data_file)
    return data['api'][key]


def sendSMS(phoneNumbers):
    pass


def main():
    latitude = '45.4215'
    longitude = '-75.6972'
    hourlyData = getHourly(getWeatherInfo(latitude, longitude))
    print temperatureToWords(hourlyData)


if __name__ == '__main__':
    main()
