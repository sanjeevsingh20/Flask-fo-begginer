from twilio.rest import Client
import keys
import random

client= Client(keys.account_sid,keys.auth_token)
num=random.randint(1000,10000)
message = client.messages.create(
    body="Your OTP for URS Account is %s" %num,
    from_= keys.twilio_number,
    to= keys.target_number
    )

print(message.body)