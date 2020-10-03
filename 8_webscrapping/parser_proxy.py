import  requests
from bs4 import BeautifulSoup #pip3 install bs4, lxml
from random import choice

def get_html(url, useragent=None, proxy=None):
    print(">>>>>>>>Get_html<<<<<<<<<")
    r = requests.get(url, headers=useragent, proxies=proxy)
    return r.text

def get_ip(html):
    soup = BeautifulSoup(html, 'lxml')
    ip = soup.find('div', class_='ip').text.strip()
    ua = soup.find('div', class_='details_browser_data').text.strip()
    print(ip)
    print(ua)
    print("..........................")

def main():
    # url = 'http://sitespy.ru/my-ip'
    url = 'http://hidemy.name/ru/what-is-my-ip/'
    useragents = open('useragents.txt').read().split('\n')
    proxies = open('proxies').read().split('\n')

    for i in range(5):
        proxy = {'http': 'http://' + choice(proxies)}
        useragent = {'User-Agent': choice(useragents)}
        try: 
            html = get_html(url, useragent, proxy)
        except:
            continue
        if html != '':
            get_ip(html)



if __name__ == '__main__':
    main()