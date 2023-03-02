from pygame import *

WIDTH, HEIGHT = 900, 600 #розміри вікна
FPS = 60 #кількість кадрів в секунду

#музика
mixer.init() #підключаємо модуль mixer для роботи з музикою
mixer.music.load('space.ogg')  #завантажуємо музику
mixer.music.set_volume(0.3) #гучність музики
mixer.music.play() #запускаємо фонову музику
# mixer.music.stop() #зупинити фонову музику

window = display.set_mode((WIDTH, HEIGHT)) #створюємо вікно
display.set_caption("Космічний шутер") #назва вікна

class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, x, y, width, height):
        super().__init__()  #створюємо порожній спрайтІ
        #завантажуємо картинку і змінюємо її розмір на width х height
        self.image = transform.scale(image.load(sprite_image), (width, height))
        self.rect = self.image.get_rect()  #отримуємо прямокутну область розміру картинки
        self.rect.x = x  #задаємо початкові координати спрайту
        self.rect.y = y

    def draw(self):
        #відрисовуємо у вікні картинку self.image в координатах self.rect
        window.blit(self.image, self.rect) 

class Player(GameSprite): #гравець
    def update(self):
        #рух гравця з клавіатури
        pressed = key.get_pressed() #список натиснутих кнопок
        if pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= 3
        if pressed[K_RIGHT] and self.rect.x < WIDTH - 70:
            self.rect.x += 3

player = Player("rocket.png", x=WIDTH/2-50, y=HEIGHT-200, width=100, height = 100)
bg = transform.scale(image.load("galaxy.jpg"), (WIDTH, HEIGHT))

run = True
clock = time.Clock() #cтворили таймер

while run: #поки гра запущена
    
    for e in event.get(): #перевіряємо всі події
        if e.type == QUIT: #якщо натиснуто закрити вікно
            run = False # зупиняємо гру
    window.blit(bg, (0,0))
    player.draw()
    player.update()
    
    display.update() #оновлюємо екран 
    clock.tick(FPS) #задаємо FPS