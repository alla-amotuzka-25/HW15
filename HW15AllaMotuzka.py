# 1. Подключитесь к API НБУ ( документация тут https://bank.gov.ua/ua/open-data/api-dev ),
# получите текущий курс валют и запишите его в TXT-файл в таком формате:
#"[дата создания запроса]"
# 1. [название ввалюты 1] to UAH: [значение курса к валюте 1]
# 2. [название ввалюты 2] to UAH: [значение курса к валюте 2]
# 3. [название ввалюты 3] to UAH: [значение курса к валюте 3]
# ...
# n. [название ввалюты n] to UAH: [значение курса к валюте n]


import requests

try:
    nbu = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date=20211013&json')
except:
    pass

nbu_lst = nbu.json()
list_nbu = nbu_lst


def utr():
    for dct in list_nbu:
        name = dct['txt']
        rate = dct['rate']
        data = dct['exchangedate']
        print(data)
        for i, val in enumerate(list_nbu):
            num = i+1
            res = f'{num} {name} to UAH: {rate}'
            print(res)


utr()


# 2. В вашем репозитории создайте отдельную ветку HW15 от ветки master, реализуйте дз в ней и выполните мердж ветки
# HW15 в ветку master.
