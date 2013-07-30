"""
Downloads the NYC Subway data from MTA's website
"""

#-----------------------------------------------------------------#
import urllib
import os
# http://www.crummy.com/software/BeautifulSoup/
from bs4 import BeautifulSoup

#-----------------------------------------------------------------#
"""
Crawl MTA Fare Data url, download all the fare data and store all 
the files in the 'fare_data' directory on local machine. 
"""
def download_data():
    
    # Create a 'fare_data' directory on local machine
    # where all csv files will be downloaded
    dir_name = 'fare_data'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    # Get contents of the webpage
    url = 'http://mta.info/developers/fare.html'
    source = urllib.urlopen(url).read()
    soup = BeautifulSoup(source)
    
    # Extract all csv file links from anchor tags
    url_prefix = 'http://mta.info/developers/'
    csv_links = []
    for tag in soup.find_all('a'):
        if '.csv' in str(tag):
            csv_links.append(url_prefix + str(tag.get('href')))

    # Download the csv files and store them in 'farw_data' directory
    print "\nDownloading files, just wait a few minutes bro"
    for link in csv_links:
        filename = dir_name + '/' + link.split('/')[-1] # split the file name from url
        if not os.path.exists(filename):
            urllib.urlretrieve(link, filename)
    print "\nGo check the " + dir_name + " directory now"

#-----------------------------------------------------------------#
if __name__ == '__main__':
    download_data()

#-----------------------------------------------------------------#