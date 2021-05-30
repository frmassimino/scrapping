import email
import imaplib #imap pop
from bs4 import BeautifulSoup

import os
import mimetypes

username = ""
password = ""

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username,password)
print(mail)

mail.select("inbox")

#create new folder
mail.create("Items2")

#list folders
mail.list()

result, data = mail.uid('search', None, "ALL")

inbox_item_list = data[0].split()

most_recent = inbox_item_list[-1]

oldest = inbox_item_list[0]

for item in inbox_item_list:
    result2, email_data = mail.uid("fetch", oldest, '(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    email_message = email.message_from_string(raw_email)
    to_ = email_message['To']
    from_ = email_message['From']
    subject_ = email_message['Subject']
    counter = 1
    for part in email_message.walk():
        if part.get_content_maintype() == "multipart":
            continue
        filename = part.get_filename()
        if not filename:
            ext = '.html'
            filename = 'nsg-part-%08d%s' %(counter,ext)
        counter += 1

"""
save file
"""
content_type = part.get_content_type()
print(subject_)
print(content_type)


#email_message.get_payload()


#for item in inbox_item_list:
#    resulr2, email_data = mail.iud('fetch', item, '(RFC822)')
#    raw_email = email_data[0][1].decode("utf-8")
#    email_message = email.message_from_string(raw_email)

