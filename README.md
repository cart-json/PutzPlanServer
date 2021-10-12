# PutzPlanServer

The PutzPlan (german for cleaning plan) is a locally hosted web application, 
that is supposed to help me and my roommates managing cleaning task in our shared apartment.

It's a fun little project to repeat and train my knowledge in software design and engineering. 
This project is unfinished and therefor the documentation will be added later.

PutzPlanServer is the just back end, the front end can be found in another repository called PutzPlanClient (hereinafter referred to as 'client'). 

The PutzPlanServer is based on Python.

It uses an SQLite database to mananage the the state of the users and tasks and a json file to log the activity (when did which user finish which task).

One part of it's job is to process and answer the clients queries:
  - checking authentication keys or username and password
  - collecting and transfering all data, that is relevant for a specific user
  - updating the database and loging updates
The Second part are periodic jobs
  - redistributing tasks once a week (users switch their tasks randomly)
  - setting all tasks undone after a day (so every task can be done every day)




The user can authenticate himself, with username and password. If the authentication works, his tasks and other information(e.g. logs, presence of users) will be loaded from the server. He can finish a task, which will update the server and load the new data. He can declare another user as present or absent, which will update the server and load the new data. The tasks of an absent user will be available for everyone, the tasks of a present user are only available for him.

This is just the basic functionality and will be described more detailed in the future.
