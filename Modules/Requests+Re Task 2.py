# На главной странице сайта proglib.io у всех картинок формата png и jpg нужно узнать урлы
# и сохранить в любую структуру данных.

import requests
import re

response = requests.get('https://proglib.io/')
content = response.text
result_png = re.findall(r'http[:\w./_-]*\.png', content)
result_jpg = re.findall(r'http[:\w./_-]*\.jpg', content)
print(result_png, result_jpg)
