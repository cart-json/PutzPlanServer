from Datenbank import Datenbank as DB
import sqlite3 as lite
import secrets
import schedule
import time
import json
from Queries import Queries as QRY
from QueriesAsJson import QueriesAsJson as QAJ
from random import randrange
from ServerScheduler import ServerScheduler
import threading
from datetime import datetime
from WeeklyResultsFile import WeeklyResultsFile as WRF
from LogFile import LogFile as LF
from flask import jsonify
# 
# user = QRY.checkLogin('Leo','')
# 
# print(type((QRY.getLastWeek())))


# con = lite.connect("data/ppDB.db")
# cur = con.cursor()
# cur.execute("""select *
#                         from Users, MainTasks
#                         where MainTasks.currentUser = Users.id and Users.absent = true""")
# 
# result = cur.fetchall()
# con.commit()
# con.close()

path = "data/weeklyResults.txt"
    

users = QRY.getUsers()
update = []
for row in users:
    update.append({"name": row[1],"points": row[2], "mainTask": row[6]})
with open(path, "r+") as file:
    data_file = json.load(file)
    #data = {update}
    #data["week" + str(len(data_file["weeklyResults"]))] = update
    data_file.append(update);
    file.seek(0)
    json.dump(data_file,file);


# cur.execute("""
#     create table SubTasks (id integer primary key, name varchar(20),
#         points integer, done bool, doneBy integer references user, mainTask integer references MainTask)
# """)
# cur.execute("""
#     create table Users (id integer primary key, name varchar(20),
#         points integer, auth varchar, password varchar(20))
# """)
# cur.execute("""
#     create table MainTasks (id integer primary key, name varchar(20),
#         currentUser integer references Users)
# """)
# cur.execute("""
#     update Users set password = '33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2'
#         
# """)
# cur.execute("""
#     alter table SubTasks add mainTask integer references MainTask
# """)
# cur.execute("""
#     insert into Users (id, name, points, password)
#     values
#         (1,'Clemens',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2'),
#         (2,'Johannes',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2'),
#         (3,'Leo',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2'),
#         (4,'Nick',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2'),
#         (5,'Robin',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2')
# 
# """)
# cur.execute("""
#     insert into MainTasks (id, name, currentUser)
#     values
#         (1,'Küche',1),
#         (2,'Bad-unten',2),
#         (3,'Bad-oben',3),
#         (4,'Böden',4),
#         (5,'Putzen',5)
# """)
# cur.execute("""
#     insert into SubTasks (id, name, points, done, doneBy, mainTask)
#     values
#         (1,'Müll',1,false,0,1),
#         (2,'Oberflächen, Spüle',1,false,0,1),
#         (3,'Spülmaschiene ausräumen',1,false,0,1),
#         (4,'Kühlschrank',6,false,0,1),
#         (5,'Gebläse',3,false,0,1),
#         (6,'Duschkabine',6,false,0,2),
#         (7,'Boden',6,false,0,2),
#         (8,'Toilette',2,false,0,2),
#         (9,'Müll',2,false,0,2),
#         (10,'Waschbecken',2,false,0,2),
#         (11,'Duschkabine',6,false,0,3),
#         (12,'Boden',6,false,0,3),
#         (13,'Toilette',2,false,0,3),
#         (14,'Müll',2,false,0,3),
#         (15,'Waschbecken',2,false,0,3),
#         (16,'Saugen',5,false,0,4),
#         (17,'Saugen und Wischen',10,false,0,4),
#         (18,'Wohnzimmer abstauben',3,false,0,5),
#         (19,'Pflanzen wässern',3,false,0,5),
#         (20,'Flaschen wegbringen',3,false,0,5)
# """)
# cur.execute("""
#     drop table MainTasks
# """)
# cur.execute("""
#     drop table SubTasks
# """)
# cur.execute("""
#     drop table Users
# """)
# cur.execute("""
#     PRAGMA table_info(Users)
# """)
