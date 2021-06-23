from random import randint
import time
import pygame
pygame.init()

W, H = 600, 600
FPS = 60
DELTA = 1
PHRASE_Y = 60
BOX_W, BOX_H = 100, 100
BLACK = (0, 0, 0)
GRAY = (192, 192, 192)
GREEN = (7, 173, 98)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
CYAN = (129, 192, 255)
BOX_IMAGE = pygame.transform.scale(pygame.image.load("Box Game\Box.jpg") , (BOX_W, BOX_H))
FONT = pygame.font.Font("freesansbold.ttf", 20)
SCORE_FONT = pygame.font.Font("freesansbold.ttf", 400)

WINDOW = pygame.display.set_mode((W, H))
pygame.display.set_caption("TICK THE BOX !")
WINDOW.fill(GRAY)

def draw(x, y, score):
    WINDOW.fill(GRAY)
    LABEL = FONT.render(f"TICK THE BOX UNDER {DELTA} SECONDS !", True, GREEN)
    LABEL_RECT = LABEL.get_rect()
    LABEL_RECT.centerx = W // 2
    LABEL_RECT.centery = 30
    WINDOW.blit(LABEL, LABEL_RECT)
    phrase = FONT.render(f"SCORE: {score}", True, BLACK)
    phrase_rect = phrase.get_rect()
    phrase_rect.centerx = W //2
    phrase_rect.centery = PHRASE_Y
    WINDOW.blit(phrase, phrase_rect)
    WINDOW.blit(BOX_IMAGE, (x, y))
    pygame.display.update()
    box_drawing_date = time.time()
    return box_drawing_date

def draw_loosing_screen(score):
    WINDOW.fill(CYAN)
    loosing_phrase = FONT.render(f"YOU LOST ! YOUR SCORE WAS:", True, WHITE)
    loosing_phrase_rect = loosing_phrase.get_rect()
    loosing_phrase_rect.centerx = W // 2
    loosing_phrase_rect.centery = 100
    WINDOW.blit(loosing_phrase, loosing_phrase_rect)
    score_phrase = SCORE_FONT.render(f"{score}", True, RED)
    score_phrase_rect = score_phrase.get_rect()
    score_phrase_rect.centerx = W // 2
    score_phrase_rect.centery = 350
    WINDOW.blit(score_phrase, score_phrase_rect)
    pygame.display.update()

def mainloop():
    score = 0
    run = True
    x, y = (W - BOX_W) // 2, (H - BOX_H) // 2
    box_drawing_date = draw(x, y, score)
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                click_date = time.time()
                if click_date - box_drawing_date > DELTA:
                        draw_loosing_screen(score)
                if x < mouse_x < x + BOX_W and y + BOX_H > mouse_y > y:
                    if click_date - box_drawing_date > DELTA:
                        draw_loosing_screen(score)
                    else:    
                        score += 1
                        x = randint(BOX_W, W - BOX_W)
                        y = randint(BOX_H, H - BOX_H)
                        box_drawing_date = draw(x, y, score)
    pygame.quit()

mainloop()