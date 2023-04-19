"""
you need to
$ pip install ping3
$ pip install requests
"""

from ping3 import ping, verbose_ping
import pandas as pd
import datetime
import requests
import json
import configparser

# init config file
inifile = configparser.SafeConfigParser()
inifile.read('config.ini')

# set up webhool url
WEB_HOOK_URL = inifile.get('URL','WEB_HOOK_URL')


while True:
    with open("./date.txt",mode="r") as f:
        today = f.read()
    d_today = str(datetime.date.today())

    # init the day file if needed
    if d_today != today:
        print("initializing date file ....",end=" ")

        df = pd.read_csv('IpList.csv', header=0,names=["ip","name","IsInRoomFlag","ComeTime","LeaveTime"])
        df.to_csv(f'{d_today}.csv')
        with open("./date.txt",mode="w") as f:
            f.write(str(datetime.date.today()))


        print("DONE")

    df = pd.read_csv(f'{d_today}.csv', header=0,names=["ip","name","IsInRoomFlag","ComeTime","LeaveTime"])

    print(f"using ip list ... \n{df}")

    # search all IP address
    for index in range(df.shape[0]):
        curr_ip = df.loc[index,"ip"]
        
        if ping(curr_ip) is not False: #つまりipあり
            print(f"ip {curr_ip} exists")
            if df.loc[index,"ComeTime"] == False: #つまり登校
                df.loc[index,"ComeTime"] = datetime.datetime.now()
                curr_name = df.loc[index,"name"]
                
                # send message to slack
                requests.post(WEB_HOOK_URL, data=json.dumps({"text" : f"これはテストだよ。{curr_name}が登校したよ！",}))

            df.loc[index,"IsInRoomFlag"] = True
            

        else: #つまりipなし
            if df.loc[index,"IsInRoomFlag"] == True:
                df.loc[index,"LeaveTime"] = datetime.datetime.now()
                curr_name = df.loc[index,"name"]

                requests.post(WEB_HOOK_URL, data=json.dumps({"text" : f"これはテストだよ。{curr_name}が部屋を出て行ったよ！",}))

                df.loc[index,"IsInRoomFlag"] = False

    # save in today's file
    df.to_csv(f'{d_today}.csv')
