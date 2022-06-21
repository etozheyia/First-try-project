# На главной странице сайта proglib.io у всех картинок формата png и jpg нужно узнать урлы
# и сохранить в любую структуру данных.

import requests
import re

url = 'https://proglib.io/'
response = requests.get(url, timeout=5)
content = response.text
regex_without_format = r'http[:\w./_-]*\.'
result = re.findall(rf'{regex_without_format}png|{regex_without_format}jpg', content)
print(set(result))
