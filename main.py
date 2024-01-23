import urllib.request

import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text
response_parse = response_text.split("<span>")
for parse_elem in response_parse:
    if parse_elem.startswith("Офіційний курс"):
        for parse_elem_2 in parse_elem.split("</span>"):
            if parse_elem_2.startswith("Офіційний курс"):
                print(parse_elem_2)

#print(response_parse)