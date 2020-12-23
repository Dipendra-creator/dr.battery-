# Project Started

# imports
import psutil
from playsound import playsound  # pip install playsound


# Function which can Check Battery Percentage
def checkBatteryPercentage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent + '% | ' + plugged)
    plug = battery.power_plugged
    if plug == True:
        playsound("D:/python/dr.battery-/Dr.Battery tunes/batery_full_capacity.mp3")


# Running Function
checkBatteryPercentage()
