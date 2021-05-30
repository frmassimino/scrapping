import requests

api_key = ""
#url = "https://www.yelp.com/search?find_desc=&find_loc=Newport+Beach%2C+CA&ns=1"

#params = {
#    "location": "Newport Beach, CA"
#}

#url = "https://api.yelp.com/v3/businesses/search?"
#r = requests.get(url, params=params, headers={"Authorization": "Bearer {api_key}".format(api_key=api_key)})
#Bearer <number>
#print(r.text)

def do_search(term="food", location="Newport Beach, CA"):
    base_url = "https://api.yelp.com/v3/businesses/search?"
    #term = term.replace(" ", "+")
    #location = location.replace(" ", "+")
    #url = "{base_url}?term={term}&location={location}".format(
    #                base_url=base_url, 
    #                term=term, 
    #                location=location)
    params = {
        "term": term,
        "location": location
    }
    headers = {"Authorization": "Bearer {api_key}".format(api_key=api_key)}
    r = requests.get(base_url, params=params, headers=headers)
    return r.json()

search_1 = do_search()

for i in search_1["businesses"]:
    print(i["name"])
    print(i["phone"])
    print(i["location"]["display_address"])
    print(i["location"]["city"])
    print(i.get("location").get("area"))
    print("\n")

