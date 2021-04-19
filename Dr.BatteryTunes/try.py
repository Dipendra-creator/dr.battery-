from datetime import datetime
import os
f = open("demofile.txt", "w")
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
f.write("Your PC Shutdown Time at "+ current_time)
f.close()
os.system("shutdown /s /t 1")