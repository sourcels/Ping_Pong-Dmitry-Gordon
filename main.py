from pygame import *
window = display.set_mode((700, 394))
display.set_caption('Dmitry_Gordon.exe')
background = transform.scale(image.load("assets/background.jpg"), (700, 394))
game = True
bool_1 = True
bool_2 = False
bool_3 = False
bool_4 = False
win1 = False
win2 = False
bool_endstream = False
score = 0
clock = time.Clock()
FPS = 60
mixer.init()
mixer.music.load('assets/music.ogg')
mixer.music.play()
font.init()
win2_txt = font.SysFont(
    'Arial', 80).render(
        'Player 2 wins!', True, (0, 255, 0))
win1_txt = font.SysFont(
    'Arial', 80).render(
        'Player 1 wins!', True, (180, 0, 0))
score_txt = font.SysFont('Arial', 40).render(
    'Score:' + str(score), True, (255, 0, 255))


class Gamespr(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y, speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(
            image.load(sprite_image), (size_x, size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player0(Gamespr):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 300:
            self.rect.y += self.speed


class Player1(Gamespr):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 300:
            self.rect.y += self.speed


class Ball(Gamespr):
    def update(self):
        global score
        global score_txt
        score_txt = font.SysFont('Arial', 40).render(
            'Score:' + str(score), True, (255, 0, 255))


gameplayer0 = Player0('assets/plat.jpg', 20, 197, 26, 100, 4)
gameplayer1 = Player1('assets/plat.jpg', 640, 197, 26, 100, 4)
ball = Ball("assets/ball.png", 320, 150, 69, 69, 2)
while game:
    window.blit(background, (0, 0))
    window.blit(score_txt, (0, 0))
    if bool_endstream and win1:
        window.blit(win1_txt, (200, 50))
        bool_endstream = True
    elif bool_endstream and win2:
        window.blit(win2_txt, (200, 50))
        bool_endstream = True
    else:
        if not bool_endstream:
            ball.update()
            ball.reset()
            gameplayer0.update()
            gameplayer0.reset()
            gameplayer1.update()
            gameplayer1.reset()
            if bool_1:
                ball.rect.x += ball.speed
                ball.rect.y += ball.speed
                if ball.rect.colliderect(gameplayer1.rect):
                    score += 1
                    ball.speed += 0.020
                    bool_1 = False
                    bool_4 = True
                elif ball.rect.x >= 631:
                    win1 = True
                    bool_endstream = True
                elif ball.rect.y >= 330:
                    ball.speed += 0.020
                    bool_1 = False
                    bool_2 = True
            if bool_2:
                ball.rect.x += ball.speed
                ball.rect.y -= ball.speed
                if ball.rect.colliderect(gameplayer1.rect):
                    score += 1
                    ball.speed += 0.020
                    bool_2 = False
                    bool_3 = True
                elif ball.rect.x >= 631:
                    win1 = True
                    bool_endstream = True
                elif ball.rect.y <= 0:
                    ball.speed += 0.020
                    bool_2 = False
                    bool_1 = True
            if bool_3:
                ball.rect.x -= ball.speed
                ball.rect.y -= ball.speed
                if ball.rect.colliderect(gameplayer0.rect):
                    score += 1
                    ball.speed += 0.020
                    bool_3 = False
                    bool_2 = True
                elif ball.rect.x <= 0:
                    win2 = True
                    bool_endstream = True
                elif ball.rect.y <= 0:
                    ball.speed += 0.020
                    bool_3 = False
                    bool_4 = True
            if bool_4:
                ball.rect.x -= ball.speed
                ball.rect.y += ball.speed
                if ball.rect.colliderect(gameplayer0.rect):
                    score += 1
                    ball.speed += 0.020
                    bool_4 = False
                    bool_1 = True
                if ball.rect.x <= 0:
                    win2 = True
                    bool_endstream = True
                elif ball.rect.y >= 330:
                    ball.speed += 0.020
                    bool_4 = False
                    bool_3 = True
    for i in event.get():
        if i.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)
