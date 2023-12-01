#!/usr/bin/python3
""" task 8 """

if __name__ == "__main__":
    from requests import post
    from sys import argv

    query = argv[1] if len(argv) > 1 else ""
    request = post('http://0.0.0.0:5000/search_user', data={'q': query})
    try:
        response = request.json()
        if response == {}:
            print('No result')
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print('Not a valid JSON')
