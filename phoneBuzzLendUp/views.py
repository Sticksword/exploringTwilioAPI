# standard library imports
import sched
import time

# third party imports
from django_twilio.decorators import twilio_view
from twilio.rest import TwilioRestClient
from twilio.twiml import Response
from django.http import HttpResponse

# local imports
from settings import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN # gotta put into bash profile and restart laptop
from api import *
s = sched.scheduler(time.time, time.sleep)


def call_someone(request):
    to_number = request.GET['to_number']
    time_delay = int(request.GET['time_delay'])
    s.enter(time_delay, 1, make_call, (to_number, time_delay))
    print s.queue
    s.run()
    print s.queue
    return HttpResponse("Great success! Your call has been placed in queue.")


def make_call(to_number, time_delay=0):
    account_sid = "ACc1819dbc489da5fae3d3506847e06ed3"
    auth_token = "2f238a6ad9f1670f888dbde2337d4101"
    # account_sid = TWILIO_ACCOUNT_SID
    # auth_token = TWILIO_AUTH_TOKEN
    client = TwilioRestClient(account=account_sid, token=auth_token)

    to_number = "+1" + str(to_number)
    print to_number
    try:
        call = client.calls.create(url="http://4bff4f94.ngrok.io/ring/",
                                   to=to_number,
                                   from_="+15712817232")
        print call
        save_call_record(to_number, call.sid, "+15712817232", time_delay)
    except Exception as e:
        print "An error has occurred in 'make_call()'."


def make_previous_call(request):
    call_id = request.GET['id']
    call_object = Calls.objects.get(pk=call_id)
    to_number = call_object.to_number
    digits_entered = call_object.digits_entered
    account_sid = "ACc1819dbc489da5fae3d3506847e06ed3"
    auth_token = "2f238a6ad9f1670f888dbde2337d4101"
    client = TwilioRestClient(account_sid, auth_token)

    try:
        call = client.calls.create(to=to_number,
                                   from_="+15712817232",
                                   url="http://4bff4f94.ngrok.io/replay/?digits="+str(digits_entered))
        save_call_record(to_number, call.sid, "+15712817232")
        update_call_record(to_number, call.sid, digits_entered)
        return HttpResponse('Dialing previous call successful!')
    except Exception as e:
        return HttpResponse('ERROR dialing previous call.')


def get_previous_calls(request):
    data = get_all_previous_calls()
    return HttpResponse(data, content_type="application/json")


@twilio_view
def handle_replay_message(request):
    digits = request.GET['digits']
    msg = get_fizzbuzz_message(int(digits))

    twilio_response = Response()
    twilio_response.say(msg)
    return twilio_response


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
    with twilio_response.gather(action='/response/', numDigits=3) as g:
        g.say(message)
        g.pause(length=1.5)
        g.say(message)
    return twilio_response


@twilio_view
def handle_response_message(request):

    digits = request.POST.get('Digits', '')
    to_number = request.POST.get('To', '')
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
    update_call_record(to_number, call_sid, str(digits))
    twilio_response.redirect('/ring/')
    return twilio_response

