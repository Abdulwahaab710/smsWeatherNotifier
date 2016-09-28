from twilio.rest import TwilioRestClient
import os
import logging
import json

def load_twilio_config():
    twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    twilio_number = os.environ.get('TWILIO_NUMBER')

    if not all([twilio_account_sid, twilio_auth_token, twilio_number]):
        logger.error(NOT_CONFIGURED_MESSAGE)
        raise MiddlewareNotUsed

    return (twilio_number, twilio_account_sid, twilio_auth_token)

def getWeatherInfo(city):
    pass

def sendSMS(phoneNumbers):
    pass

def main():
    pass

if __name__ == '__main__':
    main()
