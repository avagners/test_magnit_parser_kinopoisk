import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

headers = {
    "accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"
}

# ------------- 1. СОХРАНЕНИЕ НУЖНЫХ СТРАНИЦ (РАССКОМЕНТИРОВАТЬ КОД НИЖЕ ДЛЯ ОБНОВЛЕНИЯ ДАННЫХ) ---------------- #


def get_pages():
    for i in range(1, 6):
        url = f'https://www.kinopoisk.ru/lists/series-top250/?page={i}&tab=all'
        req = requests.get(url, headers=headers)
        src = req.text

        with open(f'page_{i}.html', 'w', encoding="utf-8") as file:
            file.write(src)

# ----------------------------------------- 2. СБОР НЕОБХОДИМЫХ ДАННЫХ ------------------------------------------ #


list_of_genre = []
res_list_of_genre = []


def get_data():

    count = 0
    for i in range(1, 6):
        with open(f'page_{i}.html', encoding="utf-8") as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')
        cards = soup.find_all(class_='selection-film-item-meta__link')

        for card in cards:
            # name_film = card.find(class_='selection-film-item-meta__name').text
            genre_film = card.find_all(class_='selection-film-item-meta__meta-additional-item')[1].text.split(', ')
            count += 1
            list_of_genre.append(genre_film)

        print(f"Получены данные со страницы {i}")
    print(f"Итого получены данные из {len(list_of_genre)} фильмов.")
    # -------------------------------- 3. ПРЕОБРАЗОВАНИЕ ДАННЫХ О ЖАНРАХ В ОДИН СПИСОК ----------------------------- #

    for i in list_of_genre:
        for j in i:
            res_list_of_genre.append(j)

# -------------------------------- 4. ПОДСЧЕТ ПОВТОРЕНИЙ ЖАНРОВ - СОЗДАНИЕ СЛОВАРЯ ----------------------------- #


def transform_list_to_dict():
    dict_count_genre = {i: res_list_of_genre.count(i) for i in res_list_of_genre}
    return dict_count_genre
# --------------------------------------- 5. СОЗДАНИЕ СТОЛБЧАТОЙ ДИАГРАММЫ  ---------------------------------------- #


def create_diagram(dict_data):
    plt.title('Статистика жанров')
    plt.xlabel("Название жанра")
    plt.ylabel("Кол-во повторений")
    plt.subplots_adjust(bottom=0.3)

    lists = dict_data.items()
    x, y = zip(*lists)

    plt.bar(x, y)

    for i, val in enumerate(y):
        plt.text(i, val, int(val), horizontalalignment='center', verticalalignment='bottom', fontdict={'fontweight': 500, 'size': 8})
    plt.gca().set_xticklabels(x, rotation=60, horizontalalignment='right')
    plt.show()

# --------------------------------------- 6. Вызов функций  ---------------------------------------- #


get_pages()
get_data()
create_diagram(transform_list_to_dict())
