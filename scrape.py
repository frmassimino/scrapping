import requests
from bs4 import BeautifulSoup

base_url = 'https://www.yelp.com/search?find_desc=&find_loc='
loc = 'Newport Beach, CA'
#page = 10
current_page = 0

while current_page < 51:
    print(current_page)
    url = base_url + loc + "&start=" + str(current_page)
    yelp_r = requests.get(url)
    yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')
    businesses = yelp_soup.findAll('div', {'class':'lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT'})
    file_path = 'yelp_{loc}-2.txt'.format(loc=loc)
    with open(file_path, "a") as textfile:
        businesses = yelp_soup.findAll('div', {'class':'lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT'})
        for biz in businesses:
            try:
                title = biz.findAll('a',{'class': 'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})
                title = title[0].text
            except:
                title = None
            print(title)
            try:
                address = biz.findAll('address',{'class': 'lemon--address__373c0__2sPac'})
                for item in address:
                    if "br" in str(item):
                        print(item.getText())
                    else:
                        print(str(item).strip(" \n\t\r"))
                address = address[0].text
            except:
                address = None
            print(address)
            try:
                phone = biz.findAll('p', {'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})
                phone = phone[0].text
            except:
                phone = None
            print(phone)
            page_line = "Title: {title}\nAddress: {address}\nPhone: {phone}\n\n".format(
                title=title, 
                address=address, 
                phone=phone)
            textfile.write(page_line)
        
    
    
    current_page += 10
#url = base_url + loc + "&start=" + str(page)


#yelp_r = requests.get(url)
#print(yelp_r)

#yelp_soup = BeautifulSoup(yelp_r.text, 'html.parser')

#print(yelp_soup.prettify())

#print(search_soup)

#for link in search_soup:
#    print(link)

#businesses = yelp_soup.findAll('div', {'class':'lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT'})
#for biz in businesses:
    #title = biz.findAll('a',{'class': 'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})
    #if len(title) > 0:
        #print(title[0].text)
    #title = biz.findAll('address',{'class': 'lemon--address__373c0__2sPac'})
    #if len(title) > 0:
        #print(title[0].text)
    #title = biz.findAll('p', {'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})
    #if len(title) > 0:
        #print(title[0].text)
    #print('\n')


#file_path = 'yelp_{loc}.txt'.format(loc=loc)
#with open(file_path, "a") as textfile:
#    businesses = yelp_soup.findAll('div', {'class':'lemon--div__373c0__1mboc arrange__373c0__UHqhV border-color--default__373c0__2oFDT'})
#    for biz in businesses:
#        title = biz.findAll('a',{'class': 'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'})
#        if len(title) > 0:
#            print(title[0].text)
#            title = title[0].text
#        address = biz.findAll('address',{'class': 'lemon--address__373c0__2sPac'})
#        if len(address) > 0:
#            print(address[0].text)
#            address = address[0].text
#        phone = biz.findAll('p', {'class': 'lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7'})
#        if len(phone) > 0:
#            print(phone[0].text)
#            phone = phone[0].text
#        page_line = "Title: {title}\nAddress: {address}\nPhone: {phone}\n\n".format(
#            title=title, 
#            address=address, 
#            phone=phone)
#        textfile.write(page_line)


#print(yelp_soup.findAll('li', {'class': 'lemon--li__373c0__1r9wz border-color--default__373c0__2oFDT'}))
#print(yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'}))

#for name in yelp_soup.findAll('a', {'class':'lemon--a__373c0__IEZFH link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5'}):
    #print(name.text)



