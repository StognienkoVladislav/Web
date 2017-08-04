
import urllib

url = 'http://api.site.com/method/'

values = {
    'argument1' : 'value1',
    'argument2' : 'value2'
}

headers = { 'User-Agent' : 'python urllib' }

data = urllib.urlencode(values)
req = urllib.Request(url, data, headers)

responce = urllib.urlopen(req)      #Отправ запрос и получ ответ
result = responce.read()            #Можем прочитать, получить статус ответа, заголовки
