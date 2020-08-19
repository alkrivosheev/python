import time
import os
import pandas#pip3 install pandas


while True:
    if os.path.exists("temps_today.csv"):
        data = pandas.read_csv("temps_today.csv")
        print(data.mean()["st1"])
    else:
        print("File is not exist.")
    time.sleep(5)