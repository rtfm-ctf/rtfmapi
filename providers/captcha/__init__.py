# -*- coding: utf-8 -*-

import time
from rtfmapi.config import ConfigSectionMap

class Captcha(object):

    def __init__(self, captchasystem="deathbycaptcha", **kwargs):
        self.captchasystem=captchasystem
        self.kwargs = kwargs

        if self.captchasystem == 'deathbycaptcha':
            from . import deathbycaptcha
            self.config = ConfigSectionMap('deathbycaptcha')

        if self.captchasystem == 'deathbycaptcha' and not self.kwargs.get('method'):
            self.kwargs['method'] = 'SocketClient'

    def auth(self):
        print('[*] Captcha: Trying ' + self.config['method'] + ' method...')
        while True:
            if self.captchasystem == 'deathbycaptcha':
                try:
                    if self.config['method'] == 'SocketClient':
                        return deathbycaptcha.SocketClient(self.config['username'], self.config['password'])
                    else:
                        return deathbycaptcha.HttpClient(self.config['username'], self.config['password'])
                except Exception as e:
                    print(str(e))
                    if self.config['method'] == 'SocketClient':
                        self.newmethod = 'HttpClient'
                    elif self.config['method'] == 'HttpClient':
                       self.newmethod = 'SocketClient'
                    print('[*] Captcha: Method ' + self.config['method'] + ' failed, trying ' + self.newmethod + ' ...')
                    self.config['method'] = self.newmethod
    
    def report(self, captcha):
        if self.captchasystem in ['deathbycaptcha']:
            if self.config['report_incorrect_captcha']:
                self.client = self.auth()
                print('\n[*] Reporting incorrectly solved captcha, if this is happening too often, consider disabling it to prevent ban...')
                return self.client.report(captcha)
        

    def decode(self, filepath, timeout=15):
        ecount=0
        while True:
            
            print('[*] Captcha: using ' + self.captchasystem)

            if self.captchasystem == 'deathbycaptcha':
                self.client = self.auth()
                try:
                    print('[*] Captcha: current balance: ' + str(self.client.get_balance()))
                    print('[*] Cracking captcha...')
                    c = self.client.decode(filepath, timeout)
                    if c['status'] == 0:
                        return c['text']
                except Exception as e:
                    print(str(e))
                    ecount+=1
                    if ecount == 3:
                        print('\n[!] Too many errors, giving up...')
                        time.sleep(2)
                        raise Exception('Unrecoverable error in captcha system')
                    else:
                        if self.config['method'] == 'SocketClient':
                            self.newmethod = 'HttpClient'
                        elif self.config['method'] == 'HttpClient':
                            self.newmethod = 'SocketClient'
                        print('\n[!] Captcha: Method ' + self.config['method'] + ' failed, trying ' + self.newmethod + ' (%d/3) ...\n' % ecount)
                        self.config['method'] = self.newmethod
