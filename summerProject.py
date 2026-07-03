#python -m flask --app summerProject run    
import os
import psutil
from flask import Flask

def find_procs_by_name(name): #maybe find with a .exe file
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(["name", "exe", "cmdline"]):
        if name == p.info['name'] or \
                p.info['exe'] and os.path.basename(p.info['exe']) == name or \
                p.info['cmdline'] and p.info['cmdline'][0] == name:
            ls.append(p)
            p.cpu_percent(interval=1, percpu=True) #per process prints out cpu usage
            #check process cpu usage and add to the list if it's too high
            processCPUUsage=p.cpu_percent(interval=.1) 
            processCPUUsage = processCPUUsage/psutil.cpu_count() * 100
           # x / psutil.cpu_count() * 100 for x in psutil.getloadavg()
            if processCPUUsage>0: 
                ls.append(p)
    return ls

#for proc in psutil.process_iter(['pid', 'name']): # does print out roblox player
 #       print(proc.info)
for proc in psutil.process_iter(['name']): # does print out roblox player
       l=proc.cpu_percent(interval=.1)
       l = l/psutil.cpu_count() * 100
       proc.memory_full_info()
       print(proc.info.get('name')+" "+ str(l))
      # if (l>0):
       # print(l) #way too damn slow

app = Flask(__name__)

@app.route("/")
def hello_world():
    
    testInput = find_procs_by_name("test.exe")
    if find_procs_by_name("test.exe"):
        
         return "<p>This computer is currently in use</p>"
    else:
         return "<p> This computer's not running an .exe program</p>"
    return "<p>Hello, World!</p>"