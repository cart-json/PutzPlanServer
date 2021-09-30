from Queries import Queries as QRY
import schedule
import time
import json
from random import randrange

class ServerScheduler:
        
    def redistributeTasks():
        users = QRY.getUsers()
        tasks = QRY.getMainTasks()
        for i in range(0,len(users)):
            user = users[randrange(len(users))]
            QRY.setCurrentUser(tasks[i][0],user[0])
            users.remove(user)
            
        
    def clearWeek():
        global week
        QRY.updateWeeklyResults()
        ServerScheduler.redistributeTasks()
        QRY.clearPoints()
        QRY.setAllUndone()
        print('weekCleared')
        
    def clearDay():
        QRY.clearPoints()
        QRY.setAllUndone()
        print('dayCleared')


    def run():    
        schedule.every(600).seconds.do(ServerScheduler.clearWeek)
    #schedule.every(20).seconds.do(clearDay)

    #schedule.every().moday.at("01:00").do(clearWeek)

        while 1:
           schedule.run_pending()
           time.sleep(1)

