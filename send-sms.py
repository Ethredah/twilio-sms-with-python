
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "-enter-account-sid-"
# Your Auth Token from twilio.com/console
auth_token  = "-enter-auth-token-"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+25400000002", #enter destination number
    from_="+12028042921", #enter sms number
    body="Greeting from Python ;)")
    #url = "https://studio.twilio.com/v1/Flows/FW7836fdba833fd6b70a30927f9d75586b/Engagements"

#call = client.calls.create(
#    to="+25400000001",
#    from_="+12028042921",
#    url="http://demo.twilio.com/docs/voice.xml")

#print(call.sid)

print(message.sid)
