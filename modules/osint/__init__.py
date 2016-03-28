from rtfmapi.modules.osint.brazil import *
import hug

@hug.post('/brazil/cpf/query', output=hug.output_format.json)
def query_cpf(cpf:str, birth:str):
    from rtfmapi.modules.osint.brazil.query_cpf import QueryCPF
    '''Queries a CPF at Receita Federal'''
    qc = QueryCPF()
    return qc.query(cpf, birth)
