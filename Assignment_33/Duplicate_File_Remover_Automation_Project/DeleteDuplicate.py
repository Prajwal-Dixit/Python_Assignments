#######################################################################################################
#   Function name :         DeleteDuplicate
#   Input :                 Name of directory
#   Description :           Deletes all duplicate files periodically
#   Date :                  26/07/2026
#   Author :                Prajwal
########################################################################################################

import smtplib
import os
import time
from FindDuplicates import FindDuplicate
from SendMail import send_mail

def DeleteDuplicate(DirectoryName, email_address):
    border = "-"*80
    start_time = time.perf_counter()

    #MyDict, total_files = FindDuplicate(DirectoryName, email_address)
    Result = FindDuplicate(DirectoryName, email_address)

    if(Result == None):
        return

    MyDict, total_files = Result
    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    timestamp = time.ctime()
    LogfileName = "DeleteDuplicate"+ timestamp +".log"
    LogfileName = LogfileName.replace(" ", "_")
    LogFileDirectory = "Duplicate_Remover"

    os.makedirs(LogFileDirectory, exist_ok = True)
    LogFileDirectory = os.path.abspath(LogFileDirectory)
    Logfile = os.path.join(LogFileDirectory, LogfileName)

    fobj = open(Logfile,"w")

    fobj.write(border + "\n")
    fobj.write("Duplicate remover automation script \n")
    fobj.write(border + "\n")
    fobj.write("Deleted duplicate files : \n")
    fobj.write(border + "\n\n")

    Count = 0
    TotalDuplicates = 0
    DuplicatesDeleted = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                try:
                    os.remove(subvalue)
                    DuplicatesDeleted += 1
                    fobj.write(os.path.abspath(subvalue) + "\n")

                except PermissionError:
                    fobj.write(f"Permission denied, cannot delete the file {subvalue}")
                except FileNotFoundError:
                    fobj.write(f"File {subvalue} is already deleted")
                except OSError:
                    fobj.write(f"Could not delete the file {subvalue}")
            TotalDuplicates = TotalDuplicates + 1
                
        Count = 0

    stop_time = time.perf_counter()

    fobj.write("\n" + border + "\n")
    fobj.write(f"Directory scanned : {DirectoryName}\n")
    fobj.write(border + "\n")
    fobj.write(f"Total files scanned : {total_files} \n")
    fobj.write(border + "\n")
    fobj.write(f"Total Deleted files : {DuplicatesDeleted} \n")
    fobj.write(border + "\n")
    fobj.write(f"Log file is created at : {timestamp} \n")
    fobj.write(border + "\n")
    fobj.write(f"Starting time of directory scanning : {start_time} \n")
    fobj.write(f"Completion time of directory scanning : {stop_time} \n")
    fobj.write(f"Total time of operation : {stop_time - start_time} \n")
    fobj.write(border + "\n")
    fobj.close()

    fobj = open(Logfile, "rb")
    file_content = fobj.read()
    fobj.close()

    print(f"Log file is created with name : {LogfileName} in the {LogFileDirectory} directory")
    print("Total Deleted files : ", DuplicatesDeleted)

    sender = "5@gmail.com"
    receiver = email_address
    password = ""
    Subject = "Duplicate file remover update"

    body = f"""
    Dear Sir/Madam,

    Duplicate file remover automation script is providing you with the results of the deletion operation
    Please find the attached log file.
    
    Starting time of scanning: {start_time}
    Total number of files scanned: {total_files}
    Total number of duplicate files found: {TotalDuplicates}
    Total number of duplicate files deleted: {DuplicatesDeleted}
    Completion time of scanning: {stop_time}
    Name of scanned directory: {DirectoryName}

    Regards, 

    Duplicate file remover automation script
    """

    fobj = open(Logfile, "a")
    try:
        send_mail(sender, receiver, password, Subject, body, file_content, LogfileName)
        print("Mail has been sent successfully")

    except smtplib.SMTPAuthenticationError:
        fobj.write(f"Password or Username is not entered or is invalid")

    except smtplib.SMTPConnectError:
        fobj.write("Could not connect to the email server")

    except smtplib.SMTPServerDisconnected:
        fobj.write("Server disconnected unexpectedly")

    except smtplib.SMTPException:
        fobj.write("SMTP error occured")

    except Exception:
        fobj.write("Unexpected error")


    fobj.close()
    