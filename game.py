from utils import randcell2
# Импорт функции randcell2 из модуля utils

from utils import randcell
# Импорт функции randcell из модуля utils

from utils import randbool
# Импорт функции randbool из модуля utils

# 🌳 🚁 🌊 🔥 🏥 ❤️ ⚡ 🏆 ☁️ 🧺 🏬 🔵 🟡

from map import Map
# Импорт класса Map из модуля map

from clouds import Clouds

# Импорт класса Clouds из модуля clouds

from pynput import keyboard
# Импорт модуля keyboard для обнаружения ввода с клавиатуры

import time
# Импорт модуля time для функций задержки

import os
# Импорт модуля os для очистки консоли

import json

from helicopter import Helicopter as Helico
# Импорт класса Helicopter из модуля helicopter


TICK_SLEEP = 0.3
# Время задержки между каждым тактом

TREE_UPDATE = 40
# Частота генерации новых деревьев

CLOUDS_UPDATE = 8
# Частота обновления позиций облаков

FIRE_UPDATE = 20
# Частота распространения огня

MAP_W, MAP_H = 20, 10
# Ширина и высота карты

field = Map(MAP_W, MAP_H)
# Создание объекта Map

clouds = Clouds(MAP_W, MAP_H)
# Создание объекта Clouds

helico = Helico(MAP_W, MAP_H)
# Создание объекта Helicopter

# Начало прослушивания ввода с клавиатуры

tick = 1

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}


# Словарь, сопоставляющий клавиши WASD кортежам dx, dy

def process_key(key):
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    if c == 'f':
        data = {"helicopter": helico.export_data(), "clouds": clouds.export_data(), "field": field.export_data()}
        with open("level.json", "w") as lvl:
             json.dump(data, lvl)    


# Функция для обработки ввода с клавиатуры и перемещения вертолета

# Создание слушателя
listener = keyboard.Listener(
    on_press=None,
    on_release=process_key, )
listener.start()


# Очистка консоли один раз в начале с проверкой операционной системы, если windows то используется cls, если linux то clear
os.system("cls" if os.name == "nt" else "clear")

while True:
    # Очистка консоли в начале каждого такта с проверкой операционной системы, если windows то используется cls, если linux то clear
    os.system("cls" if os.name == "nt" else "clear")

    print("TICK", tick)
    field.process_helicopter(helico, clouds)
    helico.print_stats()
    field.print_map(helico, clouds)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TREE_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fire()
    if (tick % CLOUDS_UPDATE == 0):
        clouds.update()


# Основной игровой цикл:
# - Очистка консоли
# - Вывод текущего такта
# - Обновление вертолета на поле
# - Вывод статистики вертолета
# - Вывод карты
# - Увеличение такта
# - Небольшая задержка
# - По желанию: генерация деревьев, распространение огня, обновление облаков
