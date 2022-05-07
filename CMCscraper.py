import requests
from bs4 import BeautifulSoup

def formatMoney(number):
    number = number[1:]
    number = float(number.replace(",", ""))
    return number

def percentageChange(html):
    sign = 1
    
    if "down" in html:
        sign = -1
    
    html = (html.split("</span>"))[1]
    html = (html.split("<"))[0]
    html = float(html)*sign 

    return html

def getIndicators(currency):

    url = 'https://coinmarketcap.com/en/currencies/' + str(currency) + '/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features= 'lxml')
    tbody = soup.find_all("tbody")

    tbody_main = list(tbody[0].children)
    tbody_cap = list(tbody[1].children)
    
    price = tbody_main[0].td.string
    price = formatMoney(price)

    price_change = tbody_main[1].td.span.string
    price_change = formatMoney(price_change)
    price_change = round((price_change/price)*100,2)
    
    volume_change = str(tbody_main[3].find_all('span')[-2])
    volume_change = percentageChange(volume_change)

    dominance = str(tbody_main[5].td.span)
    dominance = (dominance.split("<!-- -->"))[0]
    dominance = float((dominance.split(">"))[1])

    rank = tbody_main[6].td.string
    rank = float(rank[1:])

    cap_change = str(tbody_cap[0].find_all("span")[-2])
    cap_change = percentageChange(cap_change)

    indicators = [  price, 
                    price_change, 
                    volume_change,
                    cap_change,
                    dominance,
                    rank]

    return indicators