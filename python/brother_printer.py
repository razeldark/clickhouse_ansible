#brother printers page count
import re
import requests
from bs4 import BeautifulSoup


ip_pool = ('10.10.10.117' , '10.10.10.136' , '10.10.10.142', '10.10.10.147', '10.10.10.152')

url_info = ()
url_net = ()

url_http = 'http://'
url_tail_info = '/general/information.html'
url_tail_net = '/net/net/net.html'
headers = {"Accept" : "text/html", "Content-Type": "text/html"}

for i in ip_pool: 
    url_info = url_http + i + url_tail_info
    url_net = url_http + i  + url_tail_net
    req_info = requests.get(url_info, headers=headers)
    soup_info = BeautifulSoup(req_info.text,features="lxml")
    req_net = requests.get(url_net, headers=headers)
    soup_net = BeautifulSoup(req_net.text,features="lxml")
    for i in soup_info('dt'):
        if i.string == 'Copy':
            print(i.string, ' - ',i.next_sibling.text , end='\t')
        if i.string == 'Print':
            print(i.string, ' - ',i.next_sibling.text , end='\t')
            for j in soup_net('dd'):
                if j.previous_sibling.string == "Node Name":
                    print(j.string, ' - ', url_info, end='\n')
        if i.string == 'Page Counter':
            print(i.string, ' - ',i.next_sibling.text , end='\t')
