import linecache
import addAppointment
import random
# adds random appointments to the data.txt file for testing
def addtest(repeats):
    for x in range(0,repeats):
        names = str(linecache.getline("randomThings/names.txt", random.randint(1, file_len("randomThings/names.txt")))[0:-1])
        classes = str(linecache.getline("randomThings/classes.txt",random.randint(1, file_len("randomThings/classes.txt")))[0:-1])
        addAppointment.addapp(classes + " " + str(random.randint(0, 999)), names, names + "@email.com",str(random.randint(1,12))+"-"+str(random.randint(1,28))+"-"+str(17), str(random.randint(1,1200)), str(random.randint(1201,2399)), "0")

addtest(100)