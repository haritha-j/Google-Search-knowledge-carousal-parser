# core modules
import codecs
import os
import sys

# 3rd party modules
from selenium import webdriver


#############################################################################
#parameters

#define the number of results to fetch from carousal

numOfCarousalResults = int(sys.argv[1])
print (numOfCarousalResults)

keywords=[]
for k in sys.argv[2:]:
    keywords.append(k)


##############################################################################

#build url

url = "https://www.google.lk/search?q="
for keyword in keywords:
    url+=keyword+"+"
url=url[:-1]
url+="&ie=UTF-8"


##############################################################################

#download page

def get_browser():
    """Get the browser (a "driver")."""
    # find the path with 'which chromedriver'
    path_to_chromedriver = ('C:/Users/harit/.spyder-py3/chromedriver')
    browser = webdriver.Chrome(executable_path=path_to_chromedriver)
    return browser


save_path = "C:/Users/harit/.spyder-py3/"
file_name = 'index.html'
browser = get_browser()

browser.get(url)

complete_name = os.path.join(save_path, file_name)
file_object = codecs.open(complete_name, "w", "utf-8")
html = browser.page_source
file_object.write(html)
browser.close()

#open txt file
file=open("index.html", "r")
#file.close()
htmlfi =file.read()
#print(htmlfi(14))

#print(htmlfi)


##############################################################################

#get the list of new keywords
listOfResults = []

#function to find all occurances of a substring
def find_all(a_str, sub):
    start = 0

    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start

        start += len(sub) # use start += 1 to find overlapping matches
 
#find all occurances of the string "kltat" (kltat is the class that denotes a class heading )
li = (list(find_all(htmlfi, 'class="kltat"')))
#print(li)
for x in range(len(li)):
    if x>numOfCarousalResults:
        break
    else:
        #find the full text of results that spans multiple lines
        end=htmlfi.find("</div>", li[x])
        stringList = (list(find_all(htmlfi[li[x]:end], '<span>')))
        #print (stringList)
        res=""
        for z in range(len(stringList)):
            endchar = htmlfi.find("</span>", li[x]+stringList[z])
            #print (endchar)
            res+=(htmlfi[li[x]+stringList[z]+6:endchar])
        listOfResults.append(res)
        
print (listOfResults)