import hug
import requests

class GeoIP(object):
    hostname = None
    asnumber = None
    country = None
    country_code = None
    region = None
    city = None
    postal_code = None
    isp = None
    organization = None
    timezone = None
    maps = None

    def __init__(self, ip):
        self.ip = ip
        self.get_info()


    def __dict__(self):
        obj = {}
        obj['ip'] = self.ip
        obj['hostname'] = self.hostname
        obj['asnumber'] = self.asnumber
        obj['country'] = self.country
        obj['country_code'] = self.country_code
        obj['region'] = self.region
        obj['city'] = self.city
        obj['postal_code'] = self.postal_code
        obj['isp'] = self.isp
        obj['organization'] = self.organization
        obj['timezone'] = self.timezone
        obj['maps'] = self.maps

        return obj


    def get_info(self):
        r = requests.get('http://api.predator.wtf/geoip/?arguments={}'.format(self.ip))

        lines = r.content.split('<br>'.encode('utf-8'))

        for line in lines:
            text = line.strip()
            value = line.split(b':')[1].strip()
            if text.startswith(b'Hostname'):
                self.hostname = value
            elif text.startswith(b'AS Number'):
                self.asnumber = value
            elif text.startswith(b'Country:'):
                self.country = value
            elif text.startswith(b'Country Code'):
                self.country_code = value
            elif text.startswith(b'Region'):
                self.region = value
            elif text.startswith(b'City'):
                self.city = value
            elif text.startswith(b'Postal Code'):
                self.postal_code = value
            elif text.startswith(b'ISP'):
                self.isp = value
            elif text.startswith(b'Organization'):
                self.organization = value
            elif text.startswith(b'Timezone'):
                self.timezone = value
            elif text.startswith(b'Maps'):
                self.maps = value


        return self.__dict__()

@hug.post('/')
def query_ip_geo_api(ip):
    geo = GeoIP(ip)

    return geo.get_info()


if __name__ == '__main__':
    geo = GeoIP('173.194.115.73')
    print(geo.get_info())
        

