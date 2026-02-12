import requests as req
url_btc = "https://api4.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
res_btc = req.get(url_btc).json()
btc_price = float(res_btc['price'])

url_usd = "https://oapi.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=s4lSUN9i3rne8GsKR5DWHl4BQVbjEF6i&data=AP01"
res_usd = req.get(url_usd).json()
str_usd = res_usd[-1]['deal_bas_r'].replace(",","")
usd_price = float(str_usd)

krw = btc_price * usd_price
print(str(krw) + "원")