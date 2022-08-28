###Simple News Scraper from the Annapurna Post
At first the search term is converted to nepali. And request is sent to the Annapurn Post API which returns the search result in json file.
It uses Annapurn Post API for scraping.
The search result in json format is stored in news1.json. Multiple pages to scrape can be set on the annapurna_searchresults.py script given by the pagesToScrape.

To get individual news data, the id of the news article can be used. The single news article can be scraped as shown in get_individual_news_data.py which is stored in the singlenews.json, this can be run in loop to get multiple individual news articles.

In the next_page.txt value 100 is set at first which initializes the beginning scraping page. Afterwards, the link in the query is followed and updated in the next_page.txt