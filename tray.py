# Project Started

# imports
import time
import psutil
from playsound import playsound  # pip install playsound
import os
from datetime import datetime


# Audio System of Battery Alert
def alert():
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        if battery.percent >= 90:
            playsound('Dr.BatteryTunes/batery_full_capacity.mp3')
        elif 60 < battery.percent < 80:
            playsound('Dr.BatteryTunes/battery_moderate.mp3')
    else:
        if battery.percent <= 30:
            playsound('Dr.BatteryTunes/battery_at_20.mp3')
            f = open("demofile.txt", "w")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            f.write("Your PC Shutdown Time at "+ current_time)
            f.close()
            os.system("shutdown /s /t 1")


# Function which can Check Battery Percentage
def checkBatteryPercentage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    alert()
    return percent + '% | ' + plugged


# Running Function
if __name__ == "__main__":
    count = 0
    while 1:
        count += 1
        print(f"{count}: {checkBatteryPercentage()}")
        time.sleep(60)
