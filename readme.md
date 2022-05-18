# drrrbot
You can make a bot for http://drrrkari.com with this package
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
