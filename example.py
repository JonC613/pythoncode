#!/usr/bin/env python
# This program buys some Dogecoins and sells them for a bigger price
import time
from bittrex import bittrex

# Get these from https://bittrex.com/Account/ManageApiKey
api = bittrex('ec95eb5569464074a68a365edf32b364', '47ed9c9a6b194010a08af9f14cb2f77f')
 

def priceMarket(trade,currency):
	
	# Market to trade at
	market = '{0}-{1}'.format(trade, currency)
	# Amount of coins to buy
	#amount = 100
	# How big of a profit you want to make
	#multiplier = 1.1

	# Getting the BTC price for DOGE
	summary = api.getmarketsummary(market)
	price = summary[0]['Last'] 
	print summary[0]
	print ('The price for {0} is {1:.8f} {2}.').format(currency, price, trade)

def priceBalances():
		
	summary = api.getbalances()
	print summary
	#print summary[0]['Currency']
	#print summary[1]['Currency']
	#print summary[0]['ANS']

	


priceBalances()		
#priceMarket('USDT','BTC')
#priceMarket('USDT','ANS')

	 


# Buying 100 DOGE for BTC
#print ('Buying {0} {1} for {2:.8f} {3}.').format(amount, currency, dogeprice, trade)
#api.buylimit(market, amount, dogeprice)

# Multiplying the price by the multiplier
#dogeprice = round(dogeprice*multiplier, 8)

# Selling 100 DOGE for the  new price
#print ('Selling {0} {1} for {2:.8f} {3}.').format(amount, currency, dogeprice, trade)
#api.selllimit(market, amount, dogeprice)

# Gets the DOGE balance
#dogebalance = api.getbalance(currency)
#print ("Your balance is {0} {1}.").format(dogebalance['Available'], currency)

# For a full list of functions, check out bittrex.py or https://bittrex.com/Home/Api
