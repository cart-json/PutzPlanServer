from Queries import Queries as QRY
import secrets
import json

class QueriesAsJson:

    
    def userToJson(user):
        return {'id': user[0], 'name': user[1], 'points': user[2], 'absent' : bool(user[5]), 'mainTask' : user[6]}
    
    def taskToJson(task):
        return {'id': task[0], 'name': task[1], 'points': task[2], 'mainTask' : task[3]}
    
    #######################################################################Setter
    def clear():
        QRY.clearPoints()
        QRY.setAllUndone()
        
    def setAbsent(userID):
        QRY.goAbsentByID(userID)
        
    def setPresent(userID):
        QRY.goPresentByID(userID)
    
    def login(username,password):
        user = QRY.checkLogin(username,password)
        result = []
        if user != None :
            auth = secrets.token_hex(15)
            QRY.setAuth(user[0],auth)
            result.append({ 'failed' : bool(0) , 'name' : user[1], 'id' : user[0] , 'points' : user[2] , 'authKey' : auth})
        else :
            result.append({'failed' : bool(1)})
        return result
        
    def update(taskID, authKey):
        user = QRY.getUserByAuthKey(authKey)
        subTask = QRY.getSubTaskByID(taskID)
        result = []
        if bool(subTask[3]):
            user = QRY.getUserByID(subTask[4])
            result = { 'failed' : bool(1) , 'user' : user[1], 'task' : subTask[1]}
        else:  
            QRY.setDone(taskID, user[0])
            QRY.setPoints(user[0], user[2] + subTask[2])
            result = { 'failed' : bool(0)}
            QRY.log(user,subTask)
        return result
    
    ############################################################################ Getter
    
    def getAllData(authKey):
            result = {}
            result["users"] = QueriesAsJson.getAllUsers()
            result["tasks"] = []
            result["lastWeek"] = QueriesAsJson.getLastWeek()
            result["tasks"].append(QueriesAsJson.getUserTasks(authKey))
            return(result)
        
    #Die Daten zu den Nutzern abgerufen und ins JSON Format transformiert
    def getAllUsers():
        userReply = QRY.getUsers()
        resultUsers= []
        for row in userReply:
            resultUsers.append(QueriesAsJson.userToJson(row))
        return resultUsers
        
    #Nur die Aufgaben des Nutzers werden abgerufen und ins JSON Format transformiert
    def getUserTasks(authKey):
        user = QRY.getUserByAuthKey(authKey)
        taskReply = QRY.getUserSubTasks(user[7])
        resultTasks = []
        for row in taskReply:
            resultTasks.append(QueriesAsJson.taskToJson(row))
        if not user[5]:
            resultTasks = resultTasks + QueriesAsJson.getAdditionalTasks()
        result = {'name': user[6], 'currentUser': {'name' : user[1], 'points' : user[2], 'absent' : bool(user[5])},
                  'subTasks': resultTasks}
        return result
        
        
    def getAdditionalTasks():
        taskReply = QRY.getAllSubTasksFromAbsentUsers()
        resultTasks = []
        for row in taskReply:
            resultTasks.append(QueriesAsJson.taskToJson(row))
        return resultTasks
    
    def getUserByAuthKey(authKey):
        return QRY.getUserByAuthKey(authKey)
        
    def authenticate(authKey):
        user = QueriesAsJson.getUserByAuthKey(authKey)
        result = []
        if user != None :
            result.append({ 'failed' : bool(0) , 'name' : user[1], 'id' : user[0] , 'points' : user[2]})
        else :
            result.append({'failed' : bool(1)})
        return result
        
    def getWeeklyResults():
        return QRY.getWeeklyResults()
    
    def getLastWeek():
        return QRY.getLastWeek()
    
    def getLogs():
        return QRY.getLogs();
        