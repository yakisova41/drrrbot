from drrrbot import User
from drrrbot import Room
from drrrbot import Lounge
import json

class Drrrbot:
# このクラスのコンストラクタでログイン処理(drrrbot.lib.User.login())を行い、
# self.userAgent,self.loginCookie変数にそれぞれログイン時の情報を代入します。
# クラスのインスタンス破壊時またはexit()関数の実行時にlogoutURLへPOSTを送信します。

    def __init__(self, userName, userIcon, userAgent = ' '):
        loginCookie = User.login(userName, userIcon, userAgent)

        self.userAgent = userAgent
        self.loginCookie = loginCookie
        self.roomLoginStatus = False

    def getAllroom(self):
        if(self.roomLoginStatus == False):
            return Lounge.get_allroom(self.loginCookie, self.userAgent)
        else:
            return {}

    def roomKnock(self, roomid):
        if(self.roomLoginStatus == False):
            return Room.knock(roomid, self.loginCookie, self.userAgent)
        else:
            return False

    def roomLogin(self, roomid, password = False):
        if(self.roomLoginStatus == False):
            self.roomLoginStatus = True
            return Room.login(roomid, self.loginCookie, self.userAgent, password)
        else:
            return False

    def roomLogout(self):
        if(self.roomLoginStatus):
            self.roomLoginStatus = False
            return Room.logout(self.loginCookie, self.userAgent)
        else:
            return False

    def roomSend(self, message):
        if(self.roomLoginStatus):
            return Room.send(message, self.loginCookie, self.userAgent)
        else:
            return False

    def roomNewhost(self, uid):
        if(self.roomLoginStatus):
            return Room.new_host(uid, self.loginCookie, self.userAgent)
        else:
            return {}

    def roomNewname(self, name):
        if(self.roomLoginStatus):
            return Room.room_name(name, self.loginCookie, self.userAgent)
        else:
            return {}
        
    def roomKick(self, uid):
        if(self.roomLoginStatus):
            return Room.kick(uid, self.loginCookie, self.userAgent)
        else:
            return False

    def getAllRoomData(self):
        if(self.roomLoginStatus):
            responsejson = Room.ajaxResponse(self.loginCookie, self.userAgent).text
            return  json.loads(responsejson)
        else:
            return {} 

    def exit(self):
        return User.logout(self.loginCookie, self.userAgent)
    
    def __del__(self):
        User.logout(self.loginCookie, self.userAgent)
        
class DrrrbotDataParse:
# このクラスはDrrrbotクラスのgetAllRoomData()関数が取得したRoomデータを
# 処理しやすい形に整形するクラスです。
# 必ずimportする必要はありません

    #ユーザー情報をユーザー名をkeyにした状態の辞書にしてreturn
    def users(data):
        users = data['users']

        parsed = {}

        for user in users:
            user = users[user]
            parsed[user['name']] = user
        
        return parsed
