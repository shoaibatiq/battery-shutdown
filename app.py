import psutil
from time import sleep
import os
import winsound
t=int(input("Percentage: "))

while True:
    battery = psutil.sensors_battery()
    if battery.percent<t+1:
        winsound.Beep(2500, 800)
        for i in range(9,-1,-1):
            print(f'Sutting Down in {i} sec')
            sleep(1)
        break
    else:
        sleep(120)
os.system("shutdown /s /t 1")