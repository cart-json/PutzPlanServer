import sqlite3 as lite

class Datenbank:
    
    path = 'data/ppDB.db'
    
    def query(text, dictionary):
        con = lite.connect(Datenbank.path)
        cur = con.cursor()
        cur.execute(text, dictionary)
        result = cur.fetchall()
        con.commit()
        con.close()
        return result
    
    def queryOne(text, dictionary):
        con = lite.connect(Datenbank.path)
        cur = con.cursor()
        cur.execute(text, dictionary)
        result = cur.fetchone()
        con.commit()
        con.close()
        return result
    
    def create():
        con = lite.connect(Datenbank.path)
        cur = con.cursor()
        cur.execute("""select * from sqlite_master""")
        
        if cur.fetchone() == None:
            
            cur.execute("""
                create table SubTasks (id integer primary key, name varchar(20),
                    points integer, done bool, doneBy integer references user, mainTask integer references MainTask)
            """)
            con.commit()
            cur.execute("""
                create table Users (id integer primary key, name varchar(20),
                    points integer, auth varchar, password varchar(20), absent bool)
            """)
            con.commit()
            cur.execute("""
                create table MainTasks (id integer primary key, name varchar(20),
                    currentUser integer references Users)
            """)
            con.commit()
            cur.execute("""
                insert into Users (id, name, points, password, absent)
                values
                    (1,'Clemens',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2',false),
                    (2,'Johannes',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2',false),
                    (3,'Leo',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2',false),
                    (4,'Nick',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2',false),
                    (5,'Robin',0,'33c5ebbb01d608c254b3b12413bdb03e46c12797e591770ccf20f5e2819929b2',false)
                    """)
            con.commit()
            cur.execute("""
                insert into MainTasks (id, name, currentUser)
                values
                    (1,'Küche',1),
                    (2,'Bad-unten',2),
                    (3,'Bad-oben',3),
                    (4,'Böden',4),
                    (5,'Putzen',5)
            """)
            con.commit()
            cur.execute("""
                insert into SubTasks (id, name, points, done, doneBy, mainTask)
                values
                    (1,'Müll',1,false,0,1),
                    (2,'Oberflächen, Spüle',1,false,0,1),
                    (3,'Spülmaschiene ausräumen',1,false,0,1),
                    (4,'Kühlschrank',6,false,0,1),
                    (5,'Gebläse',3,false,0,1),
                    (6,'Duschkabine',6,false,0,2),
                    (7,'Boden',6,false,0,2),
                    (8,'Toilette',2,false,0,2),
                    (9,'Müll',2,false,0,2),
                    (10,'Waschbecken',2,false,0,2),
                    (11,'Duschkabine',6,false,0,3),
                    (12,'Boden',6,false,0,3),
                    (13,'Toilette',2,false,0,3),
                    (14,'Müll',2,false,0,3),
                    (15,'Waschbecken',2,false,0,3),
                    (16,'Saugen',5,false,0,4),
                    (17,'Saugen und Wischen',10,false,0,4),
                    (18,'Wohnzimmer abstauben',3,false,0,5),
                    (19,'Pflanzen wässern',3,false,0,5),
                    (20,'Flaschen wegbringen',3,false,0,5)
            """)
            con.commit()
        con.close()