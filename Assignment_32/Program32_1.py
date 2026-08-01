import schedule
import time

def create_files():
    
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    fname = "File_" + timestamp + ".txt"
    
    with open(fname, "w") as fobj:
        fobj.write(f"File name : {fname}\n")
        fobj.write(f"Creation time : {time.strftime('%H:%M:%s')}\n")
        fobj.write(f"Creation Date : {time.strftime('%Y:%m:%d')}\n\n")
  
def main():
    schedule.every(1).minute.do(create_files)

    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt as ke:
        print("Program execution terminated")        

if __name__ == "__main__":
    main()















    
