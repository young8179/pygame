import pygame
import random
import time

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speedx = random.randrange(-5, 5)
        self.speedy = random.randrange(-5, 5)
    def update(self, height, width):
        if self.rect.x > width or self.rect.x < 0 or self.rect.y > height or self.rect.y < 0:
            self.rect.x = random.randint(0, 490)
            self.rect.y = random.randint(0, 490)
            #if random.randint(0, 100) > 50:
             #   self.direction = 5 
        else:
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
class Monster(Block):
    pass
    
class Goblin(Block):
    pass
class Hero(Block):
    pass

def main():
    width = 510
    height = 480
    blue_color = (255, 255, 255)
    black_color = (0, 0, 0)
    pygame.mixer.init()
    sound_play = pygame.mixer.Sound('sounds/music.wav')
    sound_win = pygame.mixer.Sound('sounds/win.wav')
    sound_lose = pygame.mixer.Sound('sounds/lose.wav')
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
        
    
    
    def text_objects(text, font):
        textsurface = font.render(text, True, black_color)
        return textsurface, textsurface.get_rect()
    def message_display(text, x, y, sleep):
        font = pygame.font.Font(None, 50)
        text_surface, text_rect = text_objects(text, font)
        text_rect = (x, y)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        time.sleep(sleep)
        
    def crash(): 
        message_display("Game over",170, 220, 2)
    def ending():
        message_display("Game will exit in 5 seconds",170, 220, 5)
    def levelup_text(stage): 
        message_display(stage ,170, 220, 2)
    
    def level_1():
            # Hero
        hero = Hero(hero_image, [250, 400])
        hero.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        hero.vx = 5
        hero.vy = 5
        heros_group = pygame.sprite.Group()
        heros_group.add(hero)
    
        
        # monster
        monster = Monster(monster_image, [50, 100])
        monster1 = Monster(monster_image, [213, 80])
        monster2 = Monster(monster_image, [120, 410])
        monster3 = Monster(monster_image, [320, 30])
        monster4 = Monster(monster_image, [320, 30])
        monster5 = Monster(monster_image, [50, 100])
        monster6 = Monster(monster_image, [213, 80])
        monster7 = Monster(monster_image, [120, 410])
        monster8 = Monster(monster_image, [320, 30])
        monster9 = Monster(monster_image, [320, 30])
        monsters_group = pygame.sprite.Group()
        monsters_group.add(monster)
        monsters_group.add(monster1)
        monsters_group.add(monster2)
        monsters_group.add(monster3)
        
        #goblin
        goblin = Goblin(goblin_image, [100, 50])
        goblin1 = Goblin(goblin_image, [150, 210])
        goblin2 = Goblin(goblin_image, [300, 50])
        goblin3 = Goblin(goblin_image, [50, 350])
        goblin4 = Goblin(goblin_image, [400, 290])
        goblin5 = Goblin(goblin_image, [440, 400])
        goblin6 = Goblin(goblin_image, [100, 50])
        goblin7 = Goblin(goblin_image, [150, 210])
        goblin8 = Goblin(goblin_image, [300, 50])
        goblin9 = Goblin(goblin_image, [50, 350])
        goblin10 = Goblin(goblin_image, [400, 290])
        goblin11 = Goblin(goblin_image, [440, 400])
        goblin12 = Goblin(goblin_image, [150, 210])
        goblin13 = Goblin(goblin_image, [300, 50])
        goblin14 = Goblin(goblin_image, [50, 350])
        goblin15 = Goblin(goblin_image, [400, 290])
        goblin16 = Goblin(goblin_image, [440, 400])
        goblins_group = pygame.sprite.Group()
        goblins_group.add(goblin)
        goblins_group.add(goblin1)
        goblins_group.add(goblin2)
        goblins_group.add(goblin3)
        
        
        
        stage_count = 1
        score_count = 0
        
        running = False
        font_score = pygame.font.Font(None, 30)
        font_stage = pygame.font.Font(None, 30)
        
        while not running:
            text_score = font_score.render("Score: " + str(score_count), True, black_color)
            stage_number = font_stage.render("Level " + str(stage_count), True, black_color)
                # Event handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    
                
            
            key = pygame.key.get_pressed()

            for i in range(2):  ## make boundary
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width:
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            #   running = False 
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            
            
            goblin.update(height, width)
            goblin1.update(height, width)
            goblin2.update(height, width)
            goblin3.update(height, width) 
            
           
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            hit_hero = pygame.sprite.spritecollide(hero, goblins_group, True)
            if hit_monsters:
                score_count += 1    
                if score_count == 4:
                    levelup_text("Level 2")
                    
                    break
            elif hit_hero:
                hero.kill()
                sound_play.stop()
                sound_lose.play()
                crash()
                main()
            # win
            
                # Draw background
            
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))
            # Game display
            heros_group.draw(screen)
            goblins_group.draw(screen)
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
        
    #==========================================================================
    def level_2():
        
         # Hero
        hero = Hero(hero_image, [250, 400])
        hero.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        hero.vx = 5
        hero.vy = 5
        heros_group = pygame.sprite.Group()
        heros_group.add(hero)
    
        # monster
        monster = Monster(monster_image, [50, 100])
        monster1 = Monster(monster_image, [213, 80])
        monster2 = Monster(monster_image, [120, 410])
        monster3 = Monster(monster_image, [320, 30])
        monster4 = Monster(monster_image, [320, 30])
        monster5 = Monster(monster_image, [50, 100])
        monster6 = Monster(monster_image, [213, 80])
        monster7 = Monster(monster_image, [120, 410])
        monster8 = Monster(monster_image, [320, 30])
        monster9 = Monster(monster_image, [320, 30])
        monsters_group = pygame.sprite.Group()
        monsters_group.add(monster)
        monsters_group.add(monster1)
        monsters_group.add(monster2)
        monsters_group.add(monster3)
        monsters_group.add(monster4)
        monsters_group.add(monster5)
        
        #goblin
        goblin = Goblin(goblin_image, [100, 50])
        goblin1 = Goblin(goblin_image, [150, 210])
        goblin2 = Goblin(goblin_image, [300, 50])
        goblin3 = Goblin(goblin_image, [50, 350])
        goblin4 = Goblin(goblin_image, [400, 290])
        goblin5 = Goblin(goblin_image, [440, 400])
        goblin6 = Goblin(goblin_image, [100, 50])
        goblin7 = Goblin(goblin_image, [150, 210])
        goblin8 = Goblin(goblin_image, [300, 50])
        goblin9 = Goblin(goblin_image, [50, 350])
        goblin10 = Goblin(goblin_image, [400, 290])
        goblin11 = Goblin(goblin_image, [440, 400])
        goblin12 = Goblin(goblin_image, [150, 210])
        goblin13 = Goblin(goblin_image, [300, 50])
        goblin14 = Goblin(goblin_image, [50, 350])
        goblin15 = Goblin(goblin_image, [400, 290])
        goblin16 = Goblin(goblin_image, [440, 400])
        goblins_group = pygame.sprite.Group()
        goblins_group.add(goblin)
        goblins_group.add(goblin1)
        goblins_group.add(goblin2)
        goblins_group.add(goblin3)
        goblins_group.add(goblin4)
        goblins_group.add(goblin5)
        
        
        stage_count = 2
        score_count = 4
        
        running = False
        font_score = pygame.font.Font(None, 30)
        font_stage = pygame.font.Font(None, 30)
        
        
        while not running:
            text_score = font_score.render("Score: " + str(score_count), True, black_color)
            stage_number = font_stage.render("Level " + str(stage_count), True, black_color)
                # Event handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            key = pygame.key.get_pressed()

            for i in range(2):  ## make boundary
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width:
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            #   running = False 
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            monster4.update(height, width)
            monster5.update(height, width)
           

            goblin.update(height, width)
            goblin1.update(height, width)
            goblin2.update(height, width)
            goblin3.update(height, width) 
            goblin4.update(height, width)
            goblin5.update(height, width)
            
            
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            hit_hero = pygame.sprite.spritecollide(hero, goblins_group, True)
            if hit_monsters:
                score_count += 1    
                if score_count == 10:
                    levelup_text("Level 3")
                    break
            elif hit_hero:
                hero.kill()
                sound_play.stop()
                sound_lose.play()
                crash()
                main()
            # win
            
                # Draw background
        
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))
            
            # Game display
            heros_group.draw(screen)
            goblins_group.draw(screen)
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
    #--===================================================================
    def level_3():
        
         # Hero
        hero = Hero(hero_image, [250, 400])
        hero.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        hero.vx = 5
        hero.vy = 5
        heros_group = pygame.sprite.Group()
        heros_group.add(hero)
    
        # monster
        monster = Monster(monster_image, [50, 100])
        monster1 = Monster(monster_image, [213, 80])
        monster2 = Monster(monster_image, [120, 410])
        monster3 = Monster(monster_image, [320, 30])
        monster4 = Monster(monster_image, [320, 30])
        monster5 = Monster(monster_image, [50, 100])
        monster6 = Monster(monster_image, [213, 80])
        monster7 = Monster(monster_image, [120, 410])
        monster8 = Monster(monster_image, [320, 30])
        monster9 = Monster(monster_image, [320, 30])
        monsters_group = pygame.sprite.Group()
        monsters_group.add(monster)
        monsters_group.add(monster1)
        monsters_group.add(monster2)
        monsters_group.add(monster3)
        monsters_group.add(monster4)
        monsters_group.add(monster5)
        monsters_group.add(monster6)
        monsters_group.add(monster7)
        #goblin
        goblin = Goblin(goblin_image, [100, 50])
        goblin1 = Goblin(goblin_image, [150, 210])
        goblin2 = Goblin(goblin_image, [300, 50])
        goblin3 = Goblin(goblin_image, [50, 350])
        goblin4 = Goblin(goblin_image, [400, 290])
        goblin5 = Goblin(goblin_image, [440, 400])
        goblin6 = Goblin(goblin_image, [100, 50])
        goblin7 = Goblin(goblin_image, [150, 210])
        goblin8 = Goblin(goblin_image, [300, 50])
        goblin9 = Goblin(goblin_image, [50, 350])
        goblin10 = Goblin(goblin_image, [400, 290])
        goblin11 = Goblin(goblin_image, [440, 400])
        goblin12 = Goblin(goblin_image, [150, 210])
        goblin13 = Goblin(goblin_image, [300, 50])
        goblin14 = Goblin(goblin_image, [50, 350])
        goblin15 = Goblin(goblin_image, [400, 290])
        goblin16 = Goblin(goblin_image, [440, 400])
        goblins_group = pygame.sprite.Group()
        goblins_group.add(goblin)
        goblins_group.add(goblin1)
        goblins_group.add(goblin2)
        goblins_group.add(goblin3)
        goblins_group.add(goblin4)
        goblins_group.add(goblin5)
        goblins_group.add(goblin6)
        goblins_group.add(goblin7)
        
        
        stage_count = 3
        score_count = 10
        
        running = False
        font_score = pygame.font.Font(None, 30)
        font_stage = pygame.font.Font(None, 30)
        
        while not running:
            text_score = font_score.render("Score: " + str(score_count), True, black_color)
            stage_number = font_stage.render("Level : " + str(stage_count), True, black_color)
                # Event handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = True
                
            
            key = pygame.key.get_pressed()

            for i in range(2):  ## make boundary
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width:
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            #   running = False 
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            monster4.update(height, width)
            monster5.update(height, width)
            monster6.update(height, width)
            monster7.update(height, width)
            
            goblin.update(height, width)
            goblin1.update(height, width)
            goblin2.update(height, width)
            goblin3.update(height, width) 
            goblin4.update(height, width)
            goblin5.update(height, width)
            goblin6.update(height, width) 
            goblin7.update(height, width)
            
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            hit_hero = pygame.sprite.spritecollide(hero, goblins_group, True)
            if hit_monsters:
                score_count += 1    
                if score_count == 18:
                    levelup_text("Level 4")
                    break
            elif hit_hero:
                hero.kill()
                sound_play.stop()
                sound_lose.play()
                crash()
                main()
            # win
            
                # Draw background
            
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))

            # Game display
            heros_group.draw(screen)
            goblins_group.draw(screen)
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
    #----------------------------------------------------------------------
    def level_4():
         # Hero
        hero = Hero(hero_image, [250, 400])
        hero.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        hero.vx = 5
        hero.vy = 5
        heros_group = pygame.sprite.Group()
        heros_group.add(hero)
    
        # monster
        monster = Monster(monster_image, [50, 100])
        monster1 = Monster(monster_image, [213, 80])
        monster2 = Monster(monster_image, [120, 410])
        monster3 = Monster(monster_image, [320, 30])
        monster4 = Monster(monster_image, [320, 30])
        monster5 = Monster(monster_image, [50, 100])
        monster6 = Monster(monster_image, [213, 80])
        monster7 = Monster(monster_image, [120, 410])
        monster8 = Monster(monster_image, [320, 30])
        monster9 = Monster(monster_image, [320, 30])
        monsters_group = pygame.sprite.Group()
        monsters_group.add(monster)
        monsters_group.add(monster1)
        monsters_group.add(monster2)
        monsters_group.add(monster3)
        monsters_group.add(monster4)
        monsters_group.add(monster5)
        monsters_group.add(monster6)
        monsters_group.add(monster7)
        monsters_group.add(monster8)
        monsters_group.add(monster9)
        
        #goblin
        goblin = Goblin(goblin_image, [100, 50])
        goblin1 = Goblin(goblin_image, [150, 210])
        goblin2 = Goblin(goblin_image, [300, 50])
        goblin3 = Goblin(goblin_image, [50, 350])
        goblin4 = Goblin(goblin_image, [400, 290])
        goblin5 = Goblin(goblin_image, [440, 400])
        goblin6 = Goblin(goblin_image, [100, 50])
        goblin7 = Goblin(goblin_image, [150, 210])
        goblin8 = Goblin(goblin_image, [300, 50])
        goblin9 = Goblin(goblin_image, [50, 350])
        goblin10 = Goblin(goblin_image, [400, 290])
        goblin11 = Goblin(goblin_image, [440, 400])
        goblin12 = Goblin(goblin_image, [150, 210])
        goblin13 = Goblin(goblin_image, [300, 50])
        goblin14 = Goblin(goblin_image, [50, 350])
        goblin15 = Goblin(goblin_image, [400, 290])
        goblin16 = Goblin(goblin_image, [440, 400])
        goblins_group = pygame.sprite.Group()
        goblins_group.add(goblin)
        goblins_group.add(goblin1)
        goblins_group.add(goblin2)
        goblins_group.add(goblin3)
        goblins_group.add(goblin4)
        goblins_group.add(goblin5)
        goblins_group.add(goblin6)
        goblins_group.add(goblin7)
        goblins_group.add(goblin8)
        goblins_group.add(goblin9)
        
        
        stage_count = 4
        score_count = 18
        
        running = False
        font_score = pygame.font.Font(None, 30)
        font_stage = pygame.font.Font(None, 30)
        
        while not running:
            text_score = font_score.render("Score: " + str(score_count), True, black_color)
            stage_number = font_stage.render("Level : " + str(stage_count), True, black_color)
                # Event handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            key = pygame.key.get_pressed()

            for i in range(2):  ## make boundary
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width:
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            #   running = False 
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            monster4.update(height, width)
            monster5.update(height, width)
            monster6.update(height, width)
            monster7.update(height, width)
            monster8.update(height, width)
            monster9.update(height, width)

            goblin.update(height, width)
            goblin1.update(height, width)
            goblin2.update(height, width)
            goblin3.update(height, width) 
            goblin4.update(height, width)
            goblin5.update(height, width)
            goblin6.update(height, width) 
            goblin7.update(height, width)
            goblin8.update(height, width) 
            goblin9.update(height, width)
            
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            hit_hero = pygame.sprite.spritecollide(hero, goblins_group, True)
            if hit_monsters:
                score_count += 1    
                if score_count == 28:
                    levelup_text("Level 5")
                    break
            elif hit_hero:
                hero.kill()
                sound_play.stop()
                sound_lose.play()
                crash()
                main()
            # win
            
                # Draw background
            
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))

            # Game display
            heros_group.draw(screen)
            goblins_group.draw(screen)
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
    #=====================================================================
    def level_5():
         # Hero
        hero = Hero(hero_image, [250, 400])
        hero.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        hero.vx = 5
        hero.vy = 5
        heros_group = pygame.sprite.Group()
        heros_group.add(hero)
    
        
        # monster
        monster = Monster(monster_image, [50, 100])
        monster1 = Monster(monster_image, [213, 80])
        monster2 = Monster(monster_image, [120, 410])
        monster3 = Monster(monster_image, [320, 430])
        monster4 = Monster(monster_image, [320, 30])
        monster5 = Monster(monster_image, [50, 100])
        monster6 = Monster(monster_image, [213, 80])
        monster7 = Monster(monster_image, [120, 410])
        monster8 = Monster(monster_image, [320, 30])
        monster9 = Monster(monster_image, [320, 124])
        monster10 = Monster(monster_image, [200, 30])
        monster11 = Monster(monster_image, [220, 400])
        monsters_group = pygame.sprite.Group()
        monsters_group.add(monster)
        monsters_group.add(monster1)
        monsters_group.add(monster2)
        monsters_group.add(monster3)
        monsters_group.add(monster4)
        monsters_group.add(monster5)
        monsters_group.add(monster6)
        monsters_group.add(monster7)
        monsters_group.add(monster8)
        monsters_group.add(monster9)
        monsters_group.add(monster10)
        monsters_group.add(monster11)
        
        #goblin
        goblin = Goblin(goblin_image, [100, 50])
        goblin1 = Goblin(goblin_image, [150, 210])
        goblin2 = Goblin(goblin_image, [300, 50])
        goblin3 = Goblin(goblin_image, [50, 350])
        goblin4 = Goblin(goblin_image, [400, 290])
        goblin5 = Goblin(goblin_image, [440, 400])
        goblin6 = Goblin(goblin_image, [100, 50])
        goblin7 = Goblin(goblin_image, [150, 210])
        goblin8 = Goblin(goblin_image, [300, 50])
        goblin9 = Goblin(goblin_image, [50, 350])
        goblin10 = Goblin(goblin_image, [400, 290])
        goblin11 = Goblin(goblin_image, [440, 400])
        goblin12 = Goblin(goblin_image, [150, 210])
        goblin13 = Goblin(goblin_image, [300, 50])
        goblin14 = Goblin(goblin_image, [50, 350])
        goblin15 = Goblin(goblin_image, [400, 290])
        goblin16 = Goblin(goblin_image, [440, 400])
        goblins_group = pygame.sprite.Group()
        goblins_group.add(goblin)
        goblins_group.add(goblin1)
        goblins_group.add(goblin2)
        goblins_group.add(goblin3)
        goblins_group.add(goblin4)
        goblins_group.add(goblin5)
        goblins_group.add(goblin6)
        goblins_group.add(goblin7)
        goblins_group.add(goblin8)
        goblins_group.add(goblin9)
        goblins_group.add(goblin10)
        goblins_group.add(goblin11)
        
        
        stage_count = 5
        score_count = 28
        
        running = False
        font_score = pygame.font.Font(None, 30)
        font_stage = pygame.font.Font(None, 30)
        
        while not running:
            text_score = font_score.render("Score: " + str(score_count), True, black_color)
            stage_number = font_stage.render("Score: " + str(stage_count), True, black_color)
                # Event handling
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            key = pygame.key.get_pressed()

            for i in range(2):  ## make boundary
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width:
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            #   running = False 
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            monster4.update(height, width)
            monster5.update(height, width)
            monster6.update(height, width)
            monster7.update(height, width)
            monster8.update(height, width)
            monster9.update(height, width)
            monster10.update(height, width)
            monster11.update(height, width)

            goblin.update(height, width)
            goblin1.update(height, width)
            goblin2.update(height, width)
            goblin3.update(height, width) 
            goblin4.update(height, width)
            goblin5.update(height, width)
            goblin6.update(height, width) 
            goblin7.update(height, width)
            goblin8.update(height, width) 
            goblin9.update(height, width)
            goblin10.update(height, width)
            goblin11.update(height, width)
            
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            hit_hero = pygame.sprite.spritecollide(hero, goblins_group, True)
            if hit_monsters:
                score_count += 1    
                if score_count == 40:
                    levelup_text("You've completed ALL LEVELS!")
                    ending()
                    break
            elif hit_hero:
                hero.kill()
                sound_play.stop()
                sound_lose.play()
                crash()
                main()
            # win
            
                # Draw background
            
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))

            # Game display
            heros_group.draw(screen)
            goblins_group.draw(screen)
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)

    #def paused():
    
    #   largeText = pygame.font.SysFont("comicsansms",115)
    #   TextSurf, TextRect = text_objects("Paused", largeText)
    #   TextRect.center = ((width/2),(height/2))
    #   screen.blit(TextSurf, TextRect)
        
       
        

    #load image
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    goblin_image = pygame.image.load('images/goblin.png').convert_alpha()
    
    
    
    
    
    sound_play.play()

    hero_width =32
    hero_height = 32
    
    level_1()   
    level_2()
    level_3()
    level_4()
    level_5()
    
    
          
    
    pygame.quit()

if __name__ == '__main__':
    main()
