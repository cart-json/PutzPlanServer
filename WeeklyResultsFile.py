import json

class WeeklyResultsFile:
    
    path = "data/weeklyResults.txt"
    exists = False
    
    def create():
        writeFile = open(WeeklyResultsFile.path, "a")
        readFile = open(WeeklyResultsFile.path, "r")
        if readFile.read() == "":
            writeFile.write("[]")
        writeFile.close()
        WeeklyResultsFile.exists = True
        
    
    def update(update):
        if not WeeklyResultsFile.exists:
            WeeklyResultsFile.create()
        with open(WeeklyResultsFile.path, "r+") as file:
            data_file = json.load(file)
            data_file.append(update);
            file.seek(0)
            json.dump(data_file,file);
    
    def getLastEntry():
        if not WeeklyResultsFile.exists:
            WeeklyResultsFile.create()
        with open(WeeklyResultsFile.path, 'r+') as file:
            data_file = json.load(file)
            length = len(data_file)
            if length == 0:
                lastEntry = []
            else:
                lastEntry = data_file[len(data_file)-1]
        return lastEntry
        
        
    
