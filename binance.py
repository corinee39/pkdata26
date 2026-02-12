# 응용2
import requests as req
url = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
res = req.get(url).text
btc = res[29:34]
price = str(int(btc)*1450)
print(price)
int1 = price[:1]
int2 = price[1:5]
int3 = price[5:]
print(int1 + '억 ' + int2 + '만 ' + int3 +'원')