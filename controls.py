import pygame
import random
import time
# Инициализация Pygame
pygame.init()

# Создание окна игры
screen = pygame.display.set_mode((1200, 800))


pygame.mixer.music.load("MP3/backmusic.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.04)

pygame.display.set_caption("Моя игра")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Шрифт
font = pygame.font.Font(None, 36)

class Button:
    def __init__(self, text, pos_x, pos_y, width, height):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = max(width, len(self.text) * 15)  # Измените эту строку
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


# Класс для игры
class Game:
    def __init__(self):
        self.player_choice = None
        self.computer_choice = None
        self.player_health = 25
        self.computer_health = 25
        self.game_over = False
        self.winner = None
        self.button_1 = Button("1-в голову", 290, 750, 200, 50)
        self.button_2 = Button("2-в тело", 500, 750, 200, 50)
        self.button_3 = Button("3-в ноги", 710, 750, 200, 50)
        self.computer_original = pygame.image.load("images/computer/computer_body_idle.png")
        self.player_original = pygame.image.load("images/player/player_body_idle.png")



    
    

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and not self.game_over:
            if event.key == pygame.K_1:
                self.player_choice = 1
            elif event.key == pygame.K_2:
                self.player_choice = 2
            elif event.key == pygame.K_3:
                self.player_choice = 3
        # В вашем методе обработки событий (например, методе handle_events) добавьте следующую логику:
    
    def update(self):
        
        
        
        if not self.game_over and self.player_choice is not None:
            self.computer_choice = random.randint(1, 3)
            
            #если выбор игрока цифра 3
            if self.computer_choice == 1 and self.player_choice ==3:
                
                self.computer_original =  pygame.image.load("images/computer/computer_body_strike.png")
                self.player_original =  pygame.image.load("images/player/player_legs_strike.png")
                
                self.computer_health -= 1
                print("Компьютер получает 1 урона")
                self.player_health -= 5
                print("Игрок получает 5 урона")
                
            elif self.computer_choice == 2 and self.player_choice == 3:
                
                self.computer_original =  pygame.image.load("images/computer/computer_head_strike.png")
                self.player_original =  pygame.image.load("images/player/player_legs_strike.png")
                
                self.computer_health -= 1
                print("Компьютер получает 1 урона")
                self.player_health -= 3
                print("Игрок получает 3 урона")
            elif self.computer_choice == 3 and self.player_choice == 3:
                self.computer_original =  pygame.image.load("images/computer/computer_legs_strike.png")
                self.player_original =  pygame.image.load("images/player/player_legs_strike.png")
                print("Ничья")
            
            #если выбор игрока цифра 2
            elif self.computer_choice == 1 and self.player_choice == 2:
                
                self.computer_original =  pygame.image.load("images/computer/computer_body_strike.png")
                self.player_original =  pygame.image.load("images/player/player_head_strike.png")
                
                self.computer_health -= 3
                print("Компьютер получает 3 урона")
                self.player_health -= 5
                print("Игрок получает 5 урона")
                
            elif self.computer_choice == 1 and self.player_choice == 2:
                
                self.computer_original =  pygame.image.load("images/computer/computer_head_strike.png")
                self.player_original =  pygame.image.load("images/player/player_head_strike.png")
                print("Ничья")
                
            elif self.computer_choice == 3 and self.player_choice == 2:
                
                self.computer_original =  pygame.image.load("images/computer/computer_legs_strike.png")
                self.player_original =  pygame.image.load("images/player/player_head_strike.png")
                
                self.computer_health -= 3
                print("Компьютер получает 3 урона")
                self.player_health -= 1
                print("Игрок получает 1 урона")
            
            #если выбор игрока цифра 1
            elif self.computer_choice == 1 and self.player_choice == 1:
                
                self.computer_original =  pygame.image.load("images/computer/computer_body_strike.png")
                self.player_original =  pygame.image.load("images/player/player_body_strike.png")
                
            
            elif self.computer_choice == 2 and self.player_choice == 1:
                
                self.computer_original =  pygame.image.load("images/computer/computer_head_strike.png")
                self.player_original =  pygame.image.load("images/player/player_body_strike.png")
                
                
                self.computer_health -= 5
                print("Компьютер получает 5 урона")
                self.player_health -= 3
                print("Игрок получает 3 урона")
                
            
            elif self.computer_choice == 3 and self.player_choice == 1:
                
                self.computer_original =  pygame.image.load("images/computer/computer_legs_strike.png")
                self.player_original =  pygame.image.load("images/player/player_body_strike.png")
                
                self.computer_health -= 5
                print("Компьютер получает 5 урона")
                self.player_health -= 1
                print("Игрок получает 1 урона")
            
            
                        
            if self.player_health <= 0 or self.computer_health <= 0:
                self.game_over = True
                if self.player_health <= 0:
                    self.winner = "Компьютер"
                else:
                    self.winner = "Игрок"

            self.player_choice = None
    
    def draw(self, surface):
        background_image = pygame.image.load("images/background.jpg")
        background_image = pygame.transform.scale(background_image, (1200, 800))
        surface.blit(background_image, (0, 0))
        
        if not self.game_over:
            # Отображение здоровья игрока
            player_health_label = font.render(f"Здоровье игрока: {self.player_health}", True, WHITE)
            surface.blit(player_health_label, (20, 20))
            
            # Отображение здоровья компьютера
            computer_health_label = font.render(f"Здоровье компьютера: {self.computer_health}", True, WHITE)
            surface.blit(computer_health_label, (20, 50))
            
             # Отображение кнопок
            
            computer_pos_x = surface.get_width() // 2 - 90
            player_pos_x = surface.get_width() // 2 - 250 + 90
            image_pos_y = surface.get_height() // 2 - 450 // 5

            self.computer = pygame.transform.scale(self.computer_original, (250, 450))
            self.player = pygame.transform.scale(self.player_original, (250, 450))
        
            # Устанавливаем позиции для изображений
            self.computer_rect = self.computer.get_rect(topleft=(computer_pos_x, image_pos_y))
            self.player_rect = self.player.get_rect(topleft=(player_pos_x, image_pos_y))
            
            surface.blit(self.player, self.player_rect)
            surface.blit(self.computer, self.computer_rect)
            
            self.button_1.draw(surface)
            self.button_2.draw(surface)
            self.button_3.draw(surface)
            
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
pygame.mixer.music.stop()
pygame.quit()