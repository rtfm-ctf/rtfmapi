import re

class CPF(object):
    def __init__(self, cpf):
        self.cpf = cpf

    def strip(self):
        return re.sub("[^0-9]", "", self.cpf)
    def format(self):
        cpf = self.strip()
        return "{}.{}.{}-{}".format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:11])

    def __repr__(self):
        return '{}'.format(self.cpf)
