# 2.Design automation script which accept process name and display information of that process if
# it is running.
# Usage : ProcInfo.py Notepad

import psutil
import sys
import time

def DisplayProc(process_name):
    border = "-" * 100

    logfile = "ProcessLog.%s.txt" % time.strftime("%Y_%m_%d_%H_%M_%S")

    fobj = open(logfile, "w")
    fobj.write(border + "\n")
    fobj.write("--------------------------------------Process Inforation--------------------------------------------\n")
    fobj.write(border + "\n")

    ret, process = IsRunning(process_name)
    if (ret == False):
        print("Process is not running")
        return

    try :
        fobj.write(f"Name : {process.name()} \n")
        fobj.write(f"PID : {process.pid} \n")
        fobj.write(f"Status : {process.status()} \n")
        fobj.write(f"Username : {process.username()} \n")
        fobj.write(f"Memory usage :{process.memory_percent()} \n")
        fobj.write("\n"+ border + "\n")

    except (psutil.NoSuchProcess, psutil.AccessDenied) :
        fobj.write("Unable to access the file")

def IsRunning(process):
    for proc in psutil.process_iter():
        if(proc.name() == process):
            return True, proc
    return False, None

def main():
    if (len(sys.argv) != 2):
        print("Invalid nummber of arguments")
        print("Execute program as : <Program.py> <Process_name>")
        sys.exit()

    DisplayProc(sys.argv[1])

if __name__ == "__main__":
    main()