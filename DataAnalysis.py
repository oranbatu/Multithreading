import pandas as pd
import numpy as np
import csv
import time
df = []
symbols = ["CVP/USDT", "BOND/USDT", "HOOK/USDT", "HFT/USDT", "PHB/BUSD", "QUICK/USDT", "SANTOS/BUSD",
               "COCOS/USDT",
               "MINA/USDT", "MINA/USDT", "FET/USDT", "MANA/USDT",
               "AXS/USDT", "ONE/USDT", "AVAX/USDT", "LOKA/USDT", "PHB/USDT"]

num_dataframes = len(symbols)
column_names = ["Date","Time","Open","High","Low","Close","Volume","Increase"]
df_names = ["df{}".format(i) for i in range(num_dataframes)]            # Isim Listesi
dfs = {name: pd.DataFrame(columns=column_names) for name in df_names}
print(dfs["df1"])



while True:
    for symbol in symbols:
        filename = symbol.replace("/", "_").replace(":", "_") + ".csv"
        with open(f"/Users/batuhanoran/Desktop/csv_folder/{filename}",mode="r") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)


    time.sleep(60)