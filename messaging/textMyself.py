## Defines the textmyself() function that texts a message passed to it as a string.

accountSID = 'ACxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxx'
myNumber = 'xxxxxxxxxxxxxx'
twilioNumber = 'xxxxxxxxxxxxx'

from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)