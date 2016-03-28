'''General use RTFM API'''
import hug
from rtfmapi import modules

from rtfmapi.modules import osint
from rtfmapi.modules import exploit
from rtfmapi.modules import geo

@hug.cli()
@hug.extend_api('/geo')
def geo_api():
        return [geo]

@hug.cli
@hug.extend_api('/osint')
def osint_api():
        return [osint]

@hug.cli()
@hug.extend_api('/exploit')
def exploit_api():
        return [exploit]

#@hug.not_found()
#def not_found():
#    return {'Nothing': 'to see'}
