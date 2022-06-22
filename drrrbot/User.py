import requests
from bs4 import BeautifulSoup

def login(UserName, UserIcon, UserAgent):
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

def logout(cookies, UserAgent):
  headers ={
    'User-Agent': UserAgent
  }

  requests.post('http://drrrkari.com/logout/',headers=headers,cookies=cookies)