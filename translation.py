# FAILD

import urllib.request
import urllib.parse

content = input('Please input your words to translate: ')
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4068.4 Safari/537.36'

data = {}
# data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
# data['xmlVersion'] = '1.6'
# data['keyfrom'] = 'fanyi.web'
# data['ue'] = 'UTF-8'
# data['typoResult'] = 'true'
urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data, head)
html = response.read().decode('utf-8')

print(html)
