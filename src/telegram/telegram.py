import requests
from bs4 import BeautifulSoup as bs
import re
from genericfunctions import *

if __name__ == "__main__":
  url = "https://services2.hdb.gov.sg/webapp/BP13BTOENQWeb/AR_Feb2022_BTO?strSystem=BTO"

  headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36"
  }

  btoMap = {}

  page = requests.get(url, headers=headers)
  if page.status_code == 200:
    soup = bs(page.text, 'html.parser')
    data = soup.find_all(re.compile("(tr)"), text=[re.compile("(mature).", re.IGNORECASE)])
    for parentData in data:
      siblingsData = parentData.find_next_siblings("tr")
      for siblingData in siblingsData:
        siblingDataText = siblingData.text
        # asd = siblingDataText.split("\n")

        # filter away "mature/ non-mature from results"
        if ("mature" not in siblingDataText):
          print(checkIfNumber(siblingDataText))
          # if can be converted to int, means it's not a building/ room
          if (not checkIfNumber(siblingDataText)):
            continue
            # if (siblingDataText not in btoMap.keys()):
            #   currentBlock = siblingDataText
            #   internalMap = {}
            #   map[currentBlock] = internalMap
            # elif "room" not in siblingDataText:
            #   isTwoRoom = True
            #   internalMap["twoRoom"] = []
            #   map[currentBlock] = internalMap
            # else:
            #   currentRoom = siblingDataText
            #   internalMap[currentRoom] = []
            #   map[currentBlock] = internalMap
        # print(asd)
    

    # data1 = soup.find_all("tr", text="^(geylang).", re.IGNORECASE))
    # to find specific excluding room type