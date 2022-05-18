import requests
from bs4 import BeautifulSoup

class Room:
    def login(roomid, cookies, useragent = "a"):
        data = {
            'login':'login',
            'id':roomid
        }
        header = {
            'User-Agent':useragent
        }
        response = requests.post('http://drrrkari.com/room/', data=data, cookies=cookies, headers=header)
        
        return response

    def logout(cookies, useragent = "a"):
        data = {
            'logout':'logout'
        }
        header = {
            'User-Agent':useragent
        }
        response = requests.post('http://drrrkari.com/room/?ajax=1', data=data,cookies=cookies, headers=header)
        
        return response     

    def send(text, cookies, useragent = "a"):
        data = {
            'valid':1,
            'message':text
        }
        header = {
            'User-Agent':useragent
        }
        response = requests.post('http://drrrkari.com/room/?ajax=1', data=data, cookies=cookies, headers=header)

        return response 

    def knock(roomid, cookies, useragent = "a"):
        data = {
            'knock':'knock',
            'id':roomid
        } 
        header = {
            'User-Agent':useragent
        }
        response = requests.post('http://drrrkari.com/room/', data=data, cookies=cookies, headers=header)

        return response 

class Lounge:
    def rooms_parser(elem):
        datas = []

        for room in elem:
            room_name = room.select('li.name')[0].text

            room_members_count = room.select('li.member')[0].text.split('/')
            key = 0
            for count in room_members_count:
                room_members_count[key] = int(count)
                key = key + 1

            room_members_elem = room.select('li.users > ul > li')
            room_members = []
            for member in room_members_elem:
                room_members.append(member.text)
            
            if(len(room.select('li.login > .full')) == 1):
                status = 3
                roomid = False
            else:
                if(len(room.select('li.login > form > button[name="knock"]')) == 1):
                    status = 2
                else:
                    status = 1

                roomid = room.select('li.login > form > input')[0].attrs['value']

            datas.append({'name':room_name,'member':room_members,'peoples':room_members_count,'status':status,'roomid':roomid})
            
        return datas

    def get_allroom(cookies):
        response = requests.get("http://drrrkari.com/lounge/", cookies=cookies).text
        parsed = BeautifulSoup(response, "html.parser")

        kotei_rooms_elem = parsed.select('#fixed > ul.rooms')
        kotei = Lounge.rooms_parser(kotei_rooms_elem)

        zatsu_rooms_elem = parsed.select('#zatsu > ul.rooms')
        zatsu = Lounge.rooms_parser(zatsu_rooms_elem)

        narikiri_rooms_elem = parsed.select('#rp > ul.rooms')
        narikiri = Lounge.rooms_parser(narikiri_rooms_elem)

        bl_rooms_elem = parsed.select('#bl > ul.rooms')
        bl = Lounge.rooms_parser(bl_rooms_elem)

        return {
            'kotei':kotei,
            'zatsu':zatsu,
            'narikiri':narikiri,
            'bl':bl
        }

class User:
  def login(UserName, UserIcon, UserAgent = "a"):
    session = requests.session()
    TokenResponse = session.get('http://drrrkari.com/')
    soup = BeautifulSoup(TokenResponse.text, 'html.parser')
    token = soup.select('input[type="hidden"]')[3]['value']
    cookies = TokenResponse.cookies.get_dict()

    payload = {
      'language': 'ja-JP',
      'icon': UserIcon,
      'name': UserName,
      'login': 'login',
      'token': token
    }

    headers ={
        'User-Agent': UserAgent
    }
    
    session.post('http://drrrkari.com/',data=payload,headers=headers,cookies=cookies)
    
    return cookies
