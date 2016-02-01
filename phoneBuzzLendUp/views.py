from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response


def home(request):
    return render(request, 'home.html')


@twilio_view
def sms(request):
    name = request.POST.get('Body', '')
    msg = 'Hey %s, how are you today?' % (name)
    r = Response()
    r.message(msg)
    return r
