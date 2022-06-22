import requests
from bs4 import BeautifulSoup

def login(roomid, cookies, useragent, password = False):
    data = {
        'login':'login',
        'id':roomid
    }

    if(password != False):
        data['password'] = password
    
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/', data=data, cookies=cookies, headers=header)
    
    return response

def logout(cookies, useragent):
    data = {
        'logout':'logout'
    }
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/?ajax=1', data=data,cookies=cookies, headers=header)
    
    return response     

def send(text, cookies, useragent):
    data = {
        'valid':1,
        'message':text
    }
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/?ajax=1', data=data, cookies=cookies, headers=header)

    return response 

def new_host(uid, cookies, useragent):
    data = {
        'new_host':uid,
    } 
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/?ajax=1', data=data, cookies=cookies, headers=header)

    return response 

def room_name(name, cookies, useragent):
    data = {
        'room_name':name,
    } 
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/?ajax=1', data=data, cookies=cookies, headers=header)

    return response 

def knock(roomid, cookies, useragent):
    data = {
        'knock':'knock',
        'id':roomid
    } 
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/', data=data, cookies=cookies, headers=header)

    return response 

def kick(userId, cookies, useragent ):
    data = {
        'ban_user':userId,
    } 
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/room/', data=data, cookies=cookies, headers=header)

    return response 

def ajaxResponse(cookies, useragent):
    header = {
        'User-Agent':useragent
    }
    response = requests.post('http://drrrkari.com/ajax.php',cookies=cookies, headers=header)

    return response
