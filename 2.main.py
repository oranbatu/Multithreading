import ccxt
import asyncio
import csv
import datetime
import os


exchange = ccxt.binance({'enableRateLimit': True})
symbols = ["CVP/USDT", "BOND/USDT", "HOOK/USDT", "HFT/USDT", "PHB/BUSD", "QUICK/USDT", "SANTOS/BUSD",
               "COCOS/USDT",
               "MINA/USDT", "MINA/USDT", "FET/USDT", "MANA/USDT",
               "AXS/USDT", "ONE/USDT", "AVAX/USDT", "LOKA/USDT", "PHB/USDT"]
column_names = ["Date", "Time", "Open", "High", "Low", "Close", "Volume", "Increase"]


async def fetch_data():
    candles = exchange.fetch_ohlcv(symbol, interval, limit=2)
    last_candle = candles[-1]
    second_to_last_candle = candles[-2]
    high_price = second_to_last_candle[2]
    low_price = last_candle[3]
    close_price = last_candle[4]
    open_price = second_to_last_candle[4]
    volume = second_to_last_candle[5]
    increase = (close_price - open_price) / open_price

    result = [open_price, high_price, low_price, close_price, volume, increase * 100, correlated_pair]
    write_to_csv(result, filename, column_names)

    if increase >= percentage:
        print(f"Signal: {symbol} has increased by {increase * 100:.2f}%. It's correlated pair is {correlated_pair}")
        # result = [open_price, high_price, low_price, close_price, volume, increase * 100, correlated_pair]
        # write_to_csv(result,filename,column_names)



    elif increase <= -percentage:
        print(f"Signal: {symbol} has decreased by {increase * 100:.2f}%. It's correlated pair is {correlated_pair}")
        # result = [open_price, high_price, low_price, close_price, volume, increase * 100, correlated_pair]
        # write_to_csv(result,filename,column_names)

async def fetch_data2():
    candles2 = exchange.fetch_ohlcv(correlated_pair, interval2, limit=2)
    last_candle2 = candles2[-1]
    second_to_last_candle2 = candles2[-2]
    high_price2 = second_to_last_candle2[2]
    low_price2 = last_candle2[3]
    close_price2 = last_candle2[4]
    open_price2 = second_to_last_candle2[4]
    volume2 = second_to_last_candle2[5]
    increase2 = (close_price2 - open_price2) / open_price2

    result2 = [open_price, high_price, low_price, close_price, volume, increase * 100]
    print(result2)


def write_to_csv(data,filename,column_names):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = [timestamp] + data
    column_name = ["Date", "Time", "Open", "High", "Low", "Close", "Volume", "Increase"]

    with open(f"/Users/batuhanoran/Desktop/csv_folder/{filename}", mode='a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(column_names)
        writer.writerow(data_with_timestamp)

    with open(f"/Users/batuhanoran/Desktop/csv_folder/{filename}",mode='r',newline='') as read_file:
        reader = csv.reader(read_file)
        row_count = 0
        for row in reader:
            row_count += 1
            if row_count == 120:
                os.remove(f"/Users/batuhanoran/Desktop/csv_folder/{filename}")

async def main():
    symbols = ["CVP/USDT", "BOND/USDT", "HOOK/USDT", "HFT/USDT", "PHB/BUSD", "QUICK/USDT", "SANTOS/BUSD",
               "COCOS/USDT",
               "MINA/USDT", "MINA/USDT", "FET/USDT", "MANA/USDT",
               "AXS/USDT", "ONE/USDT", "AVAX/USDT", "LOKA/USDT", "PHB/USDT"]  # symbols for the crypto pairs
    correlated_pairs = ["DF/USDT", "WINGUSDT", "MAGIC/USDT", "HOOK/USDT", "AMB/BUSD", "FARM/USDT", "LAZIO/BUSD",
                        "COS/USDT",
                        "LRC/USDT", "MASK/USDT", "OCEAN/USDT", "SAND/USDT"
        , "SLPUSDT", "CELR/USDT", "JOE/USDT", "VOXEL/USDT", "AMB/USDT"]  # correlated pairs
    interval = "1m"  # interval for the candle data
    percentage = 0.0002  # threshold for the increase
    # Get the current time and calculate the number of seconds remaining until the next minute
    now = datetime.datetime.now()
    remaining_seconds = 60 - now.second

    # Wait for the remaining number of seconds before executing the loop
    asyncio.get_event_loop().run_until_complete(asyncio.sleep(remaining_seconds))

    for symbol in symbols:
        filename = symbol.replace("/", "_").replace(":", "_") + ".csv"
        index = symbols.index(symbol)
        correlated_pair = correlated_pairs[index]

        task1 = asyncio.create_task(fetch_data())
        task2 = asyncio.create_task(fetch_data2())

        await task1
        await task2

while True:
    asyncio.run(main())




