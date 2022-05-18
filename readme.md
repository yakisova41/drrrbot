# drrrbot
You can easily create a bot for http://drrrkari.com
## Useage
```sh
$ pip install git+https://github.com/yakisova41/drrrbot
```

```python
from drrrbot import User
from drrrbot import Room
from drrrbot import Rounge

login = User.login('name','usa')
rooms = Lounge.get_allroom(login)
target = rooms['zatsu'][0]

Room.login(target['roomid'],login)
Room.send('hello',login)
Room.logout(login)
```

## IF blocked access?
![Screenshot from 2022-04-23 23-24-11](https://user-images.githubusercontent.com/75610521/169055115-37f93c66-10ca-4316-bfc1-9e7e4759de87.png)

Rest assured.
This is happening because cloudflare is blocking your useragent

### How to create a bot with any useragent
```python
useragent = "super ultra internet explorer"
Room.login(target['roomid'],login,useragent)
```
ok!
