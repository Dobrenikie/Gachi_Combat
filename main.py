import pygame

# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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

# Класс для меню
class Menu:
    def __init__(self, items):
        self.items = []
        for index, item in enumerate(items):
            button = Button(item, 300, 200 + 70 * index, 200, 50)
            self.items.append(button)

    def draw(self, surface):
        for button in self.items:
            button.draw(surface)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.items:
                if button.is_clicked(mouse_pos):
                    print("Вы нажали на кнопку:", button.text)
                    if button.text == "Играть":
                        # Запуск игры
                        pass
                    elif button.text == "Выход":
                        pygame.quit()
                        break

# Создание меню
menu_items = ["Играть", "Выход"]
menu = Menu(menu_items)

# Шрифт
font = pygame.font.Font(None, 36)

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

# Завершение игры
pygame.quit()