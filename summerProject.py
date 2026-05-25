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
    return ls

for proc in psutil.process_iter(['pid', 'name']): # does print out roblox player
        print(proc.info)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"