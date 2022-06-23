# drrrbot
You can easily create a bot for http://drrrkari.com
## Useage
```sh
$ pip install git+https://github.com/yakisova41/drrrbot
```

```python
bot = Drrrbot(
    'name',#UserName
    'usa',#IconName
    'Useragent'#UserAgent
)
bot.roomLogin('exampleRoomid')
bot.roomSend('Hello!')
bot.roomLogout()

bot.exit()
```

## basic operation

### roomLogin
```python
bot.roomLogin('exampleRoomid')
```
Entering a roomid as the first argument allows you to enter that room

### roomLogout
```python
bot.roomLogout()
```
You can leave the room.

### roomSend
```python
bot.roomSend('message')
```
If you specify a string as the first argument, you can send that string as a message

### exit
```python
bot.exit()
```
Log out of drrrrkari.com

## getAllroom
Retrieve and parse information for all rooms

Information that can be obtained
- Room name
- Room members
- Number of people in room
- Roomstatus
    - 1 Can enter
    - 2 Can knock
    - 3 Can not
- Room id
```python
bot.getAllroom()

#return value =>>
#{
#   'kotei':[
#       {
#       'name':'Room name',
#       'member':['member1','member2']
#       'peoples':[2,15],//=> 2/15 
#       'status':1,
#       'roomid':'exampleRoomid'
#       },{...}...
#   ],
#   'zatsu':[...],
#   'narikiri':[...],
#   'bl':[...]
#}
```

## Functions for admin
The following functions are only available when you are the room admin


### roomKick
```python
bot.roomKick(targetUserID)
```
You can kick the target by entering the target userid string as the first argument


### roomNewhost
```python
bot.roomNewhost(targetUserID)
```
You can make the target a new administrator by entering the target's user ID string as the first argument


### roomNewname
```python
bot.roomNewname(name)
```
You can change the room name to a new one by entering the room name string as the first argument
