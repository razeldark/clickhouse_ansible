
#hp printers page count
import re
import requests
from bs4 import BeautifulSoup


ip_pool = (
'10.10.10.1',
'10.10.10.195',
'10.10.10.119',
'10.10.10.129',
'10.10.11.45',
'10.10.10.47',
'10.10.10.188',
'10.10.10.115',
'10.10.10.51',
'10.10.10.8',
'10.10.10.55',
'10.10.10.19',
'10.10.10.126',
'10.10.10.123',
'10.10.10.173',
'10.10.10.61',
'10.10.10.24',
'10.10.10.101',
'10.10.10.85',
'10.10.10.137'
 )
url = ()
url_http = 'http://'
url_https = 'https://'
url_tail = '/info_configuration.html?tab=Home&menu=DevConfig'
headers = {"Accept" : "text/html", "Content-Type": "text/html"}

for ip in ip_pool:
    try:
        url = url_http + ip + url_tail
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text,features="lxml")
        data = []
        item = {}
        rows = soup.find_all('tr')


        for row in rows:
            cells = row.find_all('td')
            cells = [ele.text.strip() for ele in cells]
            data.append([ele for ele in cells if ele])

        for i in range(len(data)):
            if data[i][0] == 'Серийный номер:': print('S/N: ', data[i][1], '\t', end='')
            if data[i][0] == ' Имя хоста:' or data[i][0] == 'Имя главн. комп.:': print(ip, data[i][1], '\t', end='')
            if data[i][0] == 'Всего оттисков:':
                print(data[i][0], '-', data[i][1], end=' ')
                pr = data[i][1]
            if data[i][0] == 'Ч/б отпечатки с копии:':
                print(data[i][0], '-', data[i][1], '\t',end='')
                cp = data[i][1]
                sum = int(pr) + int(cp)
                print('Всего напечатано страниц: ',sum)
                break
            
    except TimeoutError:
        url = url_https + ip + url_tail
        req = requests.get(url, headers=headers)
        soup = BeautifulSoup(req.text,features="lxml")
        data = []
        item = {}
        rows = soup.find_all('tr')


        for row in rows:
            cells = row.find_all('td')
            cells = [ele.text.strip() for ele in cells]
            data.append([ele for ele in cells if ele])

        for i in range(len(data)):
            if data[i][0] == 'Имя хоста:': print(ip, data[i][1], '\t', end='')
            if data[i][0] == ' Имя хоста:' or data[i][0] == 'Имя главн. комп.:': print(ip, data[i][1], '\t', end='')
            if data[i][0] == 'Всего оттисков:':
                print(data[i][0], '-', data[i][1])
                break
    except Exception as e:
        print(e)
