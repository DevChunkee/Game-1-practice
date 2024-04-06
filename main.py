import pygame
import sys

pygame.init()

width, height = 800, 600
FPS = 60
GScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game 1")
#PICTURE = pygame.image.load(os.path.join('resources','pic1.png'))
#SONG = os.path.join(os.getcwd(),'resources/song1.mp3')

def draw_fn():
    GScreen.fill((255,255,255))
    pygame.display.update()
    #pygame.display.update()
def main():
    #pygame.mixer.init()
    #pygame.mixer.music.load(SONG)
    #pygame.mixer.music.play(-1)
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_fn()

if __name__ == "__main__":
    main()