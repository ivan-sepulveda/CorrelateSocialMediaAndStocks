from bs4 import BeautifulSoup
import urllib
import urllib.parse as up
import urllib.request as ur
import urllib
# import urllib3
from urllib3 import request
import initialConditions



def urlToPartialIgUsername(urlInput):
    # some companies, like Under Armour do not follow the traditional IG username format for their subsdiaries
    # but can you blame them? "Under Armour Football is a mouthful" so they use uafootball
    # if this is the case...I don't know I'll get back to you but for now nike and adidas are good
    retailerMainIG = "https://www.instagram.com/" + initialConditions.retailerIg + "/"

    if urlInput == retailerMainIG:
        return None
    splitBySlash = urlInput.split("/")
    filterBySlash = list(filter(None, splitBySlash))
    fullIgName = filterBySlash[-1]
    splitSubName = fullIgName.split(initialConditions.retailerIg)
    splitByBrand = list(filter(None, splitSubName))
    # print("splitbybrand")
    # print(splitByBrand)
    partialIgUsername = splitByBrand[0]
    return partialIgUsername


def findSubsidiaries(query):
    address = "http://www.bing.com/search?q=%s" % (up.quote_plus(query))
    retailerMainIG = "https://www.instagram.com/" + initialConditions.retailerIg + "/"

    # print(address)
    html_page = ur.urlopen(address).read()
    soup = BeautifulSoup(html_page, "html5lib")
    subsidiaryUrls = list()
    for link in soup.findAll('a'):
        hRefObject = link.get('href')
        if type(hRefObject) == type(str("str")):
            if "instagram" in hRefObject and "search" not in hRefObject and "/p/" not in hRefObject:
                if "verified" not in hRefObject and initialConditions.retailerIg in hRefObject:
                    if hRefObject.lower() not in subsidiaryUrls:
                        subsidiaryUrls.append(link.get('href').lower())
    if retailerMainIG in subsidiaryUrls:
        subsidiaryUrls.remove(retailerMainIG)
    # subsidiaryUrls = list(filter("https://www.instagram.com/"+initialConditions.retailerIg + "/", subsidiaryUrls))
    return subsidiaryUrls

def secondRoundSubsidiaries(query):
    address = "http://www.bing.com/search?q=%s" % (up.quote_plus(query))
    # print(address)
    html_page = ur.urlopen(address).read()
    soup = BeautifulSoup(html_page, "html5lib")
    subsidiaryUrls = list()
    for link in soup.findAll('a'):
        hRefObject = link.get('href')
        if type(hRefObject) == type(str("str")):
            if "instagram" in hRefObject and "search" not in hRefObject and "/p/" not in hRefObject:
                if "verified" not in hRefObjec and hRefObject not in initialConditions.retailerIg in hRefObject:
                    # print(link.get('href'))
                    subsidiaryUrls.append(hRefObject)
    return subsidiaryUrls


def specialFilter(listOfUrls):
    if 'https://www.instagram.com/nikejane/' in listOfUrls:
            return listOfUrls.remove('https://www.instagram.com/nikejane/')
    return listOfUrls

def resultsFromThisManySearches(numberOfSearches=1):
    searchConstraints = 'site:instagram.com inBody:verified ' + initialConditions.retailerIg
    # retailerMainIG = "https://www.instagram.com/" + initialConditions.retailerIg + "/"
    allSubsidiaryLinks = list()
    print("orig search constraints")
    print(searchConstraints)
    for i in range(numberOfSearches):
        links = findSubsidiaries(searchConstraints)
        allSubsidiaryLinks += links
        for l in links:
            searchConstraints += (" -" + urlToPartialIgUsername(l))
    # firsRoundLinks = findSubsidiaries(searchConstraints)
    # print("first round")
    # print(firsRoundLinks)
    # for l in firsRoundLinks:
    #     print(urlToPartialIgUsername(l))
    #     searchConstraints += (" -" + urlToPartialIgUsername(l))
    # print("new search constraints")
    # print(searchConstraints)
    # secondRoundLinks = findSubsidiaries(searchConstraints)
    # print("second round")
    # print(secondRoundLinks)
    allSubsidiaryLinks = specialFilter(allSubsidiaryLinks)
    return allSubsidiaryLinks
endResult = resultsFromThisManySearches(4)
print(len(list(endResult)))
print(endResult)


# searchConstraints = 'site:instagram.com inBody:verified ' + initialConditions.retailerIg
# retailerMainIG = "https://www.instagram.com/" + initialConditions.retailerIg + "/"
# allSubsidiaryLinks = list()
#
#
#
# # print("First round of scraping for subsidiaries")
# print("orig search constraints")
# print(searchConstraints)
# firsRoundLinks = findSubsidiaries(searchConstraints)
# print("first round")
# print(firsRoundLinks)
# for l in firsRoundLinks:
#     print(urlToPartialIgUsername(l))
#     searchConstraints += (" -" +urlToPartialIgUsername(l))
# print("new search constraints")
# print(searchConstraints)
# secondRoundLinks = findSubsidiaries(searchConstraints)
# print("second round")
# print(secondRoundLinks)

