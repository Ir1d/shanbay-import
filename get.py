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
  # 'Content-Length': '44',
  'Cookie': 'enter your own cookie', # enter your own cookie
  'Connection': 'keep-alive',
}
url = 'https://www.shanbay.com/api/v1/wordbook/wordlist/'
data = {'name': 'value1', 'description': 'value2', 'wordbook_id': '197200'}

for i in range(1, 81): # 1..80
  data['name'] = 'Chapter' + str(i)
  data['description'] = 'Chapter' + str(i)
  r = requests.post(url, data=data, headers=headers)
  s = json.loads(r.text);
  print(s["data"]["wordlist"]["id"])