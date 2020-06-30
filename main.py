import requests

URL = 'https://es.wikipedia.org/wiki/Anexo:Estrellas_m%C3%A1s_cercanas'
page = requests.get(URL)
print(page)