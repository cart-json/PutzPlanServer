import json
from datetime import datetime

class LogFile:
    
    path = "data/log.txt"
    exists = False
#     pathTemp = "temporaryLog.txt"
#     existsTemp = False
    
    def create():
        writeFile = open(LogFile.path, "a")
        readFile = open(LogFile.path, "r")
        if readFile.read() == "":
            writeFile.write("[]")
        writeFile.close()
        LogFile.exists = True
        
    
    def log(user, subTask):
        current_time = str(datetime.now())
        if not LogFile.exists:
            LogFile.create()
        with open(LogFile.path, "r+") as file:
            data_file = json.load(file)
            dictionary = {'time' : current_time, 'userName' : user[1], 'userID' : user[0], 'mainTask' : subTask[6],
                          'task' : subTask[1], 'pointsGained' : subTask[2]}
            data_file.append(dictionary);
            file.seek(0)
            json.dump(data_file,file);
            
    def getFile():
        if not LogFile.exists:
            LogFile.create()
        with open(LogFile.path, 'r+') as file:
            data_file = json.load(file)
        return data_file
    
    def getLogs():
        file = LogFile.getFile()
        return file
        
        
#     def getLastEntry():
#         if not JsonFile.exists:
#             JsonFile.create()
#         with open(JsonFile.path, 'r+') as file:
#             data_file = json.load(file)
#             lastEntry = data_file["weeklyResults"][len(data_file["weeklyResults"])-1]["week" + str(len(data_file["weeklyResults"])-1)]
#         return lastEntry