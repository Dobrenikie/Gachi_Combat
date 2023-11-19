import pygame
import random

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

# Класс для игры
class Game:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.player_health = 25
        self.computer_health = 25
        self.game_over = False
        self.winner = None

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and not self.game_over:
            if event.key == pygame.K_1:
                self.player_choice = 1
            elif event.key == pygame.K_2:
                self.player_choice = 2
            elif event.key == pygame.K_3:
                self.player_choice = 3

    def update(self):
        if not self.game_over and self.player_choice is not None:
            self.computer_choice = random.randint(1, 3)

            if self.player_choice == self.computer_choice:
                print("Ничья, никто не получает урон")
            elif (self.player_choice == 1 and self.computer_choice == 3) or \
                    (self.player_choice == 1 and self.computer_choice == 2) or \
                    (self.player_choice == 2 and self.computer_choice == 3):
                print("Получает урон компьютер")
                self.computer_health -= 5
            else:
                print("Получает урон игрок")
                self.player_health -= 5

            if self.player_health <= 0 or self.computer_health <= 0:
                self.game_over = True
                if self.player_health <= 0:
                    self.winner = "Компьютер"
                else:
                    self.winner = "Игрок"

            self.player_choice = None

    def draw(self, surface):
        surface.fill(BLACK)
        
        if not self.game_over:
            # Отображение здоровья игрока
            player_health_label = font.render(f"Здоровье игрока: {self.player_health}", True, WHITE)
            surface.blit(player_health_label, (20, 20))
            
            # Отображение здоровья компьютера
            computer_health_label = font.render(f"Здоровье компьютера: {self.computer_health}", True, WHITE)
            surface.blit(computer_health_label, (20, 50))
            
            label = font.render("Выберите удар: 1 - Верхний удар, 2 - Средний удар, 3 - Нижний удар", True, WHITE)
            surface.blit(label, (200, 700))
        else:
            # Вывод сообщения о победителе
            winner_label = font.render(f"{self.winner} победил!", True, WHITE)
            surface.blit(winner_label, (500, 400))

        pygame.display.flip()


# Создание объекта игры
game = Game()

# controls.py
def play():
    # Ваша логика игры controls.py
    print("Игра controls.py запущена")

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game.handle_event(event)

    game.update()
    game.draw(screen)

pygame.quit()