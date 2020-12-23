# Project Started

# imports
import psutil


# Function which can Check Battery Percentage
def checkBatteryPercentage():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent + '% | ' + plugged)


# Running Function
checkBatteryPercentage()
