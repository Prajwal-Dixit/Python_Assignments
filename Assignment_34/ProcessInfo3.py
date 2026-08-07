# 1.Design automation script which display information of running processes as its name, PID, Username.
# Usage : ProcInfo.py

import psutil
import sys
import time
import os

border = "*" *100

def ProcInfo(directory):

    if not os.path.exists(directory):
        print("Given directory doesnt exists")
        return
    if not os.path.isdir(directory):
        print("Given argument is not a directory")
        return 
    
    listproc = []
    logfile = "ProcessLog_%s.txt" % time.strftime("%Y_%m_%d_%H_%M_%S")
    logfile = os.path.join(directory, logfile)

    fobj = open(logfile, "w")

    for proc in psutil.process_iter():
        proc.cpu_percent(None)

    time.sleep(1)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ("pid" ,"name", "username", "status"))
        info["Cpu_usage"] = proc.cpu_percent()
        info["Memory"] = proc.memory_percent()
        listproc.append(info)

    for i in listproc:
        fobj.write(f"PID : {i.get('pid')} \n")
        fobj.write(f"Name : {i.get('name')} \n")
        fobj.write(f"Usearname : {i.get('username')} \n")
        fobj.write(f"Memory : {i.get('Memory')} \n")
        fobj.write(f"Cpu percent : {i.get('Cpu_usage')} \n")

        fobj.write(border + "\n")
    fobj.close()
def main():
    if (len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Execute program as : <Program.py> <directory_name>")
        sys.exit()

    ProcInfo(sys.argv[1])

if __name__ == "__main__":
    main()