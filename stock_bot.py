"""
This bot will day trade a select amount of stocks

Using Alpaca API
-might include webscraping with selenium and yahoo finance to make it so it searches through stocks
-later will make a crypto bot to day trade more often
-will include machine learning in this too
-will have some calculations in cpython (maybe in c++ with dll ill decide after)

TODO:
-have a instant stop for when day lost 10% of earnings (just in case bad market)
-bot to run until the market closes, and then it will stop and report earnings or losses (total for today)
-bot will take in stream of data with sockets
-???
-profit

Created on 12/22/20
By: Me
"""

import alpaca_trade_api as tradeapi
import concurrent.futures, time
from alpaca_trade_api import StreamConn
stockTradingList = ['TSLA']     #5 max

TOTAL_CASH = 0

class PaperTradingBot(object):
    def __init__(self, alpaca, stock, cash):
        self.alpaca = alpaca
        self.stock = stock
        self.cash = cash

    def run(self):
        #loop through list of stocks to check through
        #free vers of polygon.io (used to stream stock price, while alpaca used to buy and sell), gives us 5 searches a min, therefore will use 5 searches a minute



        #initially declare each local function


        #on each minute
        async def on_minute(conn, channel, bar):
            #Entry
            if (bar.close >= bar.open and bar.open - bar.low > 0.1):
                print("Buying on Doji Candle!")
                #self.alpaca.submit()


        market_is_open = self.alpaca.get_clock()
        #now initialize necessary variables
        #

        async def waitABit():
            time.sleep(5)

        while(market_is_open.is_open is True):
            #this will be where the bot is running

            #so first we will asynchronously loop the stock and see whether to buy,
            #hold, or sell stock along with amount

            #then we will pause one and have another running checking a different stock (or
            # in other words a thread for each 5 stocks and they will run together, read if to b/s/h
            # and then wait some time)

            #decideOnStock(self.stock)
                #b/s/h based on market

            waitABit()


            #at the end of while loop
            market_is_open = self.alpaca.get_clock()

        results = "Add all info later " + self.stock
        return results
        #at end of market day, report earnings (return) and if theres a profit, take out 30%

"""
test rn, later take this out of list (maybe)
or could have the stock as a init definition and run 5 separate bots (each within a minute of each other)
and separately increment each run play separately in for loop (maybe 5 buys & wait a few & sell/buy/hold based on candle)
"""
                #self.alpaca.submit_order(self.stock, .5, 'buy')
            #Take Profit at increase


def main():
    global TOTAL_CASH
    key = 'PKNM5EGLRQENDVJMIY6K'       #hide these when uploading to github
    secret = 'Z9JRNIloBukw6R0U69QqJfFYWCVMG9RD4q5Q31FK'
    alpaca_endpoint = 'https://paper-api.alpaca.markets'
    alpaca = tradeapi.REST(key, secret, alpaca_endpoint, api_version='v2')

    #TOTAL_CASH = alpaca.cash
    #amount_given = TOTAL_CASH / 5

    with concurrent.futures.ThreadPoolExecutor() as executor:
        c1 = PaperTradingBot(alpaca,'TSLA',5000)
        c2 = PaperTradingBot(alpaca,'MSFT',5000)
        c3 = PaperTradingBot(alpaca,'AAPL',5000)

        f1 = executor.submit(c1.run)
        f2 = executor.submit(c2.run)
        f3 = executor.submit(c3.run)

        print(f1.result())
        print(f2.result())
        print(f3.result())



#alpaca = tradeapi.REST('PKNM5EGLRQENDVJMIY6K','Z9JRNIloBukw6R0U69QqJfFYWCVMG9RD4q5Q31FK','https://paper-api.alpaca.markets')
#alpaca.submit_order("MSFT",1,'buy','market','day')

#account = alpaca.get_account()
#print(int(account.cash))



if __name__ == "__main__":
    main()