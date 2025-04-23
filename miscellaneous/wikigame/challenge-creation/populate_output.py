#!/usr/bin/python3

#thequickbrowndogoverjumpslazyfox

import sys
import requests, re
from bs4 import BeautifulSoup
import json, time

def find_philosophy(url):
  MAX_HOPS = 30
  count = 0 # number of hops

  r = requests.get(url)
  soup = BeautifulSoup(r.text, "html.parser")
  finalURL = r.url # Print current url (after redirection)

  while soup.find(id='firstHeading').text != 'Philosophy':
    if count==MAX_HOPS:
      #print("MAX_HOPS reached.")
      return {'url': finalURL, 'count':count}

    content = soup.find(id='mw-content-text')
    for t in content.find_all(class_=['navbox', 'vertical-navbox', 'toc']):
      t.replace_with("")

    paragraph = soup.select('div[id=mw-content-text] > div[class=mw-parser-output] > p')[0] # Only DIRECT child
    for s in paragraph.find_all(['span', 'small', 'sup,', 'i', 'table']): # remove spans and smalls with language, pronounciation
      s.replace_with("")
    paragraphText = str(paragraph)
    paragraphText = re.sub(r' \(.*?\)', '', paragraphText) # Remove leftover parenthesized text
    
    # For debugging:
    #print(paragraphText) 

    reParagraph = BeautifulSoup(paragraphText, "html.parser") # back into bs4 object to find links
    firstLink = reParagraph.find(href = re.compile('^/wiki/')) # links that start with /wiki/ only

    while firstLink == None:
      # case of disambiguation: use first wiki link in list
      if '(disambiguation)' in url or '(surname)' in url:
        firstLink = content.ul.find(href = re.compile('^/wiki/'))

      else:  
        paragraph = paragraph.find_next_sibling("p")
        
        if(paragraph is None): # Catch-case

          if(content.ul is not None):
            firstLink = content.ul.find(href = re.compile('^/wiki/')) # Disambiguation-type page
          if(firstLink is None): # No links available
            return {'url': "Wikipedia not reachable.", 'count':1}
          continue

        for s in paragraph.find_all(['span', 'small', 'sup,', 'i', 'table']):
          s.replace_with("")
        paragraphText = str(paragraph)
        paragraphText = re.sub(r' \(.*?\)', '', paragraphText)
        reParagraph = BeautifulSoup(paragraphText, "html.parser")
        firstLink = reParagraph.find(href = re.compile('^/wiki/'))

      # For debugging:
      #print(paragraphText) 

    time.sleep(.05)
    url = 'http://en.wikipedia.org' + firstLink.get('href')
    r = requests.get(url) # Make new request
    soup = BeautifulSoup(r.text, "html.parser") # Soup it up again

    count = count+1

  #print(str(count) + " hops")
  return {'url': finalURL, 'count':count}

if __name__ == '__main__':

    # get json file and put into ascii_dict
    file = open("output.json").read()
    ascii_dict = json.loads(file)

    print("Continuing to find links...")

    # keep track of how many attributes in dictionary aren't blank
    blank = 0
    for element in ascii_dict:
        if ascii_dict[element] == "":
            blank += 1

    print(blank, "characters left")

    while (blank != 0):
        tmpObj = find_philosophy('http://en.wikipedia.org/wiki/Special:Random')

        # if the result from find_philosophy gives us a number that hasn't been assigned to a character yet
        if (tmpObj["count"] < 27) and (ascii_dict[str(tmpObj["count"])] == ""):
            ascii_dict[str(tmpObj["count"])] = tmpObj["url"]
            blank -= 1
            with open('output.json', 'w') as outfile:
                json.dump(ascii_dict, outfile)

            print("Got "+str(tmpObj["count"]))
        else:
            print("Out of bounds/Taken ("+tmpObj["url"]+") - "+str(tmpObj["count"]))