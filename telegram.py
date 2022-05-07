import telepot  

def sendUpdateTable(token, receiver_id, tickers, profits, prices, date):
    bot = telepot.Bot(token)
    message = '``` \n'

    for i, ticker in enumerate(tickers): 

        out = formatEntries(ticker, prices[i], profits[i], i)
        message += "{: ^7} {: >10} {: >9} {: <6}".format(out[0], out[1], out[2], out[3]) + '\n'
    
    message +=  '```'

    date = (str(date)).split('.')[0]
    date = '*' + date + '*'

    bot.sendMessage(receiver_id, date, parse_mode= 'Markdown')
    bot.sendMessage(receiver_id, message, parse_mode= 'Markdown')

    return None

def formatEntries(ticker, price, profit, i):

    emojis = ['🌚', '🚀 ', '🌏', '💩']
    emoji = emojis[0]

    if i > 0: 
        profit = float(profit.replace(',', '.'))

        if profit < 0: 
                emoji = emojis[3]
        elif profit >= 0 and profit < 5: 
                emoji = emojis[2]
        elif profit >= 5 and profit < 20:
                emoji = emojis[1]

        ticker = str(ticker)
        price = '$' + str(price)
        profit = str(profit) + '%'

    else: 
        emoji = ''
    
    return (ticker, price, profit, emoji)

