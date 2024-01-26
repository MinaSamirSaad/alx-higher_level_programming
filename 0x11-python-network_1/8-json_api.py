#!/usr/bin/python3
'''
Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty
display the id and name like this: [<id>] <name>
'''
if __name__ == '__main__':
    import requests
    from sys import argv
    res = requests.post("http://0.0.0.0:5000/search_user", data={'q': (
        argv[1] if len(argv) > 1 else "")}, timeout=5)
    try:
        res = res.json()
        if res:
            print("[{}] {}".format(res['id'], res['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
