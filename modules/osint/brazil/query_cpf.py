'''Brazil's CPF status checker'''

import sys
import hmac
import hashlib
import requests
from bs4 import BeautifulSoup as bs
import pprint
from dateutil.parser import parse as dtparse
from rtfmapi.providers.captcha import Captcha
from rtfmapi.validators.cpf import CPF
from rtfmapi.config import ConfigSectionMap
import json
import hug

class QueryCPF(object):
    bypass_url = 'https://movel01.receita.fazenda.gov.br/servicos-rfb/v2/IRPF/cpf'
    bypass_secret = 'Sup3RbP4ssCr1t0grPhABr4sil'
    url = 'http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/consultapublica.asp'
    post_url = 'http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/ConsultaPublicaExibir.asp'
    captcha_url = 'http://www.receita.fazenda.gov.br/aplicacoes/atcta/cpf/captcha/gerarCaptcha.asp'
    config = ConfigSectionMap('hyadesinc_query_cpf')
 
    def __init__(self):
        # Possible methods are (bypass, crack). Bypass is better in every way
        self.method = self.config['method']
        self.session = requests.Session()

    def query(self, cpf, birth):
        '''Queries a CPF at Receita Federal'''
        cpf = CPF(cpf)
        birth = dtparse(birth)

        if self.method == 'crack':
            captcha = ''
            r = self.session.get(self.captcha_url, stream=True)
            if r.status_code == 200:
                with open('/tmp/teste.png', 'wb') as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                c = Captcha('deathbycaptcha')
                captcha = c.decode('/tmp/teste.png')
            else:
                return False

            payload = {'txtTexto_captcha_serpro_gov_br': captcha, 'tempTxtCPF': cpf.format(), 'tempTxtNascimento':
                    birth.strftime('%d/%m/%Y'),
                    'temptxtToken_captcha_serpro_gov_br': '', 'temptxtTexto_captcha_serpro_gov_br': captcha}
            r = self.session.post(self.post_url, data=payload)

            soup = bs(r.content, 'lxml')

            obj = {}
            obj['death_year'] = None
            obj['death_message'] = None
            obj['cpf'] = cpf.format()
            obj['birth'] = birth.strftime('%Y/%m/%d')

            for span in soup.find_all('span', {'class': 'clConteudoDados'}):
                text = span.text.strip()
                value = text.split(':')[1].strip()
                if text.startswith('Nome da Pessoa'):
                    obj['name'] = value
                elif text.startswith('Situa') and 'Cadastral' in text:
                    obj['situation'] = value
                elif text.startswith('Data da Inscri'):
                    obj['subscription_date'] = dtparse(value.replace('anterior a', '')).strftime('%Y/%m/%d')
                elif text.startswith('Digito Verificador'):
                    obj['verification_digit'] = value
                elif 'digo de controle do comprovante' in text:
                    obj['control_code'] = value
        elif self.method == 'bypass':
            # Inspired by http://hc0der.blogspot.com.br/2014/09/bypass-captcha-da-receita-federal.html
            token_string = '{}{}'.format(cpf.cpf,birth.strftime('%d%m%Y'))
            token = hmac.new(self.bypass_secret.encode('utf-8'), token_string.encode('utf-8'), hashlib.sha1) 
            headers = {'token': token.hexdigest(), 'plataforma': 'iPhone OS', 'dispositivo': 'iPhone', 'aplicativo':
                    'Pessoa Física', 'versao': '8.3', 'versao_app': '4.1', 'Content-Type':
                    'application/x-www-form-urlencoded'}
            payload = 'cpf={}&dataNascimento={}'.format(cpf.cpf, birth.strftime('%d%m%Y'))
            r = self.session.post(self.bypass_url, headers=headers, data=payload, verify=False)

            data = r.json()

            obj = {}

            obj['cpf'] = cpf.format()
            obj['birth'] = birth.strftime('%Y/%m/%d')
            obj['name'] = data['nome']
            obj['situation'] = data['descSituacaoCadastral']
            obj['subscription_date'] = dtparse(data['dataIsncricao'].replace('anterior a', '')).strftime('%Y/%m/%d')
            obj['death_year'] = data['anoObito']
            obj['death_message'] = data['mensagemObito']
            obj['control_code'] = data['codigoControle']
            obj['verification_digit'] = data['digitoVerificador']
            obj['return_message'] = data.get('mensagemRetorno', None)

        return obj


@hug.post('/query/cpf', output=hug.output_format.json)
def query_cpf(cpf:str, birth:str):
    '''Queries a CPF at Receita Federal'''
    qc = QueryCPF()
    return qc.query(cpf, birth)


if __name__ == '__main__':
    qc = QueryCPF()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(qc.query(sys.argv[1], sys.argv[2]))
