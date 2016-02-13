# exploringTwilioAPI

This is my Django project where I'm both doing a technical coding challenge as well as explore some of the other functionalities of the Twilio API.

## Requirements have to be downloaded and can be found in requirements.txt
* twilio==5.3.0
* django-twilio==0.8.0
* Django==1.9
* If I am missing any, please let me know! I have them installed locally but may have forgotten to put here.

Install requirements via: `sudo pip install -r requirements.txt`

Run `python manage.py runserver`

Tested live using ngrok
`ngrok http 8000`

ngrok server url will have to be put in 2 locations:
* angular app requests
* django views

## Endpoints:

### Making calls
* /call_someone/
* /make_previous_call/

### SMS (did this for fun, put in repo b/c why not)
* /sms/

### Call response 
* /ring/

### Handling call response
* /response/

### Replay response
* /replay/

### Get past call history
* /get_previous_calls/


