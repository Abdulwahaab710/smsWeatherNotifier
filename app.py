from twilio.rest import TwilioRestClient
# import os
# import logging
import json
import requests


def sendSMS(phoneNumbers, latitude, longitude):
    '''(list) -> bool
    '''
    phoneNumbers = '+16135013175'
    smsBody = temperatureToWords(
        getWeatherInfo(latitude, longitude)
    )
    token = getToken()
    client = TwilioRestClient(token[0], token[1])
    client.messages.create(from_=phoneNumbers,
                           to=phoneNumbers,
                           body=smsBody)


def getWeatherInfo(latitude, longitude):
    '''(str, str) -> (dict)'''
    apiKey = getApiKey('darkSky')
    unit = 'si'
    url = 'https://api.darksky.net/forecast/{0}/{1},{2}?units={3}'.format(
        apiKey, latitude, longitude, unit
    )
    r = requests.get(url)
    return r.json()


def temperatureToWords(temp):
    '''(list) -> (list)

    '''
    tempWords = []
    for t in temp:
        if (float(t) <= -31):
            tempWords.append('I would not recommend that you go out.')
        elif (-10 < float(t) < -30):
            tempWords.append('freezing cold. You should wear a jacket')
        elif (0 < float(t) < 15):
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
    '''(dict) -> (list)
    '''
    weatherTemperature = []
    for i in range(len(Json['hourly']['data'])):
        weatherTemperature.append(Json['hourly']['data'][i]['temperature'])
    return weatherTemperature


def getApiKey(key):
    '''(str) -> (str)'''
    try:
        data = ''
        with open('apiKeys.json') as data_file:
            data = json.load(data_file)
        return data['api'][key]
    except KeyError:
        print 'invalid key, or the key doesn\'t exists'
        exit()
    except IOError:
        print 'invalid file name, or the file doesn\'t exists'
        exit()


def getToken():
    try:
        data = ''
        with open('apiKeys.json') as data_file:
            data = json.load(data_file)
        return [data['token']['TWILIO_ACCOUNT_SID'],
                data['token']['TWILIO_AUTH_TOKEN']]
    except KeyError:
        print 'invalid key, or the key doesn\'t exists'
        exit()
    except IOError:
        print 'invalid file name, or the file doesn\'t exists'
        exit()


def checkIfRainingOrSnowing(Json):
    pass


def main():
    # latitude = '45.4215'
    # longitude = '-75.6972'
    # hourlyData = getHourly(getWeatherInfo(latitude, longitude))
    # print temperatureToWords(hourlyData)
    pass


if __name__ == '__main__':
    main()
