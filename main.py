'''General use RTFM API'''
import hug
from rtfmapi import modules


@hug.extend_api('/osint')
def osint_api():
        return [modules.osint]

@hug.not_found()
def not_found():
    return {'Nothing': 'to see'}
