import random
import linecache
# add appointment
def addapp(subject,tutor,comm,date,start,end,cost):
    dataFile = open("data.txt", "a")
    dataFile.write("#" + "subject:"+subject+"\n")
    dataFile.write(">" + "tutor:"+tutor+"\n")
    dataFile.write(">" + "client:"+"N/A"+"\n")
    dataFile.write(">" + "comm:"+comm+"\n")
    dataFile.write(">" + "date:"+date+"\n")
    dataFile.write(">" + "start:"+start+"\n")
    dataFile.write(">" + "end:"+end+"\n")
    dataFile.write(">" + "cash:"+cost+"\n")
    dataFile.close()


# gets the number of files in a file
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

