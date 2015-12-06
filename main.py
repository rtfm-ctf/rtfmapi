'''General use RTFM API'''
import hug
from rtfmapi.modules.hyadesinc import query_cpf, query_geo
from rtfmapi.modules.mthbernardes import query_shellshock


@hug.extend_api('/query/cpf')
def query_cpf_api():
    '''Queries CPFs at Receita Federal'''
    return [query_cpf]

@hug.extend_api('/query/shellshock')
def query_shellshock_api():
    '''Finds shellshock-vulnerable hosts'''
    return [query_shellshock]

@hug.extend_api('/query/ip/geo')
def query_geo_ip_api():
    '''Get IP GEO information'''
    return [query_geo]


#@hug.not_found()
#def not_found():
#    return {'Nothing': 'to see'}
