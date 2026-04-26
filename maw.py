
from typing import Any

import requests

from bs4 import BeautifulSoup

import bs4
def get_info_magnit(url):
    headers = {
        'authority': 'magnit.ru',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36 OPR/63.0.3368.107',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'sec-fetch-site': 'none',
        'referer': 'https',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cookie': 'mg_udi=45778daf-50b2-452f-8b0e-613e566ea16a; nmg_dt=; shopCode=992301; x_shop_type=ME; _ym_uid=1776516551887206089; _ym_d=1776516551; _ym_visorc=b; _ym_isad=1'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    text = str(soup.body).split("₽")[0][-50:][::-1]
    #print(text.split(">")[0][-50:][::-1])
    #print(soup.title.text)
    txt = text.split(">")[0][-50:][::-1]
    name = str(soup.title.text).split(" – ")[0]
    ls = dict()
    ls["shop"] = "Магнит"
    ls["product"] = name
    ls["price"] = text.split(">")[0][-50:][::-1].split("\u200a")[0]

    #
    return ls

def get_info_patyorka(url):
    headers = {
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'text/plain;charset=UTF-8',
        'origin': 'https://5ka.ru',
        'priority': 'u=1, i',
        'referer': 'https://5ka.ru/',
        'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    text = str(soup.body)
    a = text.split(">")[0][-50:][::-1]
    #print(soup.title.text)
    #print(soup.title.text)
    txt = text.split(">")[0][-50:][::-1]
    name = str(soup.title.text).split(" – ")[0]
    ls = dict()
    ls["shop"] = "Пятёрочка"
    ls["product"] = name
    ls["price"] = text.split(">")[0][-50:][::-1].split("\u200a")[0]
    return ls

def get_info_lenta(url):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Access-Control-Request-Headers': 'authorization,content-type',
        'Access-Control-Request-Method': 'POST',
        'Connection': 'keep-alive',
        'Origin': 'https://lenta.com',
        'Referer': 'https://lenta.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
    }

    response = requests.get(url,headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')

    text = str(soup.body)
    a = text.split(">")[0][-50:][::-1]
    #print(soup.title.text)
    #print(soup.title.text)
    txt = text.split(">")[0][-50:][::-1]
    name = str(soup.title.text).split(" – ")[0]
    ls = dict()
    ls["shop"] = "Лента"
    ls["product"] = name
    ls["price"] = text.split(">")[0][-50:][::-1].split("\u200a")[0]
    return ls

print(get_info_lenta("https://lenta.com/product/chajj-chernyjj-energy-tea-aromat-kup-rossiya-20pak-696224/"))