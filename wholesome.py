from twilio.rest import Client
# put your own credentials here
account_sid = "AC070d0d1d712b8fc504d882d2156cfe43"
auth_token = "48c0bf4956d664830b9c7177196c9496"
client = Client(account_sid, auth_token)
client.messages.create(
  to="+15103871565",
  from_="+14159414110 ",
  body="Hey Mike! Hope you're doing well. Stay chillin!",
  media_url="http://www.clipartmasters.com/clip-arts/235/happy-smile-235818.png")