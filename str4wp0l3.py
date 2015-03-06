import urllib.request  # py3 is lame l0l
import random
import time
from threading import Thread


def vote(proxy, poll, c, d):
    try:
        try:
            print('proxy: ' + proxy, "id: " + poll, 'choice: ' + c)
            ip = '.'.join([str(random.randint(1, 255)) for _ in range(4)])  # generate random ip for header
            headers = {'X-Requested-With': 'XMLHttpRequest', 'X-Forwarded-For': ip}
            proxy = {"http": "http://%s" % proxy}
            proxy_support = urllib.request.ProxyHandler(proxy)
            opener = urllib.request.build_opener(proxy_support, urllib.request.HTTPHandler(debuglevel=1))
            urllib.request.install_opener(opener)
            #  found out how their api works, some1 halp
            urllib.request.Request('http://strawpoll.me/api/v2/polls/' + poll, {'votes': [c]}, headers)
        except urllib.request.URLError:
            print("Error grabbing URL")
    finally:
        time.sleep(float(d))


if __name__ == '__main__':
    print('str4wp0l3 by g19')

    pid = input('Poll ID: ')
    choice = input('Choice (0 is first): ')
    plist = input('Proxy list(ip:port): ')
    delay = int(input('Delay(s): '))

    print('Loading proxy list..')

    proxyFile = open(plist, 'r')
    proxies = []
    for p in proxyFile:
        proxies.append(p.strip())
    proxyFile.close()

    print(str(len(proxies)) + ' proxies loaded.')
    print('Starting..')

    for currProxy in proxies:
        t = Thread(target=vote, args=(currProxy, pid, choice, delay))
        t.start()

    print('Done.')
