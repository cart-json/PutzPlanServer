from flask import Flask, request
from flask import jsonify
from QueriesAsJson import QueriesAsJson as QAJ
from threading import *

class Server:

    app = Flask(__name__)
    
    @app.route("/data")
    def psuhData():
        authKey = request.args.get('authKey')
        if QAJ.getUserByAuthKey(authKey) == None:
            print({ 'failed' : bool(1), 'message': 'wrong authKey'})
            return(jsonify({ 'failed' : bool(1), 'message': 'wrong authKey'}))
        else:
            result = QAJ.getAllData(authKey)
            return(jsonify(result))

    @app.route("/data/logs")
    def pushLogs():
        if QAJ.getUserByAuthKey(request.args.get('authKey')) != None:
            result = QAJ.getLogs()
            return jsonify(result)
        else:
            print({ 'failed' : bool(1), 'message': 'wrong authKey'})
            return(jsonify({ 'failed' : bool(1), 'message': 'wrong authKey'}))

    @app.route("/update")
    def update():
        authKey = request.args.get('authKey')
        result = ''
        typ = request.args['UpdateType']
        result = [{'failed' : bool(0)}]
        if QAJ.getUserByAuthKey(authKey) == None:
            result = ({ 'failed' : bool(1), 'message': 'wrong authKey'})
            print(result)
        elif typ == 'TaskDone':
            task = request.args.get('TaskKey')
            result = QAJ.update(int(task),authKey)
        elif typ == 'setAbsent':
            userID = request.args.get('userID')
            QAJ.setAbsent(userID)
        elif typ == 'setPresent':
            userID = request.args.get('userID')
            QAJ.setPresent(userID)
        elif typ == 'Clear' :
            QAJ.clear()
        return jsonify(result)
    
    @app.route("/login")
    def login():
        username = request.args.get('username')
        password = request.args.get('password')
        return jsonify(QAJ.login(username,password))

    @app.route("/authenticate")
    def auth():
        authKey = request.args.get('authKey')
        return jsonify(QAJ.authenticate(authKey))

    @app.route("/getWeeklyResults")
    def getWeeklyResults():
        authKey = request.args.get('authKey')
        if QAJ.getUserByAuthKey(authKey) == None:
            return(jsonify({ 'failed' : bool(1), 'message': 'wrong authKey'}))
        return jsonify(QAJ.getWeeklyResults())

    @app.route("/getLastWeekResults")
    def getLastWeekResults():
        authKey = request.args.get('authKey')
        if QAJ.getUserByAuthKey(authKey) == None:
            result = jsonify({ 'failed' : bool(1), 'message': 'wrong authKey'})
        result = jsonify(QAJ.getLastWeek())
        return result

    def run():
        app = Server.app
        app.run(host="0.0.0.0", port=8500)
