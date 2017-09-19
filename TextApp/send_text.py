from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2f39a096be24b25294f9a240e16728c2"
# Your Auth Token from twilio.com/console
auth_token  = "youwish"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16502700968",
    from_="+16502482103",
    body="Hello from Python!")

print(message.sid)
