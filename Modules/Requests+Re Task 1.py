# Напишите скрипт для парсинга номеров телефонов с данного урла:
# https://www.summet.com/dmsi/html/codesamples/addresses.html

import requests
import re

url = 'https://www.summet.com/dmsi/html/codesamples/addresses.html'
response = requests.get(url, timeout=5)
text = response.text
result = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}', text)
print(result)
