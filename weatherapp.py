import requests


def main():
    url_template = 'http://wttr.in/{}'
    places = ['london', 'sheremetyevo', 'cherepovets']
    payload = {'nTqm': '', 'lang': 'ru'}

    for place in places:
        url = url_template.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
