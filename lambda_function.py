from datetime import date
import config as cf
import CMCscraper as cmc
import sheets as sheets
import telegram as tel
from datetime import datetime

def lambda_handler(event,context): 
    now = datetime.now()

    token = cf.token
    receiver_id = cf.receiver_id
    cryptos = cf.cryptos

    prices = sheets.openSheets()[0]
    operations = sheets.openSheets()[1]

    sheets.updateIndicators(cryptos, prices)

    tickers = sheets.getStats(operations)[0]
    profits = sheets.getStats(operations)[1]
    prices = sheets.getStats(operations)[2]

    tel.sendUpdateTable(token,
                        receiver_id,
                        tickers,
                        profits,
                        prices, 
                        now)
    return None


