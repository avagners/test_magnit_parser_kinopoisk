import requests
from bs4 import BeautifulSoup


headers = {
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "cookie": "yandexuid=7116207491614400248; yuidss=7116207491614400248; ymex=1929760248.yrts.1614400248#1929760248.yrtsi.1614400248; is_gdpr=0; amcuid=5342791391614432833; gdpr=0; _ym_uid=16144476991018915112; is_gdpr_b=CKLcLBDuICgC; my=YwA=; yabs-dsp=adspend.OWlocXNmcVpKd25CU1JQcWNQdzV1UQ==:getintent.TTUycmRxaGg5MG4uQWlrQUJsRjM0Y19ZMGc=:targetix.ZDQ3MjJmMTQxNTNjZjc3NjU5NGE=:tinkoff.NU5sc1RCZkFSd214Y0R1N0ZOOXVvQQ==:mts_banner.VmR0aXhIY19Ta1NrUWlqZW9rVmQwQQ==:vinia.M1JEa3FqMzdkUVl4SmtpNUlNN2tsdQ==:rutarget.dDJwWFI0cUJ6cUww:target_rtb.TEt1SHBCRmtUbS1JWkpjS0xKTmpLaA==; _ym_d=1626884603; yabs-frequency=/5/10000FgNwM000000/XGySS980003iGI5sV45jXW000En19noWFss60000x44XWc51ROO0003iGIFhLR1mbG000En1855mi72L0000x45W-n8SS980002BGVp____kTx1mbG000Er1G07xLB1mbG000En188WF772I0000xq7y____/; _ym_isad=2; yabs-vdrf=R0KTX90AgacS104TXl0pJfem1o3nXkm296e41o3nXkm3p_eO1CJbXHm1c7TO0H35XmmVems01OHrX9m1w6LK0IlXWPm1hXOS11FHWj013J8a1o-XWDm1Q58q1DDTWqG3QJre07CLWF0U7ddK1a8rWWm1rCcu04r5WSG1MVN81355WbG3uRMO1I4PWAm08jd01TZnWF01nA0000; Session_id=3:1633066009.5.1.1614524306678:Jh8laA:cc.1|1130000039850202.18541703.2.2:18541703|1164633043.128.2.2:128|3:241483.33008.R4nFBWjHFMj5kdxzrYdmQKVZByc; sessionid2=3:1633066009.5.1.1614524306678:Jh8laA:cc.1|1130000039850202.18541703.2.2:18541703|1164633043.128.2.2:128|3:241483.33008.R4nFBWjHFMj5kdxzrYdmQKVZByc; yandex_login=vagner.aa@logistic-yug.ru; i=s9WabWjgeNzsOtTSQb9lo+M+V+rL67WHR9I9GOKti0ohD0DrcMRT0RvhWwaQiAzqnhI4w49XvUzjmlRJBilioTShVwc=; cycada=9qQ/z5B2VCAw82Hb4SifJrHqufMcm1B9ou+m4vvJOdA=; ys=udn.cDphdjRnbmVycw%3D%3D#c_chck.125224583"
}


url = 'https://www.kinopoisk.ru/lists/series-top250/?page=1&tab=all'
req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, 'lxml')
cards = soup.find_all(class_='selection-film-item-meta__link')

count = 0
for card in cards:
    name_film = card.find(class_='selection-film-item-meta__name').text
    genre_film = card.find_all(class_='selection-film-item-meta__meta-additional-item')
    count += 1
    print(count, name_film, genre_film[1].text.split())



