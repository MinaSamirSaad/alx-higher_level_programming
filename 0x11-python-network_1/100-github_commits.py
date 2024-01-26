#!/usr/bin/python3
'''
script that takes 2 arguments in order to solve this challenge.
The first argument will be the repository name
The second argument will be the owner name
'''
if __name__ == '__main__':
    import requests
    from sys import argv
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    res = requests.get(url, timeout=5)
    commits = res.json()
    for commit in commits[:10]:
        print("{}: {}".format(commit.get('sha'),
                              commit.get('commit').get('author').get('name')))
