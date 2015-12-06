# rtfmapi
RTFM general use API

## Description

This API is used by the [RTFM / Red Team Freakin' Maniacs](http://www.rtfm-ctf.org) CTF team for various purposes

## Dependencies

To install dependencies, run:

```
pip install -r requirements.txt
```

You are better doing this inside a virtualenv (check out [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) for state-of-art Python versioning and virtualenv management)

## Setup
Copy config_example.conf to ~/.rtfmapi/rtfmapi.conf and edit accordingly

## Usage
To start the REST interface, run:
```
hug -f main.py
```

Additionally, most modules can be run standalone. Try and see.

## Endpoints
For a complete list of endpoints, check the code!

Endpoints arguments must be JSON-encoded inside a POST body, unless said otherwise.

### /query/cpf

Queries a CPF at Receita Federal

Expected Parameters:

* cpf: CPF number, in format NNNNNNNNNNN or NNN.NNN.NNN-NN
* birth: birth date, in any format recognizable by Python's [dateutil](https://labix.org/python-dateutil)


Example output:

```json
{
  "death_year": "0000",
  "cpf": "133.267.246-91",
  "verification_digit": "00",
  "name": "DILMA VANA ROUSSEFF",
  "situation": "REGULAR",
  "birth": "1947/12/14",
  "return_message": "OK",
  "control_code": "D060.ACA9.A3AA.1222",
  "subscription_date": "1990/10/11",
  "death_message": null
}
```


### /query/ip/geo

Queries an IP geo information

Expected parameters:

* ip: The IP to get GEO information for

Example output:
```json
{
  "country": "United States",
  "ip": "173.194.115.73",
  "organization": "Google",
  "postal_code": "94043",
  "city": "Mountain View",
  "hostname": "dfw06s41-in-f9.1e100.net",
  "country_code": "US",
  "timezone": "America/Los_Angeles",
  "asnumber": "AS15169 Google Inc.",
  "isp": "Google",
  "maps": "https",
  "region": "California / CA"
}
```

### /query/shellshock/possible

Returns a list of possibly ShellShock vulnerable hosts

Example output:
```json
[
  "http://XXX.XXX.19.27/cgi-bin/test.cgi",
  "http://XXX.XXX.23.242/cgi-bin/test.cgi",
  "http://XXX.XXX.68.82/cgi-bin/test.cgi",
  "http://XXX.XXX.168.126/cgi-bin/test.cgi",
  "http://XXX.XXX.8.11/cgi-bin/test.cgi",
  "http://XXX.XXX.246.67/cgi-bin/test.cgi",
  "http://XXX.XXX.68.66/cgi-bin/test.cgi",
  "http://XXX.XXX.3.170/cgi-bin/test.cgi",
  "http://XXX.XXX.73.229/cgi-bin/test.cgi",
  ...
  ]
```

## Credits
- [Kamus Hadenes](https://github.com/kamushadenes) (Author)
- [RTFM](http://www.rtfm-ctf.org/)
- [Gambler](https://github.com/mthbernardes)
