# Project Started

# imports
import time
import psutil
from playsound import playsound  # pip install playsound


# Audio System of Battery Alert
def alert():
    battery = psutil.sensors_battery()
    if battery.power_plugged:
        if battery.percent >= 90:
            playsound('Dr.BatteryTunes/batery_full_capacity.mp3')
        elif 60 < battery.percent < 80:
            playsound('Dr.BatteryTunes/battery_moderate.mp3')
    else:
        if battery.percent <= 20:
            playsound('Dr.BatteryTunes/battery_at_20.mp3')


# Function which can Check Battery Percentage
def checkBatteryPercentage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent + '% | ' + plugged)
    alert()


# Running Function
if __name__ == "__main__":
    while 1:
        checkBatteryPercentage()
        time.sleep(300)
