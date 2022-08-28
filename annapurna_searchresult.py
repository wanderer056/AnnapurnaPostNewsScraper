from nepali_unicode_converter.convert import Converter
import requests
import json

#To convert Roman into Nepali Word for Searching
converter = Converter()
search_string = 'koronaa'

np_search_string = converter.convert(search_string)
print(np_search_string)
##################################################
pagesToscrape = 5

#For intial storing 100 in the next_page so that it can be used as a testing condition for initializing beg_page. If 100 new beginnig page will be initialized else the next_page link retrieved from the search query json will be used
f = open("next_page.txt","r", encoding="utf-8")
test = f.read()
f.close()

if test == "100":

    beg_page = "https://bg.annapurnapost.com/api/search?title=" + np_search_string
    print("Beginning Page:  {}".format(beg_page))

    f = open("next_page.txt","w", encoding="utf-8")
    f.write(beg_page)
    f.close()

#########################################################################

news_list =[]
i=0

while True:

    #Reading URL from next_page.txt for first request. AnnapurnaPost API is used for Scraping
    f = open("next_page.txt","r",encoding="utf-8")
    url = f.read()
    f.close()
    print(url)

    ###################################################

    #Making full URL for scraping

    try:
        i=i+1
        response =  requests.get(url) # Gets 10 articles json data from the first page when run for first time

    except:
        ###If it is request error at page 1 then when again running the script it runs from page 2.
        next_page =  "https://bg.annapurnapost.com/api/search?page={}&title=".format(str(i+1)) + np_search_string
        f = open("next_page.txt","w",encoding="utf-8")
        f.write(next_page)
        f.close()

    data = json.loads(response.text)

    #Getting the search result and storing filtered news in news_list
    for news in data["data"]["items"]:
        news_list.append(news)


    next_page_api_link = data["data"]["links"]["next"] ## Got from the search result json
    next_page_to_scrape = "https://bg.annapurnapost.com" + next_page_api_link


    #Writing the next page link to scrape to a file
    f = open("next_page.txt","w",encoding="utf-8")
    f.write(next_page_to_scrape)
    f.close()

    pagesToscrape = pagesToscrape - 1
    # time.sleep(2)
    if pagesToscrape==0:
        break


json_object = json.dumps(news_list, indent=4)

#Writing to sample.json
with open("news1.json","w") as outfile:
    outfile.write(json_object)