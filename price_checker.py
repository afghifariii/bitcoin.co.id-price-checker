import requests, sys, time, winsound

last_price = 0.0
current_price = 0.0

def price_checker(target, per):
    url = 'https://vip.bitcoin.co.id/api/{0}_{1}/ticker'.format(target, per)
    resp = requests.get(url).json()
    return float(resp['ticker']['last'])

def run_checker(target, per):
    global last_price, current_price
    current_price = price_checker(target, per)
    if (current_price > last_price):
        if last_price > 0.0:
            increase = current_price - last_price
            percentage = (increase / last_price) * 100
            if (percentage > 5.0):
                winsound.PlaySound('resources/up.wav', winsound.SND_FILENAME)
        print('%.8f' % current_price)
    elif (current_price < last_price):
        decrease = last_price - current_price
        percentage = (decrease / last_price) * 100
        print('%.8f' % current_price)
        if (percentage > 5.0):
            winsound.PlaySound('resources/down.wav', winsound.SND_FILENAME)

while True:
    run_checker(sys.argv[1], sys.argv[2])
    time.sleep(10)