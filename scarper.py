"""
Author: T.Mohan Sri Sai
scraper.py is used to scarp the urls of the maximum sites
"""
from urllib.request import urlopen
import re

# Here we specify the url of the website you want to scrap
url = "https://news.ycombinator.com/"  # url


# here is the function to create a file
def create_file(string):
    string = str(string)
    f = open("urls.txt", "w")
    f.write(string)
    f.close()


# function to sort the scraped data
def sorting(file):
    # Specify the html tag that you want to sort
    s_file1 = re.findall("<a href=\".*\" class=\"titlelink\">", file, re.IGNORECASE)  # HTML tag
    s_file2 = str(s_file1)
    # Slicing URLs from scraped data using Regex
    s_file2 = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", s_file2)
    title = " \n".join(map(str, s_file2))
    create_file(title)


# Function to decode the Url and Sort data
def url_decode(link):
    page = urlopen(link)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    sorting(html)


# Calling function
url_decode(url)
