from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey dude, Where is my food?",
    to="+14153099911",    # Replace with your phone number
    from_="+15306014119") # Replace with your Twilio number
print message.sid
