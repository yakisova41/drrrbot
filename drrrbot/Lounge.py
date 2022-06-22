import requests
from bs4 import BeautifulSoup

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
            
            selectedRoom = room.select('li.login > form > input')
            if not selectedRoom:
                roomid = False
            else:
                roomid = selectedRoom[0].attrs['value']

        datas.append({'name':room_name,'member':room_members,'peoples':room_members_count,'status':status,'roomid':roomid})
        
    return datas

def get_allroom(cookies, useragent):
    header = {
        'User-Agent':useragent
    }
    response = requests.get("http://drrrkari.com/lounge/", cookies=cookies, headers=header).text
    parsed = BeautifulSoup(response, "html.parser")

    kotei_rooms_elem = parsed.select('#fixed > ul.rooms')
    kotei = rooms_parser(kotei_rooms_elem)

    zatsu_rooms_elem = parsed.select('#zatsu > ul.rooms')
    zatsu = rooms_parser(zatsu_rooms_elem)

    narikiri_rooms_elem = parsed.select('#rp > ul.rooms')
    narikiri = rooms_parser(narikiri_rooms_elem)

    bl_rooms_elem = parsed.select('#bl > ul.rooms')
    bl = rooms_parser(bl_rooms_elem)

    return {
        'kotei':kotei,
        'zatsu':zatsu,
        'narikiri':narikiri,
        'bl':bl
    }