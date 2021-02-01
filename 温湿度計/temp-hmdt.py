import RPi.GPIO as GPIO
import dht11
import time
import datetime

LedGpio1 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LedGpio1, GPIO.OUT)

now = datetime.datetime.now()
Ntime = now.strftime("%Y-%m-%d %H:%S")

TEMP_GPIO = 4
FILE_NAME = "/home/pi/Desktop/io31_kadai06_22/temp-hmdt.csv"

GPIO.setmode(GPIO.BCM)
dhtStat = dht11.DHT11(pin = TEMP_GPIO) # センサーの情報を読み取るピンを指定

while True:
    stat = dhtStat.read()    # センサーの情報を読み取る

    if stat.temperature == 0 and stat.humidity == 0:
        continue
    print(Ntime)
    print(stat.temperature)  # 温度を表示
    print(stat.humidity)     # 湿度を表示
    
    if stat.temperature > 20:
        GPIO.output(LedGpio1,GPIO.HIGH)
    else:
        GPIO.output(LedGpio1,GPIO.LOW)
        

    data = [Ntime, stat.temperature, stat.humidity]    # リスト（配列）

    # print(','.join(map(str, data)))
    # ファイルへ書き込む
    with open(FILE_NAME, mode="a", encoding="utf-8") as file:
        file.write(','.join(map(str, data)) + '\n') # mapを使ってintからstrに変換
    time.sleep(60)
    #GPIO.cleanup()
    

    


    