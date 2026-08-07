# 1.Design automation script which display information of running processes as its name, PID, Username.
# Usage : ProcInfo.py

import psutil
border = "*" *100

def ProcInfo():
    listproc = []

    for proc in psutil.process_iter():
        proc.cpu_percent(None)

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs = ("pid" ,"name", "username", "status"))
        info["Cpu_usage"] = proc.cpu_percent()
        info["Memory"] = proc.memory_percent()
        listproc.append(info)

    for i in listproc:
        print("PID : ", i.get("pid"))
        print("Name : ", i.get("name"))
        print("Usearname : ", i.get("username"))
        print("Memory : ", i.get("Memory"))
        print("Cpu percent : ", i.get("Cpu_usage"))

        print(border + "\n")
def main():
    ProcInfo()

if __name__ == "__main__":
    main()
