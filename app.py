# from twilio.rest import TwilioRestClient
# import os
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
    print getWeatherInfo(latitude, longitude)


if __name__ == '__main__':
    main()
