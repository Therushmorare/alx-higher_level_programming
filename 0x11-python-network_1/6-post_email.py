#!/usr/bin/python3
""" task 6 """

if __name__ == "__main__":
    from requests import post
    from sys import argv

    html = post(argv[1], data={'email': argv[2]})
    print(html.text)
