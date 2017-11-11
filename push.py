import requests
import json

headers = {
  'Host': 'www.shanbay.com',
  'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0',
  'Accept': '*/*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate, br',
  'Referer': 'https://www.shanbay.com/wordbook/197200/',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'Content-Length': '20',
  'Cookie': 'enter your own cookie', # enter your own cookie
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

url = 'https://www.shanbay.com/api/v1/wordlist/vocabulary/'
data = {'id': '591136', 'word': 'digit'}

l = open('list.txt', 'r')
for id in range(1, 81): # 1..80
  data['id'] = l.readline()[:-1]
  f = open('gen/' + str(id) + '.txt', 'r')
  for num in range(1, 201):
    data['word'] = f.readline()[:-1]
    headers['Referer'] = 'https://www.shanbay.com/wordbook/197200/' + data['id']
    r = requests.post(url, data=data, headers=headers)
    # s = json.loads(r.text);
    # print(s["data"]["wordlist"]["id"])
  print('Done ' + str(id))