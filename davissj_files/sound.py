import pygame

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()

#Sound Initilization
pygame.mixer.music.load("assets/Automation.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

# Main game Test loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if a key has been pressed
        if event.type == pygame.KEYDOWN:
            # If the 'C' key is pressed, play the sound effect
            if event.key == pygame.K_c:
                pygame.mixer.Sound('assets/crash.mp3').play()
            if event.key == pygame.K_j:
                pygame.mixer.Sound('assets/jump.mp3').play()
            if event.key == pygame.K_h:
                pygame.mixer.Sound('assets/handcuff.mp3').play()    
            if event.key == pygame.K_d:
                pygame.mixer.Sound('assets/dumpster.mp3').play() 
            if event.key == pygame.K_t:
                pygame.mixer.Sound('assets/cone.mp3').play()

    clock.tick(60)

pygame.quit()