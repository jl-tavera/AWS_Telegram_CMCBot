import config as cf
import CMCscraper as cmc
import gspread 


def openSheets(): 
    gc = gspread.service_account(filename= 'creds.json')
    sh = gc.open('Tracker')
    prices = sh.sheet1
    operations = sh.worksheet('Operations')
    return (prices, operations)


def updateIndicators(currencies, sheet):

    for index, coin in enumerate(currencies):

        range = 'B' + str(index + 2) + ':G' + str(index + 2)
        cell_list = sheet.range(range)
        cell_values = cmc.getIndicators(coin)
        
        for i, val in enumerate(cell_values):  
            cell_list[i].value = val  
        
        sheet.update_cells(cell_list)

    return None

def getStats(sheet): 
    operations = sheet
    tickers = operations.col_values(1)
    profits = operations.col_values(2)
    prices = operations.col_values(3)
    
    return (tickers, profits, prices)


