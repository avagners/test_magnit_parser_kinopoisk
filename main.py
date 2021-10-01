import requests
from bs4 import BeautifulSoup

headers = {
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}


# ------------- 1. СОХРАНЕНИЕ НУЖНЫХ СТРАНИЦ (РАССКОМЕНТИРОВАТЬ КОД НИЖЕ ДЛЯ ОБНОВЛЕНИЯ ДАННЫХ) ---------------- #

# for i in range(1, 6):
#     url = f'https://www.kinopoisk.ru/lists/series-top250/?page={i}&tab=all'
#     req = requests.get(url, headers=headers)
#     src = req.text
#
#     with open(f'page_{i}.html', 'w', encoding="utf-8") as file:
#         file.write(src)

# -------------- 2. СБОР НЕОБХОДИМЫХ ДАННЫХ ----------------- #

list_of_genre = []
count = 0
for i in range(1, 6):
    with open(f'page_{i}.html', encoding= "utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all(class_='selection-film-item-meta__link')

    for card in cards:
        name_film = card.find(class_='selection-film-item-meta__name').text
        genre_film = card.find_all(class_='selection-film-item-meta__meta-additional-item')[1].text.split()
        count += 1
        list_of_genre.append(genre_film)
        print(count, name_film, genre_film)
    print(f"Получены данные со старницы {i}")
print(len(list_of_genre))



