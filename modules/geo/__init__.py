from rtfmapi.modules.geo.ip import *
import hug


@hug.post('/ip/query')
def query_ip_geo_api(ip):
    from rtfmapi.modules.geo.ip.query_geo import GeoIP
    geo = GeoIP(ip)

    return geo.get_info()
