#!/usr/bin/python3
'''
Python script that fetches https://alx-intranet.hbtn.io/status
You must use the package requests
'''
if __name__ == '__main__':
    import requests
    r = requests.get('https://alx-intranet.hbtn.io/status', timeout=5)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
