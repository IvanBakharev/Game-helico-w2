from random import randint, choice


class Clouds:
    """Класс для моделирования облаков на игровом поле."""

    def __init__(self, width, height):
        # Инициализируем тип для облаков
        self.type = type

        """Создание поля и инициализация пустыми ячейками."""
        # Инициализируем ширину и высоту поля
        self.width = width
        self.height = height

        # Создание двумерного массива для хранения состояния каждой ячейки.
        # В начале, все ячейки инициализируются значением 0, что обозначает "пусто".
        self.cells = [[0 for x in range(width)] for y in range(height)]

    def spawn_cloud(self, size=2, type='normal'):
        """Генерация нового облака в случайном месте."""
        # Выбираем случайную X координату
        # для левого верхнего угла облака:
        # randint(a, b) генерирует число от a до b включительно
        # Вычитаем размер облака, чтобы оно полностью влезло в поле
        start_x = randint(0, self.width - size)

        # Выбираем случайную Y координату
        # для левого верхнего угла облака:
        start_y = randint(0, self.height - size)

        # Разные типы облаков
        type = choice(['normal', 'storm'])
        if type == 'normal':
            value = 1 # обычное облако
        elif type == 'storm':
            value = 2 # грозовое облако

        # Два вложенных цикла для заполнения облака:

        # Внешний цикл по вертикали
        for i in range(size):

            # Внутренний цикл по горизонтали
            for j in range(size):
                # Заполняем ячейку по координатам и с разным типом облаков:
                # start_x + смещение по X
                # start_y + смещение по Y
                self.cells[start_y + i][start_x + j] = value

    def fade_clouds(self):
        """Исчезновение облаков."""
        # Инициализируем переменную для шага исчезновения
        fade_step = 0

        # Проходимся по всем строкам (высоте) изображения
        for y in range(self.height):
            # Проходимся по всем столбцам (ширине) изображения
            for x in range(self.width):

                # Если текущая ячейка содержит облако (значение 1)
                if self.cells[y][x] == 1:
                    # С вероятностью 1 к 10 (10%) облако исчезает
                    if randint(1, 10) == 1:
                        self.cells[y][x] = 0  # Устанавливаем значение ячейки как "исчезнувшее"

                # Если текущая ячейка содержит исчезающее облако (значение 2)
                elif self.cells[y][x] == 2:

                    # Если шаг исчезновения равен 0, начинаем процесс исчезновения
                    if fade_step == 0:
                        fade_step = 1

                    # Если шаг исчезновения равен 1, то облако полностью исчезло, превращаясь в облако (значение 1) снова
                    elif fade_step == 1:
                        self.cells[y][x] = 1  # Устанавливаем значение ячейки как "облако"
                        fade_step = 0  # Сбрасываем шаг исчезновения

    def update(self):
        """Обновление состояния на каждом шаге."""
        # Спавн случайного облака
        if randint(1, 10) == 1:
            # Генерируем случайное число от 1 до 10
            # Если оно равно 1, то спавним облако
            # Вызываем метод spawn_cloud() для создания облаков
            type = choice(['normal', 'storm'])
            self.spawn_cloud(type=type)

        # Случайное удаление облака
        if randint(1, 10) == 1:
            self.fade_clouds()
            # Генерируем случайное число от 1 до 10
            # Если оно равно 1, удаляем случайное облако

            # Выбираем случайные координаты
            # x - от 0 до ширины поля - 1
            x = randint(0, self.width - 1)

            # y - от 0 до высоты поля - 1
            y = randint(0, self.height - 1)

            # Устанавливаем значение ячейки в 0, чтобы удалить облако
            self.cells[y][x] = 0

    def export_data(self):
        return{"cells": self.cells}  

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for x in range(self.width)] for y in range(self.height)]

