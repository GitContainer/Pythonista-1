import requests
import re

# coding=utf-8
baseurl = 'http://www.heibanke.com/lesson/crawler_ex00/'
ruler = re.compile(r'数字[^\d]*(\d+)[\.<]')
index = 1

html = requests.get(baseurl).content
with open('/home/huang/ytkdoc/a.txt', 'wb') as file:
    file.write(html)
# print(html)
number = ruler.findall(html.decode('utf-8'))
print(number)
while number:
    willurl = baseurl + number[0]
    html = requests.get(willurl).content
    number = ruler.findall(html.decode('utf-8'))
    print('访问网页%d:%s' % (index, willurl))
    index += 1

else:
    print('下一关开始:%s' % willurl)
