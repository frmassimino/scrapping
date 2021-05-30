import requests
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

to="" 
from_=""
body="Mensaje con cliente y multimedia\n"
media_url = ""

client = Client(account_sid, auth_token)

def send_message_client(client, to, from_, body, media_url):
    message = client.messages.create(
        to=to, 
        from_=from_,
        body=body,
        media_url=[media_url])
    print(dir(message))
    print(message.sid)
    print(message.media)
    print(message.status)

#send_message_client(client, to=to, from_=from_, body=body, media_url=media_url)
message_data = client.messages.get(sid='').fetch()
print(message_data.status)

image_list = [i.uri for i in message_data.fetch().media.list()]
print(image_list)


def xml_pretty(xml_string):
    import xml.dom.minidom
    xml = xml.dom.minidom.parseString(xml_string)
    pretty_xml_ = xml.toprettyxml()
    print(pretty_xml_)

base_url = "https://api.twilio.com/2010-04-01/Accounts"
message_url = base_url + "/{AccountSid}/Messages".format(AccountSid=account_sid)
auth = (account_sid, auth_token)

data = {
    "To": to,
    "From": from_,
    "Body": body,
    "MediaUrl": ""
}

#r = requests.post(message_url, auth=auth, data=data)

#print(r.status_code)
#xml_pretty(r.text)

#message_url_ind = message_url + "/MM0389a75d24ea4fafbe422e900cb36dbe"
#get_r = requests.get(message_url_ind, auth=auth)

#xml_pretty(get_r.text)