import os

# third party imports
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
from twilio.twiml import Response
from rest_framework import status
from rest_framework.response import Response as reply
from rest_framework.decorators import api_view

# local imports


@api_view(['GET', 'POST'])
def call_someone(request):
    account_sid = "ACc1819dbc489da5fae3d3506847e06ed3"
    auth_token = "2f238a6ad9f1670f888dbde2337d4101"
    client = TwilioRestClient(account=account_sid, token=auth_token)

    call = client.calls.create(url="http://79b2b7dd.ngrok.io/ring/",
        to="+15713869605",
        from_="+15712817232")
    return reply('Call placed! Please hold.', status=status.HTTP_200_OK)


@twilio_view
def sms(request):
    name = request.POST.get('Body', '')
    print name
    msg = 'Hey %s, how are you today?' % (name)
    r = Response()
    r.message(msg)
    return r


@twilio_view
def ring(request):
    twilio_response = Response()
    message = 'Welcome to Fizz Buzz! Press up to three digits to start playing.'
    with twilio_response.gather(action='/respond/', numDigits=3) as g:
        g.say(message)
        g.pause(length=1.5)
        g.say(message)

    return twilio_response


@twilio_view
def handle_response(request):

    digits = request.POST.get('Digits', '')
    calling_to = request.POST.get('To', '')
    call_sid = request.POST.get('CallSid', '')
    twilio_response = Response()

    return_message = get_fizzbuzz_message(int(digits))

    # if digits == '1':
    #     twilio_response.play('http://bit.ly/phaltsw')
    #
    # if digits == '2':
    #     number = request.POST.get('From', '')
    #     twilio_response.say('A text message is on its way')
    #     twilio_response.sms('You looking lovely today!', to=number)

    twilio_response.say(return_message)
    twilio_response.redirect('/ring/')
    return twilio_response


def get_fizzbuzz_message(number):
    return_message = ""
    if number % 5 == 0 and number % 3 == 0:
        return_message = "Fizz Buzz "
    elif number % 5 == 0:
        return_message = "Buzz "
    elif number % 3 == 0:
        return_message = "Fizz "
    else:
        return_message = str(number) + " "
    return return_message

