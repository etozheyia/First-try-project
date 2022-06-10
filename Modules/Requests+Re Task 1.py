# Напишите скрипт для парсинга номеров телефонов с данного урла:
# https://www.summet.com/dmsi/html/codesamples/addresses.html

import requests
import re

response = requests.get('https://www.summet.com/dmsi/html/codesamples/addresses.html')
text = response.text
result = re.findall(r'\(\d{3}\)\s\d{3}-\d{4}', text)
print(result)
