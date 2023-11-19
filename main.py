import pygame
import sys

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

# Класс для кнопок
class Button:
    def __init__(self, text, pos_x, pos_y, width, height):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, (self.pos_x, self.pos_y, self.width, self.height))
        label = font.render(self.text, True, BLACK)
        label_width = label.get_width()
        label_height = label.get_height()
        label_pos_x = self.pos_x + (self.width - label_width) // 2
        label_pos_y = self.pos_y + (self.height - label_height) // 2
        surface.blit(label, (label_pos_x, label_pos_y))
        
    def is_clicked(self, mouse_pos):
        if self.pos_x <= mouse_pos[0] <= self.pos_x + self.width and \
           self.pos_y <= mouse_pos[1] <= self.pos_y + self.height:
            return True
        return False

# Создание кнопки "Играть"
play_button = Button("Играть", 500, 300, 200, 50)

# Создание кнопки "Выход"
exit_button = Button("Выход", 500, 400, 200, 50)


# Основной цикл игры
running = True
playing_controls = False  # Переменная для отслеживания состояния игры controls.py
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.is_clicked(mouse_pos):
                playing_controls = True  # Устанавливаем состояние игры controls.py
            elif exit_button.is_clicked(mouse_pos):
                pygame.quit()
                sys.exit()

    screen.fill(BLACK)
    play_button.draw(screen)
    exit_button.draw(screen)
    pygame.display.flip()

    if playing_controls:
        import controls  # Импортируем модуль controls.py
        controls.play()  # Запускаем игру controls.py
        playing_controls = False  # Сбрасываем состояние игры controls.py

pygame.quit()