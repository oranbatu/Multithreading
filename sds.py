with open("Results",mode="a",newline="") as csv_file:
    writer = csv.writer(csv_file)
    if csv_file.tell() == 0:
        writer.writerow(["Symbol","Symbol_Increase","Correlated_pair","CP_increased?","Kaç Katı arttı?"])



def fetch_candle_data(correlated_pair,interval):
    candles = exchange.fetch_ohlcv(correlated_pair,interval,limit=2)
    last_candle = candles[-1]
    second_to_last_candle = candles[-2]
    high_price = second_to_last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    open_price = second_to_last_candle[4]
    volume = second_to_last_candle[5]
    increase = (close_price - open_price) / open_price

    result2 = [open_price, high_price, low_price, close_price, volume, increase * 100]
    print(result2)