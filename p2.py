import requests
import json

ar = [142,138,139,136,132,139,126,122,122,135,125,129,123,125,142,115,130,138,128,38,0,0,0,0,65,146,123,126,123,119,115,128,125,135,128,119,112,127,122,114,113,120,121,127,117,115,126,118,109,125,128,126,139,141,108,107,107,110,100,118,124,111,92,123,106,118,121,123,102,104,115,108,102,103,101,123,92,93,94,116]

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
f = open('words.txt', 'r')
cnt = 0
for id in range(1, 81): # 1..80
  data['id'] = l.readline()[:-1]
  for num in range(1, 201 - ar[id - 1]):
    data['word'] = f.readline()[:-1]
    headers['Referer'] = 'https://www.shanbay.com/wordbook/197200/' + data['id']
    r = requests.post(url, data=data, headers=headers)
    cnt += 1
    # s = json.loads(r.text);
    # print(s["data"]["wordlist"]["id"])
  print('Done ' + str(cnt))
  # TODO: count only the words that were added successfully
