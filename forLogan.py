import pygame
import random
import time
import pygame.font 

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):

        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos
    def update(self, height, width):
        if self.rect.x > width or self.rect.x < 0 or self.rect.y > height or self.rect.y < 0:
            self.rect.x = random.randint(0, 490)
            self.rect.y = random.randint(0, 490)
            #if random.randint(0, 100) > 50:
             #   self.direction = 5 
        else:
            
            if True :
                
                direction = random.randrange(0,50)
                if direction == 0:
                    for i in range(10):
                        self.rect.y -= 1
                        self.rect.y -= 1
                elif direction == 1:
                    for i in range(10):
                        self.rect.x += 1
                        self.rect.x += 1
                elif direction == 2:
                    for i in range(10):
                        self.rect.y += 1
                        self.rect.y += 1
                elif direction == 3:
                    for i in range(10):
                        self.rect.x -= 1
                        self.rect.x -= 1
                elif direction == 4:
                    for i in range(10):
                        self.rect.y += 1
                        self.rect.x += 1
                elif direction == 5:
                    for i in range(10):
                        self.rect.x -= 1
                        self.rect.y -= 1
                elif direction == 4:
                    for i in range(10):
                        self.rect.y += 1
                        self.rect.x -= 1
                elif direction == 5:
                    for i in range(10):
                        self.rect.x += 1
                        self.rect.y -= 1
                
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
        
    
    sound_play.play()
    def text_objects(text, font):
        textsurface = font.render(text, True, black_color)
        return textsurface, textsurface.get_rect()
    def message_display(text, x, y, sleep):
        font = pygame.font.Font("fonts/Concert_One/ConcertOne-Regular.ttf", 30)
        text_surface, text_rect = text_objects(text, font)
        text_rect = (x, y)
        screen.blit(text_surface, text_rect)
        pygame.display.update()
        time.sleep(sleep)
        
    def crash(): 
        message_display("Game over",190, 150, 0)
        message_display("Enter to play agin",140, 185, 0)
        message_display("Space to quit",170, 220, 5)
        
    def ending():
        message_display("Game will exit in 5 seconds",170, 220, 5)
    def levelup_text(stage): 
        message_display(stage ,220, 220, 2)
    
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

            for i in range(2):  
                if key[hero.move[i]]:
                    hero.rect.x += hero.vx * [-1, 1][i]

            for i in range(2):
                if key[hero.move[2:4][i]]:
                    hero.rect.y += hero.vy * [-1, 1][i]
            
        
            if hero.rect.x > width - hero_width: ## make boundary
                hero.rect.x -= 10
            elif hero.rect.x < 0:
                hero.rect.x += 10 
            elif hero.rect.y < 0: 
                hero.rect.y += 10
            elif hero.rect.y > height - hero_height:
                hero.rect.y -= 10     
            
            monster.update(height, width)
            monster1.update(height, width)
            monster2.update(height, width)
            monster3.update(height, width)
            
            
           
           
            
            
            # hit or die   
            hit_monsters = pygame.sprite.spritecollide(hero, monsters_group, True)
            
            if hit_monsters:
                score_count += 1    
                if score_count == 4:
                    levelup_text("Level 2")
                    sound_play.stop()
                    main()
                   
           
                
               
                           
            
            
                # Draw background
            
            screen.blit(background_image, [0, 0])
            screen.blit(text_score,(30, 30))
            screen.blit(stage_number,(410, 30))
            # Game display
            heros_group.draw(screen)
            
            monsters_group.draw(screen)
            pygame.display.update()
            clock.tick(60)
        
    #==========================================================================
               
        

    #def paused():
    
    #   largeText = pygame.font.SysFont("comicsansms",115)
    #   TextSurf, TextRect = text_objects("Paused", largeText)
    #   TextRect.center = ((width/2),(height/2))
    #   screen.blit(TextSurf, TextRect)
        
       
        

    #load image
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    
    
    
    
    
    
    

    hero_width =32
    hero_height = 32
    
    level_1()   
   
    
    
          
    
    pygame.quit()

if __name__ == '__main__':
    main()
