import requests
from datetime import datetime, timedelta


def get_questions_python(fromdate, todate, tag="python"):
    '''Функция выводит все вопросы за последние два дня и содержит тэг "Python" на сайте stackoverflow.com'''
    # print(type(fromdate))
    # print(type(todate))
    pages = 1
    check = True
    all_pages = 0
    while check:
        url = f'https://api.stackexchange.com/2.3/questions?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&tagged={tag}&site=stackoverflow&pagesize=100&page={pages}'
        response = requests.get(url)
        all_pages += len(response.json()["items"])
        check = response.json()["has_more"]
        pages += 1
    print(all_pages)
    return all_pages


if __name__ == '__main__':
    date_from = str(datetime.now() - timedelta(days=1)).split(" ")[0]
    today = str(datetime.now()).split(" ")[0]
    get_questions_python(date_from, today)
