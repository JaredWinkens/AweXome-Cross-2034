import winkenj_files.platform as platform
import winkenj_files.player as player
import winkenj_files.passible_enemy as enemySmall
import winkenj_files.not_passible_enemy as enemyLarge
import carterad_files.Splash_screenv3 as Splash_screen
import carterad_files.cop as cop
import carterad_files.cash as cash
import winkenj_files.speed_boost as speed_boost
from carterad_files.cash import save_cash
import souc_files.random_platform as rPlatform
import winkenj_files.background as bg
import pygame
import sys
from pygame.locals import *
import random
import time
import math


# Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w * 0.85
SCREEN_HEIGHT = screen_info.current_h * 0.90

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Game")

def main():
    #Sound Initilization
    pygame.mixer.music.load("assets/Automation.mp3")
    pygame.mixer.music.set_volume(0.25)
    pygame.mixer.music.play(-1)

    # Initialize constants
    #screen_info = pygame.display.Info()
    #SCREEN_WIDTH = screen_info.current_w * 0.85
    #SCREEN_HEIGHT = screen_info.current_h * 0.90
    FPS = 60
    REG_SCORE = 59 
    BONUS_SCORE = 1000

    # Define variables for scorekeeper
    speed = 5
    score: int = 0
    minute: int = 1000 * 60
    second: int = 1000
    fSizeScore = int(SCREEN_HEIGHT // 15)
    fColor = (0, 255, 0)  # Green
    scoreXPos = SCREEN_HEIGHT * .01
    scoreYPos = SCREEN_WIDTH * .01
    gameOver = 0
    FramePerSec = pygame.time.Clock()

    # Load images
    bg_img1 = pygame.transform.scale(pygame.image.load('assets/background_v2/foreground.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_img2 = pygame.transform.scale(pygame.image.load('assets/background_v2/back-buildings.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_img3 = pygame.transform.scale(pygame.image.load('assets/background_v2/far-buildings.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    bg_imgs = [bg_img3,bg_img2,bg_img1]
    player_imgs = []
    for i in range(8): player_imgs.append(pygame.transform.scale((pygame.image.load('assets/fugitive/fugitive_%d.png' % (i+1)).convert_alpha()),(SCREEN_WIDTH*0.06, SCREEN_HEIGHT*0.1)))
    cone_image = pygame.transform.scale(pygame.image.load('assets/cone.png').convert_alpha(),(SCREEN_WIDTH*0.08, SCREEN_HEIGHT*0.14))
    dumpster_image = pygame.transform.scale(pygame.image.load('assets/dumpster.png').convert_alpha(),(SCREEN_WIDTH*0.2, SCREEN_HEIGHT*0.2))
    cop_image = pygame.transform.scale(pygame.image.load('assets/cop.png').convert_alpha(),(SCREEN_WIDTH*0.06, SCREEN_HEIGHT*0.2))

    r_platform_image = pygame.transform.scale(pygame.image.load('assets/new_platform2.png'), (SCREEN_WIDTH * .25, SCREEN_HEIGHT * .045))
    r_platform_image2 = pygame.transform.scale(pygame.image.load('assets/new_platform2.png'), (SCREEN_WIDTH * .15, SCREEN_HEIGHT * .045))

    coin_image = pygame.transform.scale(pygame.image.load('assets/coin.png').convert_alpha(), (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.05))  # Load coin image
    coin_sound = pygame.mixer.Sound('assets/coinGet.mp3')

    splash_image = pygame.transform.scale(pygame.image.load('assets/spalsh_screen.jpeg').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    death_image = pygame.transform.scale(pygame.image.load('assets/death_screen.jpeg').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    pause_image = pygame.transform.scale(pygame.image.load('assets/pause_screen.jpeg').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
    speed_boost_image = pygame.transform.scale(pygame.image.load('assets/speed_boost.png').convert_alpha(), (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.05))

    # Create the player and platform objects
    def create_objects():
        global P1, PT1, BG, cash_instance, cop_spawned, score
        P1 = player.Player(SCREEN_WIDTH, SCREEN_HEIGHT, player_imgs)
        PT1 = platform.Platform(SCREEN_WIDTH, SCREEN_HEIGHT)
        BG = bg.Background(bg_imgs, [speed-2, speed-1, speed])
        cash_instance = cash.Cash(SCREEN_WIDTH, SCREEN_HEIGHT, coin_image)
        cop_spawned = False
        score = 0  # Reset score

    create_objects()
    
    bx = P1.pos.x # Player base x position

    Splash_screen.SplashScreen.run(window,splash_image)

    # Timer (Speed Timer) CHANGE MULTIPLIER TO TWEAK GAME SPEED
    timerSpeed = pygame.event.custom_type()
    pygame.time.set_timer(timerSpeed, 100)

    # Timer (one minute)
    timerMin = pygame.event.custom_type()
    pygame.time.set_timer(timerMin, minute)

    # Timer (one second)
    timerSec = pygame.event.custom_type()
    pygame.time.set_timer(timerSec, second)

    # Timer (two second)
    timerSec2 = pygame.event.custom_type()
    pygame.time.set_timer(timerSec2, second * 2)

    # Timer (three seconds)
    timerSec3 = pygame.event.custom_type()
    pygame.time.set_timer(timerSec3, 3000)

    # Cop spawn timer
    timerSpawnCop = pygame.event.custom_type()
    pygame.time.set_timer(timerSpawnCop, 5000)

    # Create sprite groups
    platforms = pygame.sprite.Group()
    platforms.add(PT1)
    all_sprites = pygame.sprite.Group()
    #all_sprites.add(PT1)
    all_sprites.add(P1)
    small_enemies = pygame.sprite.Group()
    large_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    ranPlat = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    power_ups = pygame.sprite.Group()

    cop_spawned = False  # Track whether the cop has been spawned
    big_enemy_spawned = False  # Track whether the big enemy has been spawned
    sm_obs_sound_played = False # Track whether the small obstacle sound has been played

    def spawn_enemy():
        seed = random.randint(1, 20)
        if seed <= 10:    
            enemy = enemySmall.PassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, cone_image)
            small_enemies.add(enemy)
            enemies.add(enemy)
            all_sprites.add(enemy)
            spawn_coin()
            #spawn_speed_boost()
            #if seed % 2 == 0 or seed == 1 or seed == 9:
            spawnRandomPlatform()
        elif seed > 10 and seed <= 13:
            enemy = enemyLarge.NotPassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, dumpster_image)
            large_enemies.add(enemy)
            enemies.add(enemy)
            all_sprites.add(enemy)
            big_enemy_spawned = True
            newPlatform = rPlatform.RandomPlatform(SCREEN_WIDTH, SCREEN_HEIGHT, r_platform_image)
            ranPlat.add(newPlatform)
            all_sprites.add(newPlatform)
            #spawn_coin()
            #spawn_speed_boost()
        else:
            spawn_coin()
            spawn_speed_boost()
            spawnRandomPlatform()
            print("No enemy spawned")

    # Description: Randomize platform at y position. Check for overlapping
    # before spawning a new platform.
    def spawnRandomPlatform():
        seed = random.randint(1, 20)
        # Set bounds
        xPos = SCREEN_WIDTH
        yPos = random.randint(int(SCREEN_HEIGHT * 0.65), int(SCREEN_HEIGHT * 0.8))

        newPlatform = rPlatform.RandomPlatform(SCREEN_WIDTH, SCREEN_HEIGHT, r_platform_image2)
        newPlatform.rect.center = (xPos, yPos)
        
        hits_large = pygame.sprite.spritecollideany(newPlatform, large_enemies)
        hits_small = pygame.sprite.spritecollideany(newPlatform, small_enemies)
        #hits_platform = pygame.sprite.spritecollideany(newPlatform, ranPlat)
        if hits_large or hits_small: #or hits_platform:
            print("Platform collided with enemy")
        elif seed <= 10:
            ranPlat.add(newPlatform)
            all_sprites.add(newPlatform)

    def spawn_coin():
        #coin_spawned = False
        #while not coin_spawned:
        seed = random.randint(1, 20)
        # Randomly choose a position within the screen boundaries
        x_pos = SCREEN_WIDTH + coin_image.get_width()
        y_pos = random.randint(int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT * 0.9))

        coin = cash.Cash(SCREEN_WIDTH, SCREEN_HEIGHT, coin_image)  # Create a new coin instance
        coin.rect.center = (x_pos, y_pos)

        hits_large = pygame.sprite.spritecollideany(coin, large_enemies)
        hits_small = pygame.sprite.spritecollideany(coin, small_enemies)
        if hits_large or hits_small:
            print("Coin collided with enemy")
        elif seed <= 10:
            coins.add(coin)
            all_sprites.add(coin)
            #coin_spawned = True
                
    def spawn_speed_boost():
        seed = random.randint(1, 20)
        # Randomly choose a position within the screen boundaries
        x_pos = SCREEN_WIDTH + speed_boost_image.get_width()
        y_pos = random.randint(int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT * 0.8))

        boost = speed_boost.SpeedBoost(SCREEN_WIDTH, SCREEN_HEIGHT, speed_boost_image)  # Create a new coin instance
        boost.rect.center = (x_pos, y_pos)

        hits_large = pygame.sprite.spritecollideany(boost, large_enemies)
        hits_small = pygame.sprite.spritecollideany(boost, small_enemies)
        if hits_large or hits_small:
            print("Boost collided with enemy")
        elif seed <= 3:
            power_ups.add(boost)
            all_sprites.add(boost)
            
    ##############################################
    # GAME LOOP
    ##############################################
    while True:
        # Cycle through all events
        for event in pygame.event.get():
            if event.type == QUIT:
                save_cash(cash_instance.coins_collected)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_p:
                    Splash_screen.SplashScreen.pauseScreen(window, pause_image)
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_SPACE:
                    pygame.mixer.Sound('assets/jump.mp3').play()
                    P1.jump(platforms,ranPlat, SCREEN_HEIGHT)
            if event.type == timerSec:
                score += REG_SCORE
                if speed >= 15:
                    spawn_enemy()
            if event.type == timerSec2:
                if speed < 15:   
                    spawn_enemy()
            if event.type == timerSec3:
                print("Current speed: " + str(speed))
            if event.type == timerMin:
                score += BONUS_SCORE
            if event.type == timerSpeed:
                if speed < 20:
                    speed += 0.01
                    #print(speed)
                    print("Current Y velocity: " + str(P1.vel.y))
            if event.type == timerSpawnCop and not cop_spawned:
                C1 = cop.Cop(SCREEN_WIDTH, SCREEN_HEIGHT, PT1, cop_image)  # Spawn the cop
                all_sprites.add(C1)
                cop_spawned = True

        # Render the background
        BG.update(speed)
        # Fill the window with black            
        window.fill((0, 0, 0))
        BG.render(window)

        # update the player
        P1.update(platforms, ranPlat, SCREEN_WIDTH, speed)
        P1.draw(window)

        # Render all sprites
        for entity in all_sprites:
            window.blit(entity.image, entity.rect)

        # Move and draw randomize platforms
        for plat in ranPlat:
            plat.move(speed)
            plat.draw(window)
            
        # Move and draw all enemies
        for enemy in enemies:
            enemy.move(speed)
            enemy.draw(window)
        
        # Move and draw all power-ups
        for power_up in power_ups:
            power_up.move(speed)
            power_up.draw(window)
        
        # Move and draw all coins
        for coin in coins:
            coin.update(speed)
            coin.draw(window)

        # If the cop has been spawned, move and update it
        if cop_spawned:
            C1.move(enemies, P1)  # Move cop
            C1.update(PT1)  # Update cop position if necessary
            C1.draw(window)  # Draw the cop

            # Check for collision between the player and cop
            if pygame.sprite.collide_rect(P1, C1):
                entity.kill()
                save_cash(cash_instance.coins_collected)
            
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:  # Restart game
                                create_objects()  # Reset game state
                                main()
                            if event.key == pygame.K_e:  # Exit game
                                pygame.quit()
                                sys.exit()
                        # Keep the death screen displayed until input is received
                        pygame.time.delay(10)  # Slight delay to reduce CPU usage
                        Splash_screen.SplashScreen.deathScreen(window, score, death_image)
                        pygame.display.flip()

        # Render the score
        Splash_screen.SplashScreen.display_text(window, 'Score: ' + str(score), 
                                            'Cooperplate Gothic Bold', fSizeScore, 
                                            fColor, scoreXPos, scoreYPos)

        # Display the number of coins collected using the Cash class
        cash_instance.display_coins(window, SCREEN_WIDTH)

        # Check for collisions with the player and other sprites
        hits_large = pygame.sprite.spritecollide(P1, large_enemies, False)
        hits_small = pygame.sprite.spritecollide(P1, small_enemies, False)
        hits_boost = pygame.sprite.spritecollide(P1, power_ups, True)
        hits_coin = pygame.sprite.spritecollide(P1, coins, True)
        if hits_large:
            pygame.mixer.Sound('assets/dumpster.mp3').play()
            P1.pos.x = hits_large[0].rect.left - P1.rect.width
        if hits_small:
            if not sm_obs_sound_played:
                pygame.mixer.Sound('assets/cone.mp3').play()
                sm_obs_sound_played = True
            P1.pos.x -= speed/1.5
        if not hits_small:
            sm_obs_sound_played = False                
        if hits_boost:
            P1.pos.x += speed*30
        if hits_coin:
            coin_sound.play()  # Play the collection sound
            cash_instance.collect()  # Increment coins collected in the cash instance
        
        # Update the player's x position
        P1.pos.x += (bx - P1.pos.x) * 0.01
        #print(P1.vel.x)
        #print("Bx: " + str(bx))
        #print("Px: " + str(P1.pos.x))

        # Update the display
        #print(FramePerSec.get_fps())
        pygame.display.update()
        FramePerSec.tick(FPS)
        
main()