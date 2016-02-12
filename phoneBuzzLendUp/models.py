from django.db import models


class Calls(models.Model):
    call_sid = models.CharField(max_length=34)
    time_called = models.DateTimeField(auto_now_add=True)
    time_delay = models.IntegerField(null=True, blank=True)
    to_number = models.CharField(max_length=15) # apparently max digits for any call is recommended 15 digits
    from_number = models.CharField(max_length=15, null=True, blank=True)
    digits_entered = models.CharField(max_length=100, null=True, blank=True)