# 1.Design automation script which display information of running processes as its name, PID, Username.
# Usage : ProcInfo.py

import psutil
import sys
import time
import os
import smtplib
from email.message import EmailMessage

border = "*" *100

def send_mail(sender, reciever, password, subject, body, attach, Filename):
    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = reciever
    msg["Subject"] = subject

    msg.set_content(body)
    msg.add_attachment(attach, maintype = "text", subtype = "Plain", filename = Filename)

    Smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    Smtp.login(sender, password)
    Smtp.send_message(msg)
    Smtp.quit()

def ProcInfo(directory, sender, reciever):

    if not os.path.exists(directory):
        print("Given directory doesnt exists")
        return
    if not os.path.isdir(directory):
        print("Given argument is not a directory")
        return 
    
    listproc = []
    logfile_name = "ProcessLog_%s.txt" % time.strftime("%Y_%m_%d_%H_%M_%S")
    logfile = os.path.join(directory, logfile_name)

    fobj = open(logfile, "w")

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

    fobj = open(logfile, "rb")
    attach = fobj.read()

    subject = "Process information update"

    body = """
    Dear Sir,
    This email is to update you with the processes running on the system
    
    Regards,
    Delta Systems
    """
    password = ""

    try : 
        send_mail(sender, reciever, password, subject, body, attach, logfile_name )
        fobj.close()
    except Exception as e:
        print("Email failed : ", e)

def main():

    if (len(sys.argv) != 4):
        print("Invalid number of arguments")
        print("Execute program as : <Program.py> <directory_name> <sender_mail_address> <receiver_mail_address")
        sys.exit()

    ProcInfo(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()