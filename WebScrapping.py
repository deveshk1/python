# #this program opens AMAZON shopping page and downloads price information
#
# import bs4  #for web scrapping
# import requests #for downloading
#
# response = requests.get('https://www.flipkart.com/red-label-natural-care-cardamom-ginger-liquorice-tulsi-tea-box/p/itmf9rgsp9bcdugr?pid=TEAETY5NKPGFGFZK&lid=LSTTEAETY5NKPGFGFZKEGFMJJ&marketplace=FLIPKART&srno=b_1_1&otracker=hp_banner_2_4.bannerX3.BANNER_HCJ5R0BOYYPU&fm=neo%2Fmerchandising&iid=399ae9db-18f1-4c36-b93a-7b5849337856.TEAETY5NKPGFGFZK.SEARCH&ppt=browse&ppn=browse&ssid=xde0qi84hc0000001587142008941')
# response.raise_for_status()
# soup= bs4.BeautifulSoup(response.text,'html.parser') #html parser is for parsing the html page
# # select is to select that particular element form HTML web page
# element = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
# element=element[0].text.strip() #to get the 0th index value i.e 235(price) ,Strip is to remove new line or spaces from left/right
# print(element)

import requests, bs4


def flipkartPrice(ProductURL):
    response = requests.get(ProductURL)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    try:
        element = soup.select(
        '#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    except:
        print("Selector not working")
    price = element[0].text.strip()
    return price


price1 = flipkartPrice(
    'https://www.flipkart.com/red-label-natural-care-cardamom-ginger-liquorice-tulsi-tea-box/p/itmf9rgsp9bcdugr?pid=TEAETY5NKPGFGFZK&lid=LSTTEAETY5NKPGFGFZKEGFMJJ&marketplace=FLIPKART&srno=b_1_1&otracker=hp_banner_2_4.bannerX3.BANNER_HCJ5R0BOYYPU&fm=neo%2Fmerchandising&iid=399ae9db-18f1-4c36-b93a-7b5849337856.TEAETY5NKPGFGFZK.SEARCH&ppt=browse&ppn=browse&ssid=xde0qi84hc0000001587142008941')
print('The  Price is ' + price1)



