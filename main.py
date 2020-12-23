# Project Started

# imports
import psutil
from playsound import playsound  # pip install playsound

battery = psutil.sensors_battery()


# Audio System of Battery Alert
def alert():
    if battery.power_plugged:
        if battery.percent >= 90:
            playsound('Dr.BatteryTunes/batery_full_capacity.mp3')
        elif 60 < battery.percent < 80:
            playsound('Dr.BatteryTunes/battery_low.mp3')
    else:
        if battery.percent <= 20:
            playsound('Dr.BatteryTunes/battery_at_20.mp3')


# Function which can Check Battery Percentage
def checkBatteryPercentage():
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent + '% | ' + plugged)
    alert()


# Running Function
checkBatteryPercentage()
