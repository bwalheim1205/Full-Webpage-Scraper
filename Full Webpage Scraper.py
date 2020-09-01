#--------------------------------------------------
#Website Search
#
#Searchs Website on every page for every instance of a word
#
#Author: Brian Walheim
#Version: 1.0.0
#--------------------------------------------------

#----------------
# Imports
#----------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser

#----------------
# Variables
#----------------

#Array that holds all pages
pages = []
count = 0

#-----------------
# Functions
#-----------------

#Recursive Search Function
#   Finds every link off main webpage and than searches those pages

def extendedHTMLSearch(url, element):
    global pages

    #Gets data from url
    r = urlopen(url)
    soup = BeautifulSoup(r.text)

    #Does something with page
    
    #Searches and iterates over all links on page
    for link in soup.find_all('a'):
        
        #Checks if page is in links
        if not (link in pages):
            pages.append(link)

            #Recursive Call
            extendedHTMLSearch(url, element)

