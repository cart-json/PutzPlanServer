#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sqlite3 as lite
from Datenbank import Datenbank as DB
from WeeklyResultsFile import WeeklyResultsFile as WRF
from LogFile import LogFile as LF

class Queries:

########################################################################################Database queries
    #--------------------------------------------------------------------- Task Queries
    
    #Setter
    def setAllUndone():
        DB.query("""update SubTasks set done = false""", {})
    def setDone(taskID, userID):
        DB.query("""update SubTasks set done = true, doneBy = :userID where id = :id""", {'id': taskID, 'userID': userID})
    def setCurrentUser(mainTaskID, userID):
        DB.query("""update MainTasks set currentUser = :userID where id = :id""", {'id': mainTaskID, 'userID': userID})
    
    
    #Getter
    def getMainTasks():
        return DB.query("""select * from MainTasks""",{})
    def getSubTaskByID(id):
        return DB.queryOne("""select SubTasks.*, MainTasks.name
                                from SubTasks, MainTasks
                                where SubTasks.id = :id and MainTasks.id = SubTasks.mainTask""", {'id': id})
    def getUserSubTasks(mainTaskID):
        return DB.query("""select SubTasks.id, SubTasks.name, SubTasks.points, MainTasks.name
                                from SubTasks, MainTasks
                                where Subtasks.mainTask = :mainTaskID and done = false
                                and MainTasks.id = Subtasks.mainTask""", {'mainTaskID': mainTaskID})
    def getAllSubTasksFromAbsentUsers():
        return DB.query("""select SubTasks.id, SubTasks.name, SubTasks.points, MainTasks.name
                        from Users, SubTasks, MainTasks
                        where SubTasks.mainTask = MainTasks.id and MainTasks.currentUser = Users.id
                                and Users.absent = true and SubTasks.done = false""", {})
    #--------------------------------------------------------------------- User Queries
    #Setter
    def setAuth(userID, authKey):
        DB.query("""update Users set auth = :auth where id = :userID""", {'userID': userID, 'auth': authKey})
    def clearPoints():
        DB.query("""update Users set points = 0""", {})
    def setPoints(userID, points):
        DB.query("""update Users set points = :points where id = :id""", {'id': userID, 'points': points})
    def goAbsentByID(userID):
        DB.query("""update Users set absent = true where id = :userID""", {'userID': userID})
    def goPresentByID(userID):
        DB.query("""update Users set absent = false where id = :userID""", {'userID': userID})
        
        
    #Getter
    def getUserByAuthKey(authKey):
        return DB.queryOne("""select Users.*, MainTasks.name, MainTasks.id
                            from Users, MainTasks
                            where auth = :authKey and Users.id = MainTasks.currentUser""", {'authKey': authKey})
    def getUsers():
        return DB.query("""select Users.*, MainTasks.name from Users, MainTasks where Users.id = MainTasks.currentUser""",{})
    def getUserByID(id):
        return DB.queryOne("""select * from Users where Users.id = :id""", {'id': id})
    def checkLogin(username, password):
        #return self.queryOne("""select * from Users where id = 2""",{})
        return DB.queryOne("""select * from Users where Users.name = :username""",
                            {'username' : username})
#         return self.queryOne("""select * from Users where Users.name = :username and Users.password = :password""",
#                             {'username' : username, 'password' : password})
    
######################################################################################## File queries

    #Setter
    def log(user, task):
        LF.log(user,task)
    
    def updateWeeklyResults():
        users = Queries.getUsers()
        data = []
        for row in users:
            data.append({"name": row[1],"points": row[2], "mainTask": row[6]})
        WRF.update(data)
        

    #Getter
    def getWeeklyResults():
        return WRF.getFile()
    
    def getLastWeek():
        return WRF.getLastEntry()
    
    def getLogs():
        return LF.getLogs();
