import requests, sys, time, winsound

last_price = 0.0
current_price = 0.0

def price_checker(target, per):
    url = 'https://vip.bitcoin.co.id/api/{0}_{1}/ticker'.format(target, per)
    resp = requests.get(url).json()
    return float(resp['ticker']['last'])

def jump_percent(current, last):
    delta = abs(current - last)
    return (delta / last) * 100

def run_checker(target, per):
    global last_price, current_price
    current_price = price_checker(target, per)
    if (current_price > last_price):
        if last_price > 0.0:
            percent = jump_percent(current_price, last_price)
            if (percent > 5.0):
                winsound.PlaySound('resources/up.wav', winsound.SND_FILENAME)
        print('%.8f' % current_price)
    elif (current_price < last_price):
        percent = jump_percent(current_price, last_price)
        print('%.8f' % current_price)
        if (percent > 5.0):
            winsound.PlaySound('resources/down.wav', winsound.SND_FILENAME)
    last_price = current_price
while True:
    run_checker(sys.argv[1], sys.argv[2])
    time.sleep(1)