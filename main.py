import requests
from bs4 import BeautifulSoup
from functools import reduce

# Sistema de Web Scrapper e uso de programação funcional
# Estamos usando a biblioteca requests para fazer requisições get e BeautifulSoup para trazer informações da requisição para nosso código
# Site que estamos fazendo requisição para trazer o valores da cotação de moeda

# exemplo de moedas para cotação KRW, INR, JPY, CAD, EUR, GBP, CNY, MXN, USD, BRL ...
coin = {"krw", "inr", "jpy", "cad", "eur", "gbp", "cny", "mxn", "usd", "brl"}

# validando informações recebidas
# Valida se foi preenchido corretamente todos os campos, valida se o tipos estão de acordos se o moeda de origem e de destino estão de acordo com o conjunto e verifica se as moedas são divergente para poder fazer o calculo de conversão

def validation(currency_quote, exchange, price):
    if not currency_quote or not exchange or not price:
        print("Preencher todos os campos")
        return client()
    if not type(currency_quote) == str or not type(exchange) == str or not type(price) == float:
        print("campos inválidos preencha corretamente")
        return client()
    if currency_quote not in coin:
        print(f"Moeda de origem digitada inválida, {', '.join(coin)}")
        return client()
    if exchange not in coin:
        print(f"Moeda de destino digitada inválida, {''.join(coin)}")
        return client()
    if exchange == currency_quote:
        print(f"Moeda de destino e origem não pode ser iguais")
        return client()
    print("deu bom")
    return currency_quote, exchange, price

def client():
    currency_quote = input("Qual moeda para cotação?").lower()
    exchange = input("Qual a moeda de conversão?").lower()
    price = float(input("Qual valor para conversão?"))
    validation(currency_quote, exchange, price)
    

client()

# requisição get para site de cotação ainda em desenvolvimento
def currency_converter(origin_currency, destination_currency):
    def get_value(price):
        link = f"https://wise.com/br/currency-converter/{currency_quote}-to-{exchange}-rate?amount={price}"
        return link
    return get_value

#configurar o headers para 
headers ={"user-agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36"}

requisicao = requests.get(link, headers=headers)

site = BeautifulSoup(requisicao.text, "html.parser")
print(site.prettify())

value = site.find('input', id="target-input")
print(value.get('value'))

