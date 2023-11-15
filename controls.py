import pygame
import random

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Класс для меню
class Menu:
    def __init__(self):
        self.player_choice = None

    def draw(self, surface):
        font = pygame.font.Font(None, 36)
        label = font.render("Выберите удар: 1 - Верхний удар, 2 - Средний удар, 3 - Нижний удар", True, WHITE)
        surface.blit(label, (100, 200))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.player_choice = 1
            elif event.key == pygame.K_2:
                self.player_choice = 2
            elif event.key == pygame.K_3:
                self.player_choice = 3

# Создание меню
menu = Menu()

# Основной цикл игры
running = True
while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        menu.handle_event(event)

    # Отрисовка
    screen.fill(BLACK)
    menu.draw(screen)
    pygame.display.flip()

    # Если игрок сделал выбор
    if menu.player_choice is not None:
        # Генерация выбора компьютера
        computer_choice = random.randint(1, 3)

        # Определение результата удара
        if menu.player_choice == computer_choice:
            print("Ничья, никто не получает урон")
        elif (menu.player_choice == 1 and computer_choice == 3) or \
                (menu.player_choice == 2 and computer_choice == 1) or \
                (menu.player_choice == 3 and computer_choice == 2):
            print("Получает урон компьютер")
        else:
            print("Получает урон игрок")

        # Сброс выбора игрока
        menu.player_choice = None

# Завершение игры
pygame.quit()