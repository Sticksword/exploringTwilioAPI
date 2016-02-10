from django.core import serializers
from models import Calls
from django.http import HttpResponse


def save_call_record(to_number, call_sid, from_number=None, time_delay=0):
    try:
        call_record = Calls(to_number=to_number, call_sid=call_sid, from_number=from_number, time_delay=time_delay)
        call_record.save()
        print call_record.id,' record saved!'
    except Exception as e:
        print 'exception in saving call record, ', e


def update_call_record(to_number, call_sid, digits):
    try:
        call_record = Calls.objects.get(call_sid=call_sid, to_number=to_number)
        if call_record.digits_entered is None:
            call_record.digits_entered = digits
        else:
            call_record.digits_entered = call_record.digits_entered + digits
        call_record.save()
        print call_record.id, 'record updated with digits pressed'
    except Exception as e:
        print 'exception in updating call record', e