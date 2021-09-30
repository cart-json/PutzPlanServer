from Server import Server
from ServerScheduler import ServerScheduler
from threading import*
from Datenbank import Datenbank as DB

DB.create()
  
threadServerScheduler = Thread(target=ServerScheduler.run)
threadServer = Thread(target=Server.run)
threadServerScheduler.start()
threadServer.start()
